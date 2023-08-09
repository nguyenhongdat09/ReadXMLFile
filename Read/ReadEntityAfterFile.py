import re
from Constant.constant import Constant as ct
import os
path_root = r"\\172.168.5.14\CustomerPro\FBO\PBBinhDien\SP2264\App_Data\Controllers\Dir\InputInvoice - Copy.xml"
class ReadEntityAfterFile:
    def __init__(self):
        self.path_root = path_root
        self.xml_content =  ""
        self.regex_in_entity_system = re.compile(r'<!ENTITY\s+% (\S+)\s+SYSTEM "(.*?)"\s*>')
        self.entity_declare_regex = ct.entity_declare_regex
    def readXML(self):
        if not os.path.exists(self.path_root):
            return ''
        else:
            with open(path_root, 'r', encoding="utf-8") as f:
                return f.read()

    def cut_to_controllers(seft):
        if not seft.path_root.__contains__("Controllers"):
            print("Không có Folder Controllers trong đường dẫn")
            return None
        else:
            index = seft.path_root.find("\\Controllers")
            if os.path.exists(seft.path_root[:index + len("\\Controllers")]):
                return seft.path_root[:index + len("\\Controllers")]
            else:
                print("Invalid path. The 'Controllers' folder does not exist.")
                return None
    def getArrDoctype(self):
        xml_content = self.readXML()
        doctype =  re.findall(r'<!DOCTYPE [^[]+\[([^\]]+)\]', xml_content)
        element_doctype = ' '.join(doctype).split('">')
        try:
            index = element_doctype.index("\n")
            del element_doctype[index]
        except ValueError:
            pass
        return [part.replace("\n", "").lstrip() + '">' for part in element_doctype]
    def getEntity(self, partition_doctype):
        mapping_entity = ()
        for index, value in enumerate(partition_doctype):
            a = self.entity_declare_regex.findall(value)
            parent = ""
            if len(a) > 0 :
                if index != 0:
                    parent = partition_doctype[index-1]
                    index = parent.index("<!ENTITY")
                    parent = parent[index:]
                    a = [x[1:len(x)-1] for x in a]
                match = self.regex_in_entity_system.search(parent)
                enity_system_name = match.group(1)
                enity_system_link = match.group(2)
                try:
                    index = a.index(enity_system_name)
                    del a[index]
                except ValueError:
                    pass
                if len(a) >0:
                    path = self.cut_to_controllers()
                    mapping_entity += (parent, a, path)
        print(mapping_entity)
read = ReadEntityAfterFile()
partition_doctype = read.getArrDoctype()
read.getEntity(partition_doctype)

