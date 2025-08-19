from collections import defaultdict
from utils import json_to_dict_list
from flask import request

def registration_user():
    json_array = json_to_dict_list('Data/data.json')
    data = request.form
    login = data['login']
    email = data['email']
    dictionary = defaultdict(list)
    for i in json_array:
        for k, v in i.items():
            dictionary[k].append(v)
    array_of_arrays = list(dictionary.values())
    array = []
    for j in range(len(array_of_arrays)):
        array.extend(array_of_arrays[j])

    if login not in array and email not in array:
        return True
    elif login in array:
        return False
    elif email in array:
        return False
