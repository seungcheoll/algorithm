# import math
# import os
# from tkinter import *
# from tkinter import messagebox
# ## 함수
# def displayImage() :
#     global window, canvas, paper, height, width, filename
#     if canvas != None :
#         canvas.destroy()
#
#     canvas = Canvas(window, height=256, width=256)
#     paper = PhotoImage(height=256, width=256)
#     canvas.create_image((256 / 2, 256 / 2), image=paper, state='normal')
#
#     for i in range(height) :
#         for k in range(width) :
#             r = g = b = image[i][k]
#             paper.put('#%02x%02x%02x' % (r, g, b), (k, i))
#
#     canvas.pack()
#
# def  reverseImage() :
#     for i in range(height):
#         for k in range(width):
#             image[i][k] = 255 - image[i][k]
#
#     displayImage()
#
# ## 변수
# window, canvas, paper = None, None, None
# filename = ""
# height, width = 0, 0
# image = []
#
# ## 메인
# window = Tk()
# window.geometry('300x300')
# window.title('영상처리 Alpha')
#
#
# btnRevese = Button(window, text ='반전', command=reverseImage )
# btnRevese.pack()
#
#
#
# filename = 'Etc_Raw(squre)/LENA256.RAW'
# # 파일 크기 알아내기
# fSize = os.path.getsize(filename) # Byte 단위
# height = width = int(math.sqrt(fSize))
# # 메모리 확보 (영상 크기)
# image = [ [0 for _ in range(width)] for _ in range(height)]
# # 파일 --> 메모리 로딩
# rfp = open(filename, 'rb')
# for i in range(height) :
#     for k in range(width) :
#         image[i][k] = ord(rfp.read(1))
#
# rfp.close()
# displayImage()
# window.mainloop()

#퀴즈 : 밝게, 어둡게, 흑백(127), 흑백(평균)
#모두 안에 넣기
import math
import os
from tkinter import *
from tkinter import messagebox
## 함수
def displayImage() :
    global window, canvas, paper, height, width, filename
    if canvas != None :
        canvas.destroy()

    canvas = Canvas(window, height=256, width=256)
    paper = PhotoImage(height=256, width=256)
    canvas.create_image((256 / 2, 256 / 2), image=paper, state='normal')

    for i in range(height) :
        for k in range(width) :
            r = g = b = image[i][k]
            paper.put('#%02x%02x%02x' % (r, g, b), (k, i))

    canvas.pack()

def  reverseImage() :
    for i in range(height):
        for k in range(width):
            image[i][k] = 255 - image[i][k]

    displayImage()

def  uplightImage() :
    for i in range(height):
       for k in range(width):
           if (image[i][k]+50>255):
               image[i][k]=255
           else :
               image[i][k]+= 50
    displayImage()

def  downImage() :
    for i in range(height):
      for k in range(width):
           if (image[i][k]-100<0):
               image[i][k]=0
           else :
               image[i][k]-= 100  #image[i][k]=image[i][k]-100
    displayImage()

def  blackImage() :
    for i in range(height):
        for k in range(width):
            if image[i][k]<127.5:
                image[i][k]=0
            else :
                image[i][k]= 255
    displayImage()

def  blackmImage() :
    hap=0
    for i in range(height):
        for k in range(width):
            hap+=image[i][k]
    avg=hap/(height*width)
    print(avg)

    for i in range(height):
        for k in range(width):
            if image[i][k]<avg:
                image[i][k]=0
            else :
                image[i][k]= 255
    displayImage()

## 변수
window, canvas, paper = None, None, None
filename = ""
height, width = 0, 0
image = []

## 메인
window = Tk()
window.geometry('300x500')
window.title('영상처리 Alpha')


btnRevese = Button(window, text ='반전', command=reverseImage )
btnRevese.pack()
btnuplight = Button(window, text ='밝게', command=uplightImage )
btnuplight.pack()
btndown = Button(window, text ='어둡게', command=downImage )
btndown.pack()
btnblack = Button(window, text ='흑백127', command=blackImage )
btnblack.pack()
btnblackm = Button(window, text ='흑백(평균)', command=blackmImage )
btnblackm.pack()

filename = 'Etc_Raw(squre)\LENA256.RAW'
# 파일 크기 알아내기
fSize = os.path.getsize(filename) # Byte 단위
height = width = int(math.sqrt(fSize))
# 메모리 확보 (영상 크기)
image = [ [0 for _ in range(width)] for _ in range(height)]
# 파일 --> 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height) :
    for k in range(width) :
        image[i][k] = ord(rfp.read(1))

rfp.close()

displayImage()


window.mainloop()

# import math
# import os
# from tkinter import *
# from tkinter import messagebox
# ## 함수
# def displayImage() :
#     global window, canvas, paper, height, width, filename
#     if canvas != None :
#         canvas.destroy()
#
#     canvas = Canvas(window, height=256, width=256)
#     paper = PhotoImage(height=256, width=256)
#     canvas.create_image((256 / 2, 256 / 2), image=paper, state='normal')
#
#     for i in range(height) :
#         for k in range(width) :
#             r = g = b = image[i][k]
#             paper.put('#%02x%02x%02x' % (r, g, b), (k, i))
#
#     canvas.pack()
#
# def  reverseImage() :
#     for i in range(height):
#         for k in range(width):
#             image[i][k] = 255 - image[i][k]
#
#     displayImage()
#
# ## 변수
# window, canvas, paper = None, None, None
# filename = ""
# height, width = 0, 0
# image = []
#
# ## 메인
# window = Tk()
# window.geometry('300x300')
# window.title('영상처리 Alpha')
#
#
# btnRevese = Button(window, text ='반전', command=reverseImage )
# btnRevese.pack()
#
#
#
# filename = 'Etc_Raw(squre)/new.RAW'
# # 파일 크기 알아내기
# fSize = os.path.getsize(filename) # Byte 단위
# height = width = int(math.sqrt(fSize))
# # 메모리 확보 (영상 크기)
# image = [ [0 for _ in range(width)] for _ in range(height)]
# # 파일 --> 메모리 로딩
# rfp = open(filename, 'rb')
# for i in range(height) :
#     for k in range(width) :
#         image[i][k] = ord(rfp.read(1))
#
# rfp.close()
#
# displayImage()
#
#
# window.mainloop()