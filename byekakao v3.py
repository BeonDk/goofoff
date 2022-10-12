# 남은 과제
# GUI 만들기 : 별도 파일로 작업 중
# inputdate에 입력 잘못했을 때 다시 입력하게 하는 것 while문으로 구분 : v3에서 얼추 완료
# inputdate를 날짜로 말고 일정 숫자를 넣으면 경과 날짜로 변환시키기



import os
from xml.dom import InuseAttributeErr
import send2trash

windows_user_name = os.path.expanduser('~')
path_dir = f'{windows_user_name}\\desktop\\test_folder'
file_size = os.path.getsize(path_dir)
file_list = os.listdir(path_dir)

from datetime import datetime 
inputDate = datetime.strptime(str(input("날짜를 입력해 주세요. 입력한 날짜 이전의 파일을 검색하여 삭제하게 됩니다. (입력형식 : YYYYMMDD) : ")),f'%Y%m%d')
folderfile_list = []
folderfile_only = []
print(type(folderfile_list))
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
            print(*folderfile_list, sep='\n')
            # print(*folderfile_only, sep='\n')
        # else:
        #     print(f"{inputDate}보다 일찍 생성된 파일이 없습니다.")
if len(folderfile_only) == 0:
    print(f"{inputDate}보다 일찍 생성된 파일이 없습니다.")
else:
    print(*folderfile_only, sep='\n')
    while True:
        YN = input("선택된 파일들을 휴지통으로 이동시키겠습니까? (Y/N)")
        YN = YN.upper() # y/n 대소문자 아무거나 넣었을 때 일정한 값으로 입력시키기 위한 구문
        
        if YN == "Y" :
            os.chdir(path_dir)
            send2trash.send2trash(folderfile_only)
            print("선택한 파일이 모두 휴지통으로 이동되었습니다. 복구하고 싶으면 휴지통에서 복구 하세요.")
            break
        elif YN == "N" :
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 값을 입력하였습니다. 다시 입력하여주세요.")
