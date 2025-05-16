# -*- coding: utf-8 -*-
# v231018
import os
import sys
from collections import OrderedDict
import xml.etree.ElementTree as ET
import json
import subprocess
import re

# 현재 스크립트 파일의 절대 경로 추출
script_dir = os.path.dirname(os.path.abspath(__file__))

# deploy.prototxt.txt 파일의 상대 경로
# president_info = 'president_info_k-e.csv' # 전체인물 대상
# ke_mapping = 'new_k-e_mapping.csv'
ke_mapping_name = 'new_k-e_mapping_name.csv'
# ke_mapping_last = 'new_k-e_mapping_last_name.csv'

people_list_army = 'people_list_army.csv'       # 군
people_list_policy = 'people_list_policy.csv'   # 정
people_list_party = 'people_list_party.csv'     # 당
people_list_normal = 'people_list_normal.csv'     # 당

# people_list.csv 파일의 절대 경로
# president_info_file_path = os.path.join(script_dir, president_info)
# ke_mapping_file_path = os.path.join(script_dir, ke_mapping)
ke_mapping_file_path_name = os.path.join(script_dir, ke_mapping_name)
# ke_mapping_file_path_last = os.path.join(script_dir, ke_mapping_last)

army_file_path = os.path.join(script_dir, people_list_army)
policy_file_path = os.path.join(script_dir, people_list_policy)
party_file_path = os.path.join(script_dir, people_list_party)
normal_file_path = os.path.join(script_dir, people_list_normal)

def search_kor_name_in_csv(char: str, is_last: bool=False):
    # csv_file = ke_mapping_file_path_last if is_last else ke_mapping_file_path_name
    csv_file = ke_mapping_file_path_name
    search_column = 'ko'
    search_value = char
    target_column = 'en'
    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row[search_column] == search_value:
                return row[target_column]
    if is_last:
        csv_file = ke_mapping_file_path_name
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row[search_column] == search_value:
                    return row[target_column]
    return None

# def search_kor_name_from_db(kor_name: str):
#     search_column = 'ko'
#     search_keyword = kor_name
#     return_column = 'en'
#     with open(army_file_path, 'r', encoding='utf-8-sig') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             if row[search_column] == search_keyword:
#                 name1 = row[return_column]
#                 type = 'army'
#                 note = '군'

#     with open(policy_file_path, 'r', encoding='utf-8-sig') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             if row[search_column] == search_keyword:
#                 name2 = row[return_column]
#                 type = 'policy'
#                 note = '정'

#     with open(party_file_path, 'r', encoding='utf-8-sig') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             if row[search_column] == search_keyword:
#                 name3 = row[return_column]
#                 type = 'party'
#                 note = '당'

#     with open(party_file_path, 'r', encoding='utf-8-sig') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             if row[search_column] == search_keyword:
#                 name3 = row[return_column]
#                 type = 'normal'
#                 note = '기타'

#     name_result = {}
#     if name1:
#         name_result['name'] = {
#             'text': name1
#         }
#     elif name2:
#         name_result['name'] = {
#             'text': name2
#         }
#     elif name3:
#         name_result['name'] = {
#             'text': name3
#         }
#     return name_result

def get_kor_char_from_csv(name: str, type='normal'):
    name = name.strip()
    print('Line 112 ', name)
    kor_num_pattern = r"^([가-힣]+)(_)?(.+)?"
    is_kor_name = re.compile(kor_num_pattern)
    is_eng_name = re.compile(r"^([a-zA-Z]+)(_.+)?")
    en_name = None
    splited = None
    result = None
    # xml 작성 코드 추가
    match = is_kor_name.match(name)
    number_part=None
    if match:
        korean_part = match.group(1)
        number_part = match.group(3)
        print('Line 125 ', korean_part)
        print('Line 126 ', number_part)
        splited = list(korean_part)
    elif is_eng_name.match(name):
        # eng_name = process(self.current_image_path, eng_name=self.input_value)
        return name
    else:
        return name

    name_chars = []
    for i, char in enumerate(splited):
        if i == 0:
            en_char = search_kor_name_in_csv(char=char, is_last=True)
        else:
            en_char = search_kor_name_in_csv(char=char, is_last=False)
        if en_char:
            name_chars.append(en_char)
        else:
            name_chars.append(char)
    print('Line 142 ', name_chars)
    en_name = ('_').join(name_chars)
    print('Line 144 ', en_name)

    if number_part:
        # print(number_part)
        # if en_name == 'nam' or en_name == 'yeo':
        #     result = en_name + '_' + str(int(number_part)).zfill(4)
        # else:
        #     result = en_name + '_' + str(int(number_part)).zfill(2)
        result = name.replace(korean_part, en_name)
    else:
        print('Line 152',en_name)
        result = en_name
    return str(result)
    # inputs = input(f'result : {en_name}. is correct? if correct enter empty\nor enter correct name with correct form : ')
    # if inputs:
    #     result = {
    #         'text': inputs
    #     }
    # elif not inputs:
    #     result = {
    #         'text': en_name
    #     }
    # return result
backgrounds = [None, 'bgm', 'noise']
def process(file_path, kor_name:str=None, eng_name:str=None):
    # kor_name = None
    print("file ", file_path)
    processs = subprocess.Popen(['ffplay', file_path])
    if not kor_name:
        kor_name = stqinput(kor_name, 'korean name')
    elif not eng_name:
        eng_name = stqinput(eng_name, "english name")
    
    # type = None
    # type = stqinput(type, "person's type or enter empty to normal")
    if not kor_name and not eng_name:
        return process(file_path)
    # background = strip_quotes(input("Enter background(1. bgm, 2. noise): "))
    # if not background:
    #     background = 'normal'
    # else:
    #     background = backgrounds[int(background)]

    name = None
    # if type:
    #     name = search_kor_name_from_db(kor_name)
    if not name and kor_name:
        name = get_kor_char_from_csv(kor_name)
        print("Line 184 ", name)
    elif eng_name:
        name = eng_name
    print("Line 187 ", name)

    file_basename = os.path.splitext(os.path.basename(file_path))[0]

    default_form = {
        'folder': {'__text__':str(os.path.dirname(file_path))},
        'filename': {'__text__':str(file_basename)},
        'filename_origin': {'__text__': str(os.path.basename(file_path))},
        # 'starttime_origin': '',
        # 'endtime_origin': '',
        'name': {'__text__': name},
        'background': {
            '__text__': ""
        }
    }
    # if background:
    #     default_form['background']['__text__'] = background
    obj = JsonToXmlConverter(json_data=default_form, root_name='annotation')
    obj.save_to_xml_file(join_folder_path(parent_path(file_path), file_basename + '.xml'))
    return name

def run(select='', folder_path=None, file_path=None, is_return:bool=False):
    while(True):
        if not select:
            print('1. folder\n2. file')
            select = str(strip_quotes(input("Enter select process : "))) or '1'
        if select == '1':
            folder_path = folder_path or strip_quotes(input('Enter folder path: '))
            extension = None
            # extension = stqinput(extension, 'target extension(txt, mp4, etc.)')
            files = get_files_path_in_folder_via_ext(folder_path, 'mp4')
            files.sort()

            for i, file_path in enumerate(files, 1):
                clear()
                print(f"{i}/{len(files)}")
                process(file_path)
            select = None
            folder_path = None
            if is_return: return

        elif select == '2':
            if not file_path:
                file_path = strip_quotes(input('Enter file path: '))
                process(file_path)
            select = None
            file_path = None
            if is_return: return
        # elif select == '3':
        #     root_folder_path = folder_path or strip_quotes(input('Enter folder path: '))
        #     folders = get_dir_sub_folder_path(root_folder_path)
        #     for i, folder_path in enumerate(folders):
        #         files = get_files_path_in_folder_via_ext(folder_path, 'mp4')
        #         files.sort()

        #         for j, file_path in enumerate(files, 1):
        #             clear()
        #             print(f"{i}/{len(folders)}")
        #             print(f"{j}/{len(files)}")
        #             if path_exist(rename(file_path, new_extension='xml')): continue
        #             process(file_path)
        #     select = None
        #     folder_path = None
        #     if is_return: return
        else:
            select = None
            continue


# class JsonToXmlConverter:
#     def __init__(self, json_data, root_name=None):
#         self.json_data = json_data
#         self.root_name = root_name

#     def convert_to_xml(self):
#         root = ET.Element(
#             self.root_name) if self.root_name else ET.Element('root')
#         self._add_children(root, self.json_data)
#         return ET.ElementTree(root)

#     def _add_children(self, parent_element, data):
#         if isinstance(data, dict):
#             for key, value in data.items():
#                 if str(key) == 'text':
#                     child = ET.Element(key)
#                     parent_element.append(child)
#                     self._add_children(child, value)
#                 else:

#                     pass
#         else:
#             # value가 dict가 아닌 경우, key를 요소로 추가하고 해당 값을 속성으로 설정
#             parent_element.set(key, str(value))

#     def save_to_xml_file(self, filename):
#         xml_tree = self.convert_to_xml()
#         xml_tree.write(filename, encoding='utf-8', xml_declaration=True)


def dict_to_json(data):
    return json.dumps(data)


# 예시 데이터
# data = {
#     "root": {
#         "child1": "Hello from child1",
#         "child2": "Hello from child2"
#     }
# }
if __name__ == "__main__":
    # run()
    print(get_kor_char_from_csv("리일환"))
