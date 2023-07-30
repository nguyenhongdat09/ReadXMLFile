import os

def cut_to_controllers(path):
    if not path.__contains__("Controllers"):
        print("Kohng co conm")
        return None
    else:
        index = path.find("\\Controllers")
        if os.path.exists(path[:index + len("\\Controllers")]):
            return path[:index + len("\\Controllers")]
        else:
            print("Invalid path. The 'Controllers' folder does not exist.")
            return None

# Lấy đường dẫn từ người dùng (ví dụ)
user_input_path = input("Nhập đường dẫn: ")

# Gọi hàm để cắt đường dẫn tới thư mục "Controllers"
result_path = cut_to_controllers(user_input_path)

print("Đã cắt đến thư mục 'Controllers':", result_path)