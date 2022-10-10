import os

windows_user_name = os.path.expanduser('~')
path_dir = f'{windows_user_name}\\desktop\\test_folder'
file_list = os.listdir(path_dir)
file_size = os.path.getsize(path_dir)

print(file_size)
print(os.getcwd())
# aaaaa
#fdsafdsa