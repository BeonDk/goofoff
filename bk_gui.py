from tkinter import *

root = Tk()
root.title("Welcome back my space")
root.geometry("640x480+320+240") # 가로, 세로, x좌표, y 좌표
# root.attributes('-fullscreen', True)
root.resizable(False, False)

btn1 = Button(root, text = "버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2") # pad는 입력된 내용을 대비하여 공간을 확보하는 개념
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼2")
btn3.pack()

btn4 = Button(root, width=10, height=5, text="버튼2") # width, height는 고정크기
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")

photo = PhotoImage(file="pepe.png")
btn6 = Button(root, width=100, height=50, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요.")

btn7 = Button(root, text="동작하는 버튼", command = btncmd)
btn7.pack()

root.mainloop()


root.mainloop()