import os
from lxml import etree
import re
import pandas as pd
import threading
from Constant.constant import Constant as ct
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)
class readFile():
    def __init__(self, path_root):
        self.path_root = path_root
        self.file_khong_hop_le = []
        self.file_hop_le = []
        self.entity_pattern = ct.entity_pattern
        self.string_pattern = ct.string_pattern
        self.string_endfile = ct.string_endfile

    def cut_to_controllers(self):
        if not self.path_root.__contains__("Controllers"):
            print("Không có Folder Controllers trong đường dẫn")
            return None
        else:
            index = self.path_root.find("\\Controllers")
            if os.path.exists(self.path_root[:index + len("\\Controllers")]):
                return self.path_root[:index + len("\\Controllers")]
            else:
                print("Invalid path. The 'Controllers' folder does not exist.")
                return None
    def list_entity(self, text):
        matches = self.entity_pattern.findall(text)
        controllers_path = self.cut_to_controllers()
        if controllers_path is None:
            return [], []
        list_invalid, list_valid = [], []
        for entity_name, entity_value in matches:
            file = controllers_path + "\\"  + re.sub(r"\.\.\\", "", entity_value)
            if not os.path.exists(file):
                list_invalid.append(file)
            else:
                for end_char in self.string_endfile:
                    if entity_value.endswith(end_char):
                        list_valid.append(file)
        return list_invalid, list_valid

    def readXml(self, path):
        if not os.path.exists(path):
            print("File không tồn tại")
            return
        if not os.path.isfile(path):
            print("Đường dẫn phải là file")
            return
        with open(path, "r", encoding="utf-8") as file:
            # print(f"Reading: {path}")
            xml_text = file.read()
        list_invalid, list_valid = self.list_entity(xml_text)
        if len(list_invalid) >= 0:
            self.file_khong_hop_le.extend(list_invalid)
        if len(list_valid) >= 0:
            self.file_hop_le.extend(list_valid)
            threads = []
            for file_path in list_valid:
                # readXml(file_path)
                thread = threading.Thread(target= self.readXml, args=(file_path,))
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()
    def file_to_df(self):
        if len(self.file_hop_le) == 0 & len(self.file_khong_hop_le) == 0:
            return pd.DataFrame(), pd.DataFrame()
        lst_stt_dong = list(range(1, max(len(self.file_khong_hop_le), len(self.file_hop_le)) + 1 ))
        if not len(self.file_khong_hop_le) == max(lst_stt_dong):
            self.file_khong_hop_le += [None] * (max(lst_stt_dong) - len(self.file_khong_hop_le))
        if not len(self.file_hop_le) == max(lst_stt_dong):
            self.file_hop_le += [None] * (max(lst_stt_dong) - len(self.file_hop_le))
        dict_file ={
            "stt": lst_stt_dong,
            "file_hop_le": [x for x in self.file_hop_le],
            "file_khong_hop_le": [x for x in self.file_khong_hop_le]
        }
        df = pd.DataFrame(dict_file)
        return df
