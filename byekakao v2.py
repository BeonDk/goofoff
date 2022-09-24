import os
from xml.dom import InuseAttributeErr
import send2trash

windows_user_name = os.path.expanduser('~')
path_dir = f'{windows_user_name}\\desktop\\goofoff\\test'
file_list = os.listdir(path_dir)

from datetime import datetime 
inputDate = datetime.strptime(str(input("Searching Input Date : ")),f'%Y%m%d')
folderfile_list = []
folderfile_only = []

for (path, dir, files) in os.walk(path_dir):
    for filename in files:
        fileMtime = datetime.fromtimestamp(os.path.getmtime(path+'\\'+filename))
        # print(inputDate)
        # print(fileMtime)
        if inputDate < fileMtime:
            # print('경로 : [%s], 파일명 : [%s], 수정일자 : [%s]' %(path,filename,fileMtime))
            # print(f'{path} {filename} {fileMtime}') # 온전히 파일 이름만 입력
            # a = ({path}+{filename})
            folderfile_only.append(path+'\\'+filename)
            folderfile_list.append(f'경로 : {path}, 파일명 : {filename}, 수정일자 : {fileMtime}')
            # print(*folderfile_list, sep='\n')
            # print(*folderfile_only, sep='\n')
        # else:
        #     print(f"{inputDate}보다 일찍 생성된 파일이 없습니다.")
if len(folderfile_only) == 0:
    print(f"{inputDate}보다 일찍 생성된 파일이 없습니다.")
else:
    print(*folderfile_only, sep='\n')
    YN = input("선택된 파일들을 휴지통으로 이동시키겠습니까?")
    if YN == "Y":
        os.chdir(path_dir)
        send2trash.send2trash(folderfile_only)
    else:
        print("프로그램을 종료합니다.")
# print(*folderfile_list, sep='\n')
# print(*folderfile_only, sep='\n')
# YN = input("선택된 파일들을 휴지통으로 이동시키겠습니까?")
# if YN == "Y":
#     os.chdir(path_dir)
#     send2trash.send2trash(folderfile_only)
# else:
#     print("프로그램을 종료합니다.")


        # try:
        #     inputDate > fileMtime
        #     print('경로 : [%s], 파일명 : [%s], 수정일자 : [%s]' %(path,filename,fileMtime))
        # except:
        #     print(f"{inputDate}보다 일찍 생성된 파일이 없습니다.")


