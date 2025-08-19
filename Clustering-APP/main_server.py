from flask import Flask, render_template, request, url_for, redirect
import pandas as pd
from utils import json_to_dict_list
from utils import dict_list_to_json
from save_process import save_ID
from login_process import login_user_check
from registration_process import registration_user
from check_files import filena
from clusterization import clusterization_process
from is_user_by_login import is_user_by_login
from visual import make_dash, make_layout
from libary import get_file_values
import hmac
import hashlib
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

X = None
Y = None
hash_key = b'/@cet%#3f&u0A27Tye%!ifn/?>mg5'
app = Flask(__name__)
app.secret_key = 'your_secret_key'
dash_app = make_dash(app)
dash_app.layout = make_layout(X, Y)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'ID'


@app.route('/')
@app.route('/main')
@app.route('/main.html')
def get_main():
    return render_template('main.html')


@app.route('/dash')
@login_required
def get_dash():
    return render_template('dash.html')


@app.route('/files')
@login_required
def get_files():
    return render_template('file-load.html')


@app.route('/login')
def get_login():
    return render_template('login.html')


@app.route('/acсount')
def get_account():
    return render_template('acсount.html')


@app.route('/register')
def get_register():
    return render_template('register.html')


def is_user_by_name(username):
    username = username
    login, password = is_user_by_login(username)
    return login, password


class User(UserMixin):
    def __init__(self, login, password):
        self.id = login
        self.password = password


@login_manager.user_loader
def load_user(user_name):
    print(user_name)
    login, password = is_user_by_name(user_name)
    if not(id is None):
        return User(login, password)
    return None


@app.route('/libary')
@login_required
def libary_claster():
    ID = save_ID(current_user.id)
    arr = get_file_values(ID)
    return render_template('libary.html', arr=arr)


@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    global datafilejs
    datafile = request.files['file']
    datafilejs = request.files['file'].filename
    data = request.form
    X = data['X']
    Y = data['Y']
    if datafile:
        try:
            df = pd.read_csv(datafile)
            new_df = pd.DataFrame({
                'x': df[X],
                'y': df[Y]
            })
            filename = 'test-user.csv'
            new_df.to_csv(filename, index=False)
            print('_____________________', 'Файл', datafilejs, 'сохранен как', filename, '_____________________')
        except KeyError:
            print('_____________________', 'Указаны неверные имена столбцов', '_____________________')
            return render_template('wrong-column.html')
    else:
        print('_____________________', "Файл не был загружен", '_____________________')
        return "Файл не был загружен"
    optimal_clusters, largest_cluster_name, largest_cluster_size, optimal_silhouette_score = clusterization_process(
        'test-user.csv')
    dash_app.layout = make_layout(X, Y)
    return render_template('dash.html', number=optimal_clusters, silhouette=optimal_silhouette_score, cluster_name=largest_cluster_name, size=largest_cluster_size)


@app.route('/save', methods=['POST'])
@login_required
def save():
    global datafilejs
    print('current_user.id')
    ID = save_ID(current_user.id)
    DATA = datafilejs
    file_dict = filena(ID, DATA)
    if file_dict:
        print(
            "_____________________Такого файла нет списке cluster-save.json, файл и ID добавлены успешно_____________________")
        return render_template('dashsave.html')
    elif not file_dict:
        print(
            "_____________________Такой файл есть в списке cluster-save.json, добавление файла и ID отколено_____________________")
        return render_template('dashsave_failed.html')


@app.route('/submit', methods=['POST'])
def log():
    data = request.form
    process = login_user_check()
    login = data['login']
    password = data['password'].encode('utf-8')
    hmac_object = hmac.new(hash_key, password, hashlib.sha256)
    password = hmac_object.hexdigest()
    id = save_ID(login)
    print('key:', id)
    print('_____________________Логин введенный пользователем:', login, '_____________________')
    print('_____________________Пароль введенный пользователем:', data['password'], '_____________________')
    if id is None:
        return redirect('login-failed.html', login=data['login'])
    if login and password in process:
        user = User(login, password)
        print(user)
        login_user(user)
        return redirect(url_for('dashboard'))
        print('_____________________Пароль и логин совпали со списком data.json_____________________')
    return render_template('login-failed.html', login=data['login'])


@app.route('/reg', methods=['POST'])
def reg():
    data = request.form
    json_array = json_to_dict_list('Data/data.json')
    reg_proc = registration_user()
    i = len(json_array)
    password = data['password'].encode('utf-8')
    hmac_object = hmac.new(hash_key, password, hashlib.sha256)
    final_pass = hmac_object.hexdigest()
    list_user = {
        "ID": i,
        "login": data['login'],
        "password": final_pass,
        "email": data['email']
    }
    if reg_proc:
        print(
            "_____________________Такого пользователя нет списке data.json, регистрация прошла успешно_____________________")
        json_array.append(list_user)
        dict_list_to_json(json_array, 'Data/data.json')
        return render_template('registration-done.html', login=data['login'], password=data['password'],
                               email=data['email'])
    elif not reg_proc:
        print(
            '_____________________Такой пользователь есть списке data.json, регистрация отклонена_____________________')
        return render_template('registration-failed.html', login=data['login'])


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('login-done.html', login=current_user.id)


@app.route("/logout", methods = ['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('log'))

if __name__ == '__main__':
    app.run(debug=True, port=8000)
