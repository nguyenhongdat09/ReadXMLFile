from Read.ReadFile import readFile as rd
path = r'\\172.168.5.14\CustomerPro\FBO\PBBinhDien\SP2264\App_Data\Controllers\Dir\InputInvoice - Copy.xml'
reader = rd(path_root= path)
reader.readXml(path)
print(reader.file_to_df())