import math
import os
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
from tkinter.simpledialog import *
from PIL import Image
import PIL
import numpy as np
from sympy import *


## 함수 선언부
### 공통 함수부 ###
def loadImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    filename = askopenfilename(parent=window,
            filetypes=(("칼라", "*.png;*.jpg;*.bmp;*.gif"),("모든 파일", "*.*")))
    # 파일 크기 알아내기
    pillow=Image.open(filename)
    inH = pillow.height
    inW = pillow.width
    # 메모리 확보 (영상 크기)
    inImage = [[[0 for _ in range(inW)] for _ in range(inH)] for _ in range(3)]
    # 파일 --> 메모리 로딩
    pillowRGB = pillow.convert('RGB') #RGB 모델로 변경
    for i in range(inH):
        for k in range(inW):
            r, g, b = pillowRGB.getpixel((k,i))
            inImage[0][i][k] = r
            inImage[1][i][k] = g
            inImage[2][i][k] = b
    equalImage()

def displayImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    if canvas != None:
        canvas.destroy()
    window.geometry(str(outW) + 'x' + str(outH))
    canvas = Canvas(window, height=outH, width=outW)
    paper = PhotoImage(height=outH, width=outW)
    canvas.create_image((outW / 2, outH / 2), image=paper, state='normal')
    # for i in range(outH) :
    #     for k in range(outW) :
    #         r = g = b = outImage[i][k]
    #         paper.put('#%02x%02x%02x' % (r, g, b), (k, i))
    rgbString = ""
    for i in range(outH):
        tmpString = ""
        for k in range(outW):
            r = outImage[0][i][k]
            g = outImage[1][i][k]
            b = outImage[2][i][k]
            tmpString += '#%02x%02x%02x ' % (r, g, b)
        rgbString += '{' + tmpString + '} '
    paper.put(rgbString)

    canvas.pack()

def saveImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    save_filename = asksaveasfilename(parent=window, filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), defaultextension=".png")
    if save_filename:
        new = np.array(outImage, dtype=np.uint8).transpose(1, 2, 0)
        img = Image.fromarray(new, 'RGB')
        img.save(save_filename)
        messagebox.showinfo("저장", "파일이 성공적으로 저장되었습니다.")

def quit():
    window.destroy()
    window.quit()
    exit()


## 영상 처리 함수부 ##
def equalImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)]for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for rgb in range(3) :
        for i in range(inH) :
            for k in range(inW) :
                outImage[rgb][i][k] = inImage[rgb][i][k]
    ##############################
    displayImage()

def grayImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)]for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for i in range(inH) :
        for k in range(inW) :
            hap = inImage[0][i][k] + inImage[1][i][k] +inImage[2][i][k]
            outImage[0][i][k] = outImage[1][i][k]= outImage[2][i][k]=hap//3
    ##############################
    displayImage()

def reverseImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)]for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for rgb in range(3):
        for i in range(inH) :
            for k in range(inW) :
                outImage[rgb][i][k] = 255-inImage[rgb][i][k]
    ##############################
    displayImage()

def addImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)]for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    value=askinteger("밝게할 값", f"-{255} 부터 {255}까지 입력", minvalue=-255, maxvalue=255)
    for rgb in range(3):
        for i in range(inH) :
            for k in range(inW) :
                if (inImage[rgb][i][k]+value>255):
                    outImage[rgb][i][k] = 255
                elif (inImage[rgb][i][k]+value<0):
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = inImage[rgb][i][k]+value
    ##############################
    displayImage()

def blackImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)]for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for rgb in range(3):
        for i in range(inH) :
            for k in range(inW) :
                outImage[rgb][i][k] = inImage[rgb][i][k]
                if outImage[rgb][i][k]<255/2:
                    outImage[rgb][i][k]=0
                else:
                    outImage[rgb][i][k]=255
    ##############################
    displayImage()

def gammaImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    gamma=askfloat("감마 값","")
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k]=int(np.power(inImage[rgb][i][k]/255,gamma)*255)
    displayImage()

def parabolaImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if int(255 * np.power(inImage[rgb][i][k]/127-1,2))>255 :
                    outImage[rgb][i][k] = 255
                else:
                    outImage[rgb][i][k]=int(255 * np.power(inImage[rgb][i][k]/127-1,2))
    displayImage()


### 기하학 처리
def moveImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)]for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    xVal=askinteger("x값","")
    yVal=askinteger("y값","")
    for rgb in range(3):
        for i in range(inH) :
            for k in range(inW) :
                if (0 <= i+yVal< outH) and(0 <= k+xVal < outW):
                    outImage[rgb][i+yVal][k+xVal] = inImage[rgb][i][k]
    ##############################
    displayImage()

def zoomOutImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    scale = askinteger("축소배율", "")
    outH = inH//scale
    outW = inW//scale
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)]for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for rgb in range(3):
        for i in range(outH):
            for k in range(outW):
                outImage[rgb][i][k] = inImage[rgb][i*scale][k*scale]
    ##############################
    displayImage()

def zoomInImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    scale = askinteger("확대배율", "")
    outH = inH*scale
    outW = inW*scale
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)]for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    # for i in range(inH):
    #     for k in range(inW):
    #         outImage[i*scale][k*scale] = inImage[i][k]
    for rgb in range(3):
        for i in range(outH):
            for k in range(outW):
                outImage[rgb][i][k]=inImage[rgb][i//scale][k//scale]
    ##############################
    displayImage()

def rotateImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    angle = askinteger("각도", "0~360")
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;
    outW = inW;
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    radian = -angle * math.pi / 180.0
    cx = inH // 2
    cy = inW // 2

    # for i in range(inH) :
    #     for k in range(inW) :
    #         newI = int(math.cos(radian)*(i-cx) - math.sin(radian)*(k-cy))+cx
    #         newK = int(math.sin(radian)*(i-cx) + math.cos(radian)*(k-cy))+cy
    #
    #         if( 0<=newI<outH) and (0<=newK<outW) :
    #             outImage[newI][newK] = inImage[i][k]
    for rgb in range(3):
        for i in range(outH):
            for k in range(outW):
                oldI = int(math.cos(radian) * (i - cx) + math.sin(radian) * (k - cy)) + cx
                oldK = int(-math.sin(radian) * (i - cx) + math.cos(radian) * (k - cy)) + cy

                if (0 <= oldI < inH) and (0 <= oldK < inW):
                    outImage[rgb][i][k] = inImage[rgb][oldI][oldK]
    ##############################
    displayImage()


## 전역 변수부 ##
window, canvas, paper = None, None, None
filename = ""
inImage, outImage = None, None
inH, inW, outH, outW = 0, 0, 0, 0



## 메인 코드부
window = Tk()
window.title('GrayScale Image Processing (Beta 1)')

mainMenu = Menu(window) # 메뉴의 틀
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu) # 상위 메뉴(파일)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=loadImage)
fileMenu.add_command(label='저장', command=saveImage)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=quit)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label='화소점 처리', menu=image1Menu)
image1Menu.add_command(label='동일영상', command=equalImage)
image1Menu.add_command(label='그레이스케일', command=grayImage)
image1Menu.add_command(label='반전', command=reverseImage)
image1Menu.add_command(label='밝게/어둡게', command=addImage)
image1Menu.add_command(label='흑백', command=blackImage)
image1Menu.add_command(label='감마 변환', command=gammaImage)
image1Menu.add_command(label='파라볼라 변환', command=parabolaImage)

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label='기하학 처리', menu=image2Menu)
image2Menu.add_command(label='이동', command=moveImage)
image2Menu.add_command(label='축소', command= zoomOutImage)
image2Menu.add_command(label='확대', command= zoomInImage)
image2Menu.add_command(label='회전', command= rotateImage)




window.mainloop()