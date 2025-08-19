from utils import json_to_dict_list


def save_ID(login):
    print('_____________________Функция определения ID начала свою работу_____________________')
    json_array = json_to_dict_list('Data/data.json')
    def find_all_by_key(iterable, keys, value):
        for index, dict_ in enumerate(iterable):
            if keys in dict_ and dict_[keys] == value:
                return dict_

    dictionary = find_all_by_key(json_array, 'login', login)
    key = dictionary.get('ID')
    print('_________________________________ ID Определено_________________________________')
    return key
