from collections import defaultdict
from utils import json_to_dict_list


def login_user_check():
    json_array = json_to_dict_list('Data/data.json')
    dicti = defaultdict(list)
    for i in json_array:
        for k, v in i.items():
            dicti[k].append(v)
    array_of_arrays = list(dicti.values())
    array = []
    for j in range(len(array_of_arrays)):
        array.extend(array_of_arrays[j])
    return array
