from tkinter import *
from tkinter import messagebox

def clickButton() :
    messagebox.showinfo('제목','나 불렀어?')

window=Tk()
window.geometry('300x300') #TK 크기 지정
window.title('요기가 제목')
label1=Label(window,text='나 글자다',font=('궁서체',20))
button1=Button(window,text='나를 클릭해줘',command=clickButton) #command에서는 ()를 빼주기


label1.pack()
button1.pack()
window.mainloop()