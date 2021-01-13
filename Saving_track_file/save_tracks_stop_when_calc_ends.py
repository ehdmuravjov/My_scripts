import re
import os
from datetime import datetime
from datetime import timedelta

path_list = [
    r'dir\file_name1.tracks',
    r'dir\file_name2.tracks'
]

def make_new_track_name(path_track):
    now_date = datetime.now()
    name, ext = path_track.split('\\')[-1].split('.')
    path = re.findall(r'.+(?=\\\w+\.tracks)',path_track)[0] + '\\'
    path_to_save = path + name + '_saved_on_' + now_date.strftime("%d_%b_%H_%M") + '.' + ext
    return path_to_save

def save_track(path_track):
    f = open(path_track, 'rb')
    data = f.readlines()
    f.close()

    path_to_save = make_new_track_name(path_track)
    file = open(path_to_save, 'wb')
    for line in data:
          file.write(line)
    file.close()

def find_res_file(path_track):
    name = path_track.split('\\')[-1].split('.')[0]
    name = name[:-2]
    path_res_file = re.findall(r'.+(?=\\\w+\.tracks)',path_track)[0] + '\\' + name + '.res'
    return path_res_file

def main(path_track):
    res_file = find_res_file(path_track)
    mod_time = os.path.getmtime(res_file)

    if datetime.now() - datetime.fromtimestamp(mod_time) < timedelta(minutes=1):
        save_track(path_track)
        return print("Запись треков прошла успешно")
    else:
        return print("Расчет уже закончен")

for path_track in path_list:
    main(path_track)