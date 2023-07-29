import os
from lxml import etree
import  re
path = r'\\172.168.5.14\CustomerPro\FBO\PBBinhDien\SP2264\App_Data\Controllers\Dir\InputInvoice - Copy.xml'
entity_pattern = re.compile(r'<!ENTITY\s+(.*?)\s+SYSTEM\s+"(.*?)"\s*>')

# Định nghĩa regex cho tìm kiếm chuỗi trong cặp dấu ngoặc kép ""
string_pattern = re.compile(r'"(.*?)"')
string_endfile = [".ent", ".xml"]
file_khong_hop_le = []
file_hop_le = []
def list_entity(text):
    matches = entity_pattern.findall(text)
    controllers_path = os.path.dirname(os.path.dirname(path))
    list_invalid, list_valid = [], []
    for entity_name, entity_value in matches:
        file = controllers_path + "\\"  + re.sub(r"\.\.\\", "", entity_value)
        if not os.path.exists(file):
            for end_char in string_endfile:
                if entity_value.endswith(end_char):
                    list_invalid.append(file)
        else:
            for end_char in string_endfile:
                if entity_value.endswith(end_char):
                    list_valid.append(file)
    return list_invalid, list_valid

def readXml(path):
    global file_khong_hop_le
    if not os.path.exists(path):
        print("Not exists path")
        return
    dir_path = os.path.dirname(os.path.dirname(os.path.dirname(path)))
    with open(path, "r", encoding="utf-8") as file:
        xml_text = file.read()
    list_invalid, list_valid = list_entity(xml_text)
    file_khong_hop_le.extend(list_invalid)
    for file in list_valid:
        print(f"Reading: {file}")

readXml(path)
print(file_khong_hop_le)
