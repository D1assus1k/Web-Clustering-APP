from utils import json_to_dict_list


def is_user_by_login(username):
    print('_____________________Функция определения ID начала свою работу_____________________')
    json_array = json_to_dict_list('Data/data.json')

    def find_all_by_key(iterable, keys, value):
        for index, dict_ in enumerate(iterable):
            if keys in dict_ and dict_[keys] == value:
                return dict_
    dictionary = find_all_by_key(json_array, 'login', username)
    if dictionary is None:
        return None, None, None
    login = dictionary.get('login')
    password = dictionary.get('password')
    return login, password