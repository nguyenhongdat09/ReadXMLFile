import os
from lxml import etree
import  re
path = r'\\172.168.5.14\CustomerPro\FBO\PBBinhDien\SP2264\App_Data\Controllers\Dir\InputInvoice - Copy.xml'
entity_pattern = re.compile(r'<!ENTITY\s+(.*?)\s+SYSTEM\s+"(.*?)"\s*>')

# Định nghĩa regex cho tìm kiếm chuỗi trong cặp dấu ngoặc kép ""
string_pattern = re.compile(r'"(.*?)"')

def list_entity(text):
    matches = entity_pattern.findall(text)
    controllers_path = os.path.dirname(os.path.dirname(path))
    list_invalid, list_valid = [], []
    for entity_name, entity_value in matches:
        file = controllers_path + "\\"  + re.sub(r"\.\.\\", "", entity_value)
        if entity_value.endswith(".xml") & (not os.path.exists(file)):
            list_invalid.append(file)
        else:
            list_valid.append(file)
    return list_invalid, list_valid

def readXml():
    if not os.path.exists(path):
        print("Not exists path")
        return
    dir_path = os.path.dirname(os.path.dirname(os.path.dirname(path)))
    with open(path, "r", encoding="utf-8") as file:
        xml_text = file.read()
    list_invalid, list_valid = list_entity(xml_text)
    for file in list_invalid:
        print(f"File Name {file}")

readXml()
