from utils import json_to_dict_list
from utils import dict_list_to_json

def filena(USER_ID, datafilejs):
    print('_____________________Функция проверки массива cluster-save.json начала свою работу_____________________')
    json_claster = json_to_dict_list('Data/cluster-save.json')
    def find_all_by_key(iterable, keys, value):
        for index, dict_ in enumerate(iterable):
            if keys in dict_ and dict_[keys] == value:
                return dict_
    dicti = find_all_by_key(json_claster, 'ID', USER_ID)
    if dicti:
        json_claster.remove(dicti)
        values = list(dicti.values())
        if datafilejs not in values:
            key = 'file'
            i = 1
            while key in dicti:
                key = f'file{i}'
                i += 1
            dicti[key] = datafilejs
            json_claster.append(dicti)
            dict_list_to_json(json_claster, 'Data/cluster-save.json')
            return True
        else:
            json_claster.append(dicti)
            dict_list_to_json(json_claster, 'Data/cluster-save.json')
            return False
    else:
        listik = {'ID': USER_ID, 'file': datafilejs}
        json_claster.append(listik)
        dict_list_to_json(json_claster, 'Data/cluster-save.json')
        return True
