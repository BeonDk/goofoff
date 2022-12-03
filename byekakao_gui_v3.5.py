# To-to list
# 1. 파일 삭제 후 몇개의 파일 삭제, 얼마 파일 삭제했다는 메세지 박스
# 2. 파일 삭제 후 Listfram refresh해서 다시 남은 파일 얼마나 되었는지
# 3. 루피 얼굴 적용

import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * # __all__
from tkinter import filedialog
from datetime import datetime, timedelta
# from webbrowser import get
import send2trash

# To-do list
# 1. del_file 함수 적용될 때 삭제가 아니라 send2trash로 가는 옵션도 만들 것 (tkinter의 선택지 고르른 것에 적용하는 것 검토)

windows_user_name = os.path.expanduser('~')
# path_dir = f'{windows_user_name}\\desktop\\test_folder'
list_deleted = []
list_deleted_full = []

root = Tk()
root.title("Byekakao")

# 파일 추가
# def add_file():
#     files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
#         initialdir=r"C:\Users\PHIL\Desktop\goofoff") # 최초 폴더 지정

# # 사용자가 선택한 파일출력
# #   # 선택된 값을 list에 받아오는 방식 / class는 list
# #     a = []
# #     for file in files:
# #         a.append(file)
# #         print(type(a))
# #         # print(*a, sep='\n')
# #   # tkinter 모듈에서 처리 / class는 tkinter.listbox
#     for file in files:
#         list_file.insert(END, file)
#         print(type(list_file))
#         b = list_file.get(0, END)
#     print(*b, sep='\n')

## 221010_to-do_삭제된 파일리스트까지는 완성되었고 전체 파일 경로를 넣어서 나중에 os를 활용하여 실제로 지울 파일들 목록을 따오는 것 준비
### 221012_done_listbox를 get으로 받아오는 함수가 tuple 형식이었는데 list로 바꿔주는 list(list_deleted)를 사용해서 해결

# 삭제하고자 하는 날짜 프레임
## 221012_to-do_> file_list를 파일 명만 불러 오는 것이 아니라 경로까지 같이 넣을 수 있는 방법
### 221012_done_for문으로 처리함
windows_user_name = os.path.expanduser('~')
path_dir = f'{windows_user_name}\\AppData\\Local\\Kakao\\KakaoTalk\\users'
# file_size = os.path.getsize(path_dir)
# file_list = os.listdir(path_dir)


original_filelist = []

for (path, dir, files) in os.walk(path_dir):
        for file in files:
            file_path = os.path.join(path, file)
            original_filelist.append(file_path)

# 파일사이즈 convert
# def convert_size(size_bytes):
#     import math
#     if size_bytes == 0:
#         return "0B"
#     size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
#     i = int(math.floor(math.log(size_bytes, 1024)))
#     p = math.pow(1024, i)
#     s = round(size_bytes / p, 2)
#     return "%s %s" % (s, size_name[i])

def error():
    msgbox.showerror("에러", '잘못된 날짜를 입력하였습니다. 입력형식 : "YYYYMMDD" 으로 다시 입력해주세요.')

def yesorno():
    yesorno = msgbox.askokcancel("확인", "선택하신 날짜 이전의 파일이 모두 삭제됩니다. 정말 삭제하시겠습니까?")
    
    if yesorno == 1:
        # list_deleted = list_file.get(0, END)
        # list(list_deleted)
        # list(path_dir)
        # for A in list_deleted:
        #     list_deleted_full.append(path_dir+'\\'+A)
        
        # list_deleted_full의 getmtime을 inputDate와 비교해서 크기 설정
        # print(list_deleted_full)

        # 아래 잠시 pause
        # # # 정의해야 할 것은 입력받은 숫자 (예를 들어 90일...이면 현재 날짜 - 90일이 되어야 함)
        int_input_date = datetime.strptime(input_date.get() ,f'%Y%m%d')
        comparedfile = []
        for filename in original_filelist:
            fileMtime = datetime.fromtimestamp(os.path.getmtime(filename))
            # print(int_input_date)
            # print(fileMtime)
            # folderfile_list = []
            
            if int_input_date > fileMtime:
                # print('경로 : [%s], 파일명 : [%s], 수정일자 : [%s]' %(path,filename,fileMtime))
                # print(f'{path} {filename} {fileMtime}') # 온전히 파일 이름만 입력
                # a = ({path}+{filename})
                comparedfile.append(filename)
                # folderfile_list.append(f'경로, 파일명 : {filename}, 수정일자 : {fileMtime}')
                # print(*folderfile_list, sep='\n')
                # print(*comparedfile, sep='\n')
            # else:
            #     print(f"{int_input_date}보다 일찍 생성된 파일이 없습니다.")
        
        # 프로그레스 바 연동하려면 = 총 삭제해야하는 파일들의 진척률
        # for idx, img in enumerate(images):
        #     result_img.paste(img, (0, y_offset)) 
        #     y_offset += img.size[1] # 높이 값 만큼 더해줌       

        #     progress = (idx + 1) / len(images) *100 # 실제 percent 정보를 계산 / index 0 부터 시작
        #     p_var.set(progress)
        #     progress_bar.update()
        

        if len(comparedfile) == 0:
            msgbox.showinfo("오류", "입력한 날짜보다 일찍 생성된 파일이 없습니다.")
            # print(f"입력한 날짜보다 일찍 생성된 파일이 없습니다.")
        else:
            # print(*comparedfile, sep='\n')
            os.chdir(path_dir)
            # totalsize = 0
            # for i in comparedfile:
                
            #     file_size = os.path.getsize(i)
            #     totalsize += file_size + totalsize
            # converted_size = convert_size(totalsize)

            send2trash.send2trash(comparedfile)
            msgbox.showinfo("완료", '선택한 파일이 모두 휴지통으로 이동되었습니다. 복구하고 싶으면 휴지통에서 복구 하세요.')
            # print("선택한 파일이 모두 휴지통으로 이동되었습니다. 복구하고 싶으면 휴지통에서 복구 하세요.")
    # else:
    #     print("프로그램을 완전히 종료합니다.")


def delete_seleted():
    # folder_selected = filedialog.askdirectory()
    # if folder_selected == "": # 사용자가 취소를 누를 때
    #     return
    try:
        int_input_date = datetime.strptime(input_date.get() ,f'%Y%m%d')
        yesorno()

    except:
        error()
    
    today = datetime.today()
    
    
    # targetdate = today - timedelta(days=int_input_date)
    # print(today)
    # print(type(today))
    # print(targetdate)
    # print(type(targetdate))

### 아래가 원래 구간
    
    # list_deleted = list_file.get(0, END)
    # list(list_deleted)
    # list(path_dir)
    # for A in list_deleted:
    #     list_deleted_full.append(path_dir+'\\'+A)
    # folderfile_list = []
    # comparedfile = []
    # # list_deleted_full의 getmtime을 inputDate와 비교해서 크기 설정
    # # print(list_deleted_full)

    # # 아래 잠시 pause
    # # # # 정의해야 할 것은 입력받은 숫자 (예를 들어 90일...이면 현재 날짜 - 90일이 되어야 함)
    
    # for filename in list_deleted_full:
    #     fileMtime = datetime.fromtimestamp(os.path.getmtime(filename))
    #     # print(int_input_date)
    #     # print(fileMtime)
        
    #     if int_input_date > fileMtime:
    #         # print('경로 : [%s], 파일명 : [%s], 수정일자 : [%s]' %(path,filename,fileMtime))
    #         # print(f'{path} {filename} {fileMtime}') # 온전히 파일 이름만 입력
    #         # a = ({path}+{filename})
    #         comparedfile.append(filename)
    #         folderfile_list.append(f'경로, 파일명 : {filename}, 수정일자 : {fileMtime}')
    #         # print(*folderfile_list, sep='\n')
    #         # print(*comparedfile, sep='\n')
    #     # else:
    #     #     print(f"{int_input_date}보다 일찍 생성된 파일이 없습니다.")
    # if len(comparedfile) == 0:
    #     print(f"입력한 날짜보다 일찍 생성된 파일이 없습니다.")
    # else:
    #     print(*comparedfile, sep='\n')
    #     while True:
    #         YN = input("선택된 파일들을 휴지통으로 이동시키겠습니까? (Y/N)")
    #         YN = YN.upper() # y/n 대소문자 아무거나 넣었을 때 일정한 값으로 입력시키기 위한 구문
            
    #         if YN == "Y" :
    #             os.chdir(path_dir)
    #             send2trash.send2trash(comparedfile)
    #             print("선택한 파일이 모두 휴지통으로 이동되었습니다. 복구하고 싶으면 휴지통에서 복구 하세요.")
    #             break
    #         elif YN == "N" :
    #             print("프로그램을 종료합니다.")
    #             break
    #         else:
    #             print("잘못된 값을 입력하였습니다. 다시 입력하여주세요.")
    
### 여기까지 원래 구간    

    # for gettime in range(len(list_deleted_full)):
    #     for xxx in range(len(list_deleted_full)):
    #         for yyy in list_deleted_full:
    #             # print(*list_deleted_full, sep='\n')
    #             fileMtime = datetime.fromtimestamp(os.path.getmtime(yyy))
    #             # print(gettime)
    #             # print(fileMtime)
    #             if (today - fileMtime) >= timedelta(days=int_input_date):
    #                 # print('경로 : [%s], 파일명 : [%s], 수정일자 : [%s]' %(path,filename,fileMtime))
    #                 # print(f'{path} {filename} {fileMtime}') # 온전히 파일 이름만 입력
    #                 # a = ({path}+{filename})
    #                 comparedfile.append(yyy)
    #                 # comparedfile.append(path_dir +'\\'+ yyy)
    #                 # folderfile_list.append(f'경로 : {path}, 파일명 : {filename}, 수정일자 : {fileMtime}')
    #                 # print(*folderfile_list, sep='\n')
    #             else:
    #                 print("일찍 생성된 파일이 없습니다.")
    #                 # print(f"{targetdate}보다 일찍 생성된 파일이 없습니다.")
    #     print(*comparedfile, sep='\n')

    # for gettime in range(len(list_deleted_full)):
    #     for xxx in list_deleted_full:
    #         fileMtime = datetime.fromtimestamp(os.path.getmtime(xxx))
    #         # print(gettime)
    #     # print(fileMtime)
    #         if targetdate < fileMtime:
    #             # print('경로 : [%s], 파일명 : [%s], 수정일자 : [%s]' %(path,filename,fileMtime))
    #             # print(f'{path} {filename} {fileMtime}') # 온전히 파일 이름만 입력
    #             # a = ({path}+{filename})
    #             comparedfile.append(path_dir +'\\'+ xxx)
    #             # folderfile_list.append(f'경로 : {path}, 파일명 : {filename}, 수정일자 : {fileMtime}')
    #             # print(*folderfile_list, sep='\n')
    #             print(*comparedfile, sep='\n')
    #         else:
    #             print(f"{targetdate}보다 일찍 생성된 파일이 없습니다.")

# # 여기까지_221101_done : 일단 파일 리스트에서 필요한 파일 받아오는 것까지는 완성된 것 같음. 앞으로 할 내용은 Y/N control 박스 받아서 실제 살제하는 코드 추가할 것.
    # if len(comparedfile) == 0:
    #     print(f"{targetdate}보다 일찍 생성된 파일이 없습니다.")
    # else:
    #     print(*comparedfile, sep='\n')
    #     while True:
    #         YN = input("선택된 파일들을 휴지통으로 이동시키겠습니까? (Y/N)")
    #         YN = YN.upper() # y/n 대소문자 아무거나 넣었을 때 일정한 값으로 입력시키기 위한 구문
            
    #         if YN == "Y" :
    #             os.chdir(path_dir)
    #             send2trash.send2trash(comparedfile)
    #             print("선택한 파일이 모두 휴지통으로 이동되었습니다. 복구하고 싶으면 휴지통에서 복구 하세요.")
    #             break
    #         elif YN == "N" :
    #             print("프로그램을 종료합니다.")
    #             break
    #         else:
    #             print("잘못된 값을 입력하였습니다. 다시 입력하여주세요.")

    # 아래는 타입 테스트용 프린트
    # print(type(targetdate))
    # V = str(value_txt_dest_path)
    # print(V)
    # print(type(V))

    # print(txt_dest_path.get())
    # txt_dest_path.delete(0,END)
    # txt_dest_path.insert(0, folder_selected)
    

# 정한 폴더 파일 사이즈 구하기
# windows_user_name = os.path.expanduser('~')
# path_dir = f'{windows_user_name}\\desktop\\test_folder'
# file_list = os.listdir(path_dir)
# file_size = os.path.getsize(path_dir)


# 파일 프레임 (파일 추가, 선택 삭제)
# file_frame = Frame(root)
# file_frame.pack(fill="x", padx=5, pady=5) # 간격 띄우기

# btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
# btn_add_file.pack(side="left")
# file_frame.insert(0, f'{file_size}kb의 용량이 사용되고 있습니다.')

# main_label = Label(file_frame, text=f'{file_size}kb의 용량이 사용되고 있습니다.')
# main_label.pack(side="left", padx=5, pady=5)

# 리스트 프레임
# list_frame = Frame(root)
# list_frame.pack(fill="both", padx=5, pady=5)

# scrollbar = Scrollbar(list_frame)
# scrollbar.pack(side="right", fill="y")

# list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)

### to-do_done. list_file 자체에 default 값으로 카카오톡 폴더의 총 파일 사이즈를 가지고 와야함 > 카카오톡 지울 폴더의 총 파일 사이즈 함수 정의

# tip. 해당 내용은 별도의 현재 상태표시 프레임으로 넣을 것 list_file.insert(0, f'{file_size}kb의 용량이 사용되고 있습니다.')
# tip. 아래는 지정된 리스트 프레임에 파일 리스트(path_dir = user\\desktop\\test_foler)를 하나씩 넣어주는 것
# for i in range(len(file_list)):
#     list_file.insert(END, file_list[i])

# list_file.pack(side="left", fill="both", expand=True)
# scrollbar.config(command=list_file.yview)


# 삭제 원하는 날짜 입력 프레임
### to-do 1. Button command 변경이 필요함 > 찾아보기에서 파일 검색 후 목록으로 보여주는 함수로 변경 (delete_seleted)
### to-do 2. Entry에 입력되는 값 받아와야 함
delete_date = LabelFrame(root, text="삭제하고자 하는 날짜를 입력/선택해주세요. 형식 : YYYYMMDD")
delete_date.pack(fill="x", padx=5, pady=5, ipady=5)

input_date = Entry(delete_date)
input_date.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경
# get 값을 통해서 entry에 들어가있는 value를 value_txt_dest_path로 돌려줌
# print(type(value_txt_dest_path))
# V = float(value_txt_dest_path)
# value_int = int(value_txt_dest_path)
# print(type(value_int))

## 221013_to-do_검색 버튼 눌렀을 때 더 날짜 숫자만큼 더 적은 파일리스트만 남기고 출력하는 명령
## 221018_to-do_value_txt로 받은 값을 int값으로 정하고 (현재 날짜 - 기존 파일리스트 날짜 >= 받은 날짜 값)의 if문으로 진행할 것
findfile = Button(delete_date, text="삭제", width=10, command=delete_seleted)
findfile.pack(side="right", padx=5, pady=5)



# 진행 상황 Progress Bar
# frame_progress = LabelFrame(root, text="진행상황")
# frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

# p_var = DoubleVar()
# progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
# progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
# frame_run = Frame(root)
# frame_run.pack(fill="x", padx=5, pady=5)

# btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
# btn_close.pack(side="right", padx=5, pady=5)


root.resizable(False, False)
root.mainloop()