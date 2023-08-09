import re
from Constant.constant import Constant as ct
import os

def cut_to_controllers():
    path_root = r"\\172.168.5.14\CustomerPro\FBO\PBBinhDien\SP2264\App_Data\Controllers\Dir\InputInvoice - Copy.xml"
    if not path_root.__contains__("Controllers"):
        print("Không có Folder Controllers trong đường dẫn")
        return None
    else:
        index = path_root.find("\\Controllers")
        print(path_root[:index + len("\\Controllers")])
        if os.path.exists(path_root[:index + len("\\Controllers")]):
            return path_root[:index + len("\\Controllers")]
        else:
            print("Invalid path. The 'Controllers' folder does not exist.")
            return None
xml_content = """
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE dir [
  <!ENTITY XMLSuggestion SYSTEM "..\Include\XML\Suggestion.xml">
  <!ENTITY % ScriptSuggestion SYSTEM "..\Include\Javascript\Suggestion.txt">
   %ScriptSuggestion;
 
  <!ENTITY % Media SYSTEM "..\Include\Media.ent">
  %Media;
  %AnotherEntity;
  <!ENTITY MediaController "crItem">
    
  <!ENTITY MediaSource "Media">
  <!ENTITY MediaTabIndex "5">
  <!ENTITY MediaTable "media">
  <!ENTITY MediaSysField "syskey">
  <!ENTITY MediaKeyField "ma_hh">
  <!ENTITY MediaImageField "ikey">
  
  <!ENTITY Identification "crItem">
    <!ENTITY % Extender SYSTEM "..\Include\Extender.ent">
  %Extender;
  %Extender.Include.InputInvoice;
  %Extender.Ignore;
]>
"""

# Lay trong doctype
doctype =  re.findall(r'<!DOCTYPE [^[]+\[([^\]]+)\]', xml_content)
regex_in_entity_system = re.compile(r'<!ENTITY\s+% (\w+)\s+SYSTEM "(.*?)"\s*>')

entity_declare_regex = ct.entity_declare_regex
element_doctype = ' '.join(doctype).split('">')
try:
    index = element_doctype.index("\n")
    del element_doctype[index]
except ValueError:
    pass
partition_doctype = [part.replace("\n", "").lstrip() + '">' for part in element_doctype]
mapping_entity = ()
for index, value in enumerate(partition_doctype):
    a = entity_declare_regex.findall(value)
    parent = ""
    if len(a) > 0 :
        if index != 0:
            parent = partition_doctype[index-1]
            index = parent.index("<!ENTITY")
            parent = parent[index:]
            a = [x[1:len(x)-1] for x in a]
        enity_system_arr = regex_in_entity_system.findall(parent)
        enity_system_name = enity_system_arr[0][0]
        enity_system_link = enity_system_arr[0][1]
        try:
            index = a.index(enity_system_name)
            del a[index]
        except ValueError:
            pass
        if len(a) >0:
            path = cut_to_controllers()
            print(path + "\\" + re.sub(r"\.\.\\", "", enity_system_link))
            mapping_entity += (parent, a )

print()
print(mapping_entity)

