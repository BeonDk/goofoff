import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
print(driver.current_url)


# 1. 프로그램 전환하는 방법 : Chrome 브라우저 선택하는 방법 (https://pythondocs.net/pyautogui/pywinauto-pyautogui-%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%8A%B9%EC%A0%95-%EC%9C%88%EB%8F%84%EC%9A%B0-%EC%B0%BD-%ED%99%9C%EC%84%B1%ED%99%94-%ED%83%80%EC%9D%B4%ED%8B%80%EB%AA%85-%EC%9D%B4%EC%9A%A9/)
# 2. 켜져있는 브라우저에서 현재 URL 가져오기
# 3. 가져온 URL 엑셀로 저장하기
# 4. URL 각 탭별로 가져오기
# 5. 반복문 적용해서 하나의 엑셀로 저장

urllist = []
urllist.append(driver.current_url)
print(urllist)

