from tkinter import *

root = Tk()
root.title("HH GUI")
root.geometry("640x480") # 가로 * 세로

listbox = Listbox(root, selectmode="extended", height=0) #은 리스트가 포함하고 있는 크기만큼 다 보여지게 됨
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd() :
    listbox.delete(listbox.curselection()) #0은 맨 앞, END는 맨 끝, curselection()은 현재 선택된 것을
                                            # return해주므로 그 위치에 있는걸 지워줌
    # print("이 리스트에는", listbox.size(),"개가 있어요") # 개수확인
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2)) #시작 index, 끝 index를 리턴해줌
    # print("선택된 항목 : ", listbox.curselection()) #선택된 항목을 index값으로 반환
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
