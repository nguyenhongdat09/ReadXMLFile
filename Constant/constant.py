import re
class Constant():
    entity_pattern = re.compile(r'<!ENTITY\s+(.*?)\s+SYSTEM\s+"(.*?)"\s*>')
    # Định nghĩa regex cho tìm kiếm chuỗi trong cặp dấu ngoặc kép ""
    string_pattern = re.compile(r'"(.*?)"')
    string_endfile = [".ent", ".xml"]
