import os
from datetime import datetime
from tkinter import E 


windows_user_name = os.path.expanduser('~')
path_dir = f'{windows_user_name}\\desktop\\test_folder'
file_list = os.listdir(path_dir)
file_size = os.path.getsize(path_dir)
print(file_size)
print(os.getcwd())

a = 'C:/Users/PHIL/Desktop/test_folder/KakaoTalk_20221008_200004359.mp4'
e = os.path.getmtime(a)
fileMtime = datetime.fromtimestamp(e)
# strMtime = datetime.strptime(fileMtime, f'%Y%m%d').date()
# print(fileMtime)

now = datetime.now()

b = now - fileMtime
print(b)

# 문제 해결!
if b.days >= 5:
    print("참")