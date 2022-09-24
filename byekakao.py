# 1. 절대 주소로 폴더에 접근하는 방법
# 2. 사용자의 input 받아서 일정한 시간 경과된 파일 선택
# 3. 파일 삭제 > 휴지통으로 이동하는 옵션으로 (다시 살릴 수 있게)
# 4. GUI 적용 > 개구리 Pepe gif

from calendar import month
import os
import send2trash
# path = os.path.dirname(os.path.abspath(__file__)) # python  작업하는 절대경로 구하기

# ===================== 절대 경로 구하기 ======================= #
windows_user_name = os.path.expanduser('~')
# print("{0}\\desktop\\goofoff\\test".format(windows_user_name))
# path_dir = ("{0}\\desktop\\goofoff\\test".format(windows_user_name))
path_dir = f'{windows_user_name}\\desktop\\goofoff\\test'
file_list = os.listdir(path_dir)
os.chdir(path_dir)
# ===================== 절대 경로 구하기 ======================= #


# 여기에 Try 구분을 써서 지울 파일이 없는 경우 오류 표시를 해야함
# send2trash.send2trash(file_list) # FileNotFoundError: [Errno 2] 지정된 파일을 찾을 수 없습니다. 이런 오류는 해당 폴더로 이동하지 않아서 생기는 문제임. 18열에 chdir로 해당 폴더로 이동해줬음.


# datetime.datetime.now() # 첫번째 모듈, 두번째 클래스, 세번째 메소드/함수
# ftime = datetime.fromtimestamp(os.path.getmtime(path_dir)).strftime('%Y-%m-%d %H:%M:%S')
# print(str(ftime))

# 해당 폴더 파일 출력문
# 공부 1: for 문에서 여러가지 변수를 튜플 ()안에 넣는 것? > 은 아니고 해당 형식이 저렇게 구성되어 있음 : for의 다수 변수와 in 이하의 변수의 숫자가 매칭되어야 함
# 공부 2: os.walk 기능
# 공부 3: os.path.join 기능
# 공부 4: 파일 날짜는 어떻게 따오지? 07/09
# 공부 5: 함수 밖에서 리스트를 추가로 구성할 수 있는 방법 알안내야 함 / def 함수가 힌트 https://blockdmask.tistory.com/440 07/07
# 공부 6: 조건문 날짜 비교하기 https://jsikim1.tistory.com/144
# 공부 7: 현재 리스트 내 입력받은 날짜보다 오래 경과된 값만 다시 리스트에 저장

# ==================== folder 내 리스트 뽑는 파트, pathlib 패키지도 있음 =========================
from datetime import *
import os
import pathlib
import datetime

folderfile_list = []
# user = int(input("원하는 날짜를 입력하세요 :"))
# now = datetime.datetime.now()
# now_after = now + datetime.timedelta(days = - user)

# https://wikidocs.net/14786


# for (root, directories, files) in os.walk(path_dir): # os.walk는 (경로, 경로 내 디렉토리 리스트, 경로 내 파일 리스트)의 3가지 값을 받아오기 때문에 앞에 root, directories, files 변수에 집어넣음
#     for d in directories:
#         d_path = os.path.join(root, d) # root, d(경로 내 디렉토리 리스트)을 조합해서 아래에서 프린트함

#     for file in files: # 파일리스트 나옴
#         file_path = os.path.join(root, file)
#         folderfile_list.append(file_path)

# datetime.datetime.fromtimestamp(os.path.getctime(folderfile_list)).strftime('%Y-%m-%d %H:%M:%S') # 타입에 대한 문제가 발생 https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=youndok&logNo=222022211206
# print(*folderfile_list, sep='\n')



# ctime = os.path.getctime(folderfile_list)
# print(ctime)


# ==================== folder 내 리스트 뽑는 파트, pathlib 패키지도 있음 =========================

# =================== pathlib 패키지 사용 ======================
for (root, directories, files) in os.walk(path_dir): # os.walk는 (경로, 경로 내 디렉토리 리스트, 경로 내 파일 리스트)의 3가지 값을 받아오기 때문에 앞에 root, directories, files 변수에 집어넣음
    for name in files:
        f = pathlib.Path(root, name)
        creation_time = datetime.datetime.fromtimestamp(f.stat().st_mtime)
        fileAndTime = pathlib.PurePath(root, name),creation_time.year, creation_time.month, creation_time.day, creation_time.hour
        timeonly = creation_time.year, creation_time.month, creation_time.day, creation_time.hour
        # print(pathlib.PurePath(root, name),creation_time.year, creation_time.month, creation_time.day, creation_time.hour)
        folderfile_list.append(fileAndTime)

print(*folderfile_list, sep='\n')


# 날짜 기준 파일 검색 참조 : https://pydole.tistory.com/entry/Python-%ED%8C%8C%EC%9D%BC%EA%B2%80%EC%83%89-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-%EB%B3%80%EA%B2%BD-%EB%82%A0%EC%A7%9C%EA%B8%B0%EC%A4%80-%ED%8C%8C%EC%9D%BC-%EA%B2%80%EC%83%89

# =================== 아래는 pathlib 패키지 사용 ======================

# print(type(folderfile_list))

# ==================== folder 내 리스트 뽑는 파트 =========================
# 공백
# ==================== folder 내 리스트를 원하는 일자에 맞춰서 뽑는 파트 ===============



# ==================== folder 내 리스트를 원하는 일자에 맞춰서 뽑는 파트 ===============

# a = os.path.getmtime(folderfile_list)
# print(a)
