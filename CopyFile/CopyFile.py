import os
import shutil
class copyFile():
    def __init__(self, path_root_to_copy):
        self.path_root_to_copy = path_root_to_copy
        self.path_project = os.path.dirname(os.getcwd()) + '\Controllers'
    def get_controllers_path(self):
        if self.path_root_to_copy.find(r'\Controllers') > 0:
            return self.path_root_to_copy[: self.path_root_to_copy.find(r'\Controllers') + len(r'\Controllers')]
        else:
            return None
    def copy_file(self, path_file_copy):
        # Create file and not make error if folder exists
        os.makedirs(self.path_project, exist_ok=True)
        if not os.path.isfile(path_file_copy):
            return
        folder_copy = os.path.dirname(path_file_copy)
        index_folder = os.path.dirname(path_file_copy).find(r'\Controllers')
        path_file_to_find = folder_copy[index_folder + len(r'\Controllers'):]
        destination_folder =self.path_project + path_file_to_find
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        print("Copy: " , path_file_copy)
        print("Paster: " ,destination_folder)
        shutil.copy(path_file_copy, destination_folder)
    def exeute_copy(self, arr_path):
        if len(arr_path) <= 0:
            return
        path_controller_copy = self.get_controllers_path()
        if path_controller_copy is None:
            return
        for path in arr_path:
            index_controllers_index = path.find(r'\Controllers')
            if index_controllers_index <= 0:
                return
            path_file_to_find = path[index_controllers_index+ len(r'\Controllers') +1 :]
            path_file_copy = path_controller_copy + '\\' + path_file_to_find
            self.copy_file(path_file_copy)

# path_to_find = [r'\\172.168.5.14\CustomerPro\FBO\PBBinhDien\SP2264\App_Data\Controllers\Include\XML\APVPOXMLViews_test.txt']
# cp = copyFile(path_root_to_copy= r'\\172.168.5.14\CustomerPro\FBO\Fahasa\R2SP2255\App_Data\Controllers')
# cp.exeute_copy(path_to_find)

# print(cp.get_controllers_path())