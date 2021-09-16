from tkinter import *

root = Tk()
root.title("HH GUI")
root.geometry("640x480") # 가로 * 세로

txt = Text(root, width=30, height=5) #여러 줄에 걸쳐서 입력을 받을 수 있음
txt.pack()
txt.insert(END, "글자를 입력하세요")

e= Entry(root, width=30) #엔터를 입력할 수 없음. 한 줄로 입력을 받음 ex. 아이디, 비밀번호
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd() :
    print(txt.get("1.0", END)) #처음부터 끝까지 있는 모든 내용을 가져옴. 1은 라인1부터 가져와라, 0은 column 기준으로 0부터 가져와라
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
