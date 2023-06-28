import math
import os
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
from tkinter.simpledialog import *



## 함수 선언부
### 공통 함수부 ###
def loadImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    filename = askopenfilename(parent=window,
            filetypes=(("RAW파일", "*.raw"),("모든 파일", "*.*")))
    # 파일 크기 알아내기
    fSize = os.path.getsize(filename)  # Byte 단위
    inH = inW = int(math.sqrt(fSize))
    # 메모리 확보 (영상 크기)
    inImage = [[0 for _ in range(inW)] for _ in range(inH)]
    # 파일 --> 메모리 로딩
    rfp = open(filename, 'rb')
    for i in range(inH):
        for k in range(inW):
            inImage[i][k] = ord(rfp.read(1))

    rfp.close()
    equalImage()

def displayImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    if canvas != None:
        canvas.destroy()
    window.geometry(str(outH) + 'x' + str(outW))
    canvas = Canvas(window, height=outH, width=outW)
    paper = PhotoImage(height=outH, width=outW)
    canvas.create_image((outH / 2, outW / 2), image=paper, state='normal')
    # for i in range(outH) :
    #     for k in range(outW) :
    #         r = g = b = outImage[i][k]
    #         paper.put('#%02x%02x%02x' % (r, g, b), (k, i))
    rgbString = ""
    for i in range(outH):
        tmpString = ""
        for k in range(outW):
            r = g = b = outImage[i][k]
            tmpString += '#%02x%02x%02x ' % (r, g, b)
        rgbString += '{' + tmpString + '} '
    paper.put(rgbString)

    canvas.pack()

def saveImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    saveFp=asksaveasfile(parent=window,mode='wb',defaultextension='*.raw',filetypes=(("RAW파일", "*.raw"),("모든 파일", "*.*"))) #바이너리 파일
    import struct
    for i in range(outH):
        for k in range(outW):
            saveFp.write(struct.pack('B',outImage[i][k]))
    saveFp.close()
    messagebox.showinfo('성공',saveFp.name + '으로 저장')



## 영상 처리 함수부 ##
def equalImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = inImage[i][k]
    ##############################
    displayImage()

def reverseImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = 255-inImage[i][k]
    ##############################
    displayImage()

def addImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## ** 찐 영상처리 알고리즘 ** ##
    value=askinteger("밝게할 값", f"-{inH-1} 부터 {inW-1}까지 입력", minvalue=-(inH-1), maxvalue=(inH-1))
    for i in range(inH) :
        for k in range(inW) :
            if (inImage[i][k]+value>255):
                outImage[i][k] = 255
            elif (inImage[i][k]+value<0):
                outImage[i][k] = 0
            else:
                outImage[i][k] = inImage[i][k]+value
    ##############################
    displayImage()

def blackImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = inImage[i][k]
            if outImage[i][k]<255/2:
                outImage[i][k]=0
            else:
                outImage[i][k]=255
    ##############################
    displayImage()

def blackmeanImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    hap=0
    for i in range(inH):
        for k in range(inW):
            hap+=inImage[i][k]
    avg=hap/(inH*inW)
    print(avg)
    for i in range(outH):
        for k in range(outW):
            if inImage[i][k]<avg:
                outImage[i][k]=0
            else :
                outImage[i][k]= 255
    displayImage()

def blackmedImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    hap = 0
    image1 = []
    for i in range(inH):
        for k in range(inW):
            a = inImage[i]
            b = a[k]
            image1.append(b)
    def quick_sort(image1):
        if len(image1) <= 1:
            return image1
        pivot = image1[len(image1) // 2]
        less, more, equal = [], [], []
        for each in image1:
            if each < pivot:
                less.append(each)
            elif each > pivot:
                more.append(each)
            else:
                equal.append(each)
        return quick_sort(less) + equal + quick_sort(more)
    # 중앙값 구하기
    rcm = (inH * inW) // 2
    med=(quick_sort(image1)[rcm]+quick_sort(image1)[rcm+1])/2
    # 최종
    for i in range(outH):
        for k in range(outW):
            if inImage[i][k] < med:
                outImage[i][k] = 0
            else:
                outImage[i][k] = 255
    displayImage()

def rotate90():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    for i in range(outH):
        for k in range(outW):
            outImage[k][outH-i-1]=inImage[i][k]
    displayImage()

def rotate180():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    for i in range(outH):
        for k in range(outW):
            outImage[outH-i-1][outW-k-1]=inImage[i][k]
    displayImage()

def rotate270():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    for i in range(outH):
        for k in range(outW):
            outImage[outW-k-1][i]=inImage[i][k]
    displayImage()

def udmirror():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    for i in range(outH):
        for k in range(outW):
            outImage[outH-i-1][k]=inImage[i][k]
    displayImage()

def lfmirror():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    for i in range(outH):
        for k in range(outW):
            outImage[i][outW-k-1]=inImage[i][k]
    displayImage()



## 전역 변수부
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
fileMenu.add_command(label='종료', command=None)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label='영상처리1', menu=image1Menu)
image1Menu.add_command(label='동일영상', command=equalImage)
image1Menu.add_command(label='반전', command=reverseImage)
image1Menu.add_command(label='밝게/어둡게', command=addImage)
image1Menu.add_command(label='흑백', command=blackImage)
image1Menu.add_command(label='흑백 평균', command=blackmeanImage)
image1Menu.add_command(label='흑백 중앙값', command=blackmedImage)
image1Menu.add_command(label='90도 회전', command=rotate90)
image1Menu.add_command(label='180도 회전', command=rotate180)
image1Menu.add_command(label='270도 회전', command=rotate270)
image1Menu.add_command(label='상하 미러링', command=udmirror)
image1Menu.add_command(label='좌우 미러링', command=lfmirror)


window.mainloop()



# 영상처리 알고리즘 분류
# -화소점 처리 (Pixel Processing)
# >동일 영상, 반전, 흑백, 감마, 파라볼라
# -기하학 처리 (Geometric Processing) 자리 바꾸기
# >이동, 회전, 축소, 확대
# -화소영역 처리 (Area Processing)
# >블러링(뿌옇게), 샤프닝(뚜렷하게), 경계선 처리, 지문 인식
# 히스토그램 처리(Histogram Processing) > 화소점 처리의 일부
# >흑백(평균, 중앙값), 평활화