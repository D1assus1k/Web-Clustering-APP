from utils import json_to_dict_list


def get_file_values(USER_ID):
    json_claster = json_to_dict_list('Data/cluster-save.json')
    def find_all_by_key(iterable, key, value):
        for index, dict_ in enumerate(iterable):
            if key in dict_ and dict_[key] == value:
                return dict_
    dicti = find_all_by_key(json_claster, 'ID', USER_ID)
    file_values = []
    values = list(dicti.values())
    values.remove(values[0])
    for i in values:
        if '.csv' in i:
            file_values.append(i)
    file_values = (' '.join(map(str, file_values)))
    return file_values



