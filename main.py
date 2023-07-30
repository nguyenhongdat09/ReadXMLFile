from Read.ReadFile import readFile as rd
from CopyFile.CopyFile import copyFile
import openpyxl

# path = r'\\172.168.5.14\CustomerPro\FBO\PBBinhDien\SP2264\App_Data\Controllers\Dir\InputInvoice - Copy.xml'

copy_yn = '0'
while True :
    copy_yn = input("Có cần copy từ dự án khác không (1 - Có, 0 - Không): ")
    if copy_yn in( '0', '1'):
        break
    print("Hãy nhập đúng định dạng")

path = input("Nhập đường dẫn cần check: ")
# path = r'\\172.168.5.14\CustomerPro\FBO\PBBinhDien\SP2264\App_Data\Controllers\Dir\InputInvoice - Copy.xml'
reader = rd(path_root= path)
reader.readXml(path)
df_file, df_file_khl = reader.file_to_df()
df_file_khl.to_excel('file_thieu.xlsx', index=False)

if len(reader.file_khong_hop_le) == 0:
    print("Không tìm thấy file thiếu sót")
else:
    if copy_yn == '1':
        # path_root_to_copy= r'\\172.168.5.14\CustomerPro\FBO\Fahasa\R2SP2255\App_Data\Controllers'
        path_root_to_copy = input("Nhập đường dẫn dự án cần copy (Phải bao gồm Controllers): ")
        cp = copyFile(path_root_to_copy= path_root_to_copy)
        cp.exeute_copy(reader.file_khong_hop_le)