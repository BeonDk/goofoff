# 인터넷에서 마우스 클릭 조작을 통해서 진행함

# 1. 현재 URL 가져오기
# 2. 가져온 URL 엑셀로 저장하기
# 3. URL 각 탭별로 가져오기
# 4. 반복문 적용해서 하나의 엑셀로 저장


import pyautogui
from tkinter import Tk
from time import sleep

SLEEP_TIME = 0.5
MAX_DUPLICATE_COUNT = 5
links = []
filename = "Trial01.txt"

def readURLs():
    pyautogui.hotkey('win', '7')      # Open Google Chrome #7은 일곱번째
    sleep(SLEEP_TIME)
    # pyautogui.position()              # To read current mouse position
    # pyautogui.moveTo(298, 69)
    pyautogui.hotkey('ctrl', '1')     # Open 1st Tab
    duplicate_count = 0
    while duplicate_count < MAX_DUPLICATE_COUNT:
        pyautogui.click(x=1000, y=70, button='left')      # Click on URL Bar
        sleep(SLEEP_TIME)
        pyautogui.hotkey('ctrl', 'a')                 # Select complete URL
        sleep(SLEEP_TIME)
        pyautogui.hotkey('ctrl', 'c')                 # Copy URL
        sleep(SLEEP_TIME)
        link = Tk().clipboard_get()                      # Read from Clipboard
        if len(links) > 0 and link in links:            # Check if the URL has already been saved
            duplicate_count += 1
            # print('Duplicate ' + str(duplicate_count) + ' found: ' + link)
        else:
            links.append(link)                      # Else append the URL to list
        print(link)
        sleep(SLEEP_TIME)
        pyautogui.hotkey('ctrl', 'tab')                   # Switch to next tab
        sleep(SLEEP_TIME)

def saveToFile():
    file = open(filename, 'w')
    file.write('\n'.join(links(file.close())))

readURLs()
saveToFile()
pyautogui.hotkey('win', 'd') 