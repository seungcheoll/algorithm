import random
##함수
##디스플레이(화면출력)
def display():
    for i in range(ROW):
        for k in range(COL):
            print('%3d'%image[i][k],end=" ")
        print()
    print()
##변수
ROW,COL=5,5
image=None
##메인
##메모리 할당
image=[]
tmpAry=[]
for i in range(ROW):
    for k in range(COL):
        tmpAry.append(0)
    image.append(tmpAry)
    tmpAry=[]
print(image)
print(tmpAry)

##파일> 메모리로 로딩(Loading)
##파일> 디스크/ 메모리> ram (동적인/끄면 사라짐/배열)
ROW,COL=5,5
pixel=[]
for i in range(ROW):
    for k in range(COL):
        pixel=random.randint(0,255) #한장짜리 그레이 스케일
        image[i][k]=pixel
display()

##영상 처리
#(1) 영상을 50 밝게 처리하자.
#for i in range(ROW):
#    for k in range(COL):
#        if (image[i][k]+50>255):
#            image[i][k]=255
#        else :
#            image[i][k]+= 50
#display()

#퀴즈 :100 어둡게
# for i in range(ROW):
#   for k in range(COL):
#        if (image[i][k]-100<0):
#            image[i][k]=0
#        else :
#            image[i][k]-= 100  #image[i][k]=image[i][k]-100
# display()

#퀴즈: 완전 흑백 처리
# for i in range(ROW):
#     for k in range(COL):
#         if image[i][k]<127.5:
#             image[i][k]=0
#         else :
#             image[i][k]= 255
# display()

# 평균으로 흑백 처리
# hap=0
# for i in range(ROW):
#     for k in range(COL):
#         hap+=image[i][k]
# avg=hap/(ROW*COL)
# print(avg)
#
# for i in range(ROW):
#     for k in range(COL):
#         if image[i][k]<avg:
#             image[i][k]=0
#         else :
#             image[i][k]= 255
# display()

#퀴즈: 반전하기
# for i in range(ROW):
#    for k in range(COL):
#        image[i][k]=255-image[i][k]
# display()

##과제 1 흑백처리를 중앙값으로 하기 (퀵소트(.sort()) 구현>2차원 배열에서 1차원 배열로 바꾼 후 진행, 선택 정렬)
#1차원 배열로 만들기
image1=[]
for i in range(ROW):
    for k in range(COL):
        a=image[i]
        b=a[k]
        image1.append(b)
print(image1)

#퀵 소트 알고리즘
def quick_sort(image1):
    if len(image1)<=1:
        return image1
    pivot=image1[len(image1)//2]
    less, more, equal=[], [], []
    for each in image1:
        if each<pivot:
            less.append(each)
        elif each<pivot:
            more.append(each)
        else:
            equal.append(each)
    return quick_sort(less)+equal+quick_sort(more)

#중앙값 구하기
rcm = (ROW*COL) // 2
med = (quick_sort(image1)[rcm] + quick_sort(image1)[rcm + 1]) / 2
print(med)

#이미지 변환
for i in range(ROW):
    for k in range(COL):
        if image[i][k]<med:
            image[i][k]=0
        else :
            image[i][k]= 255
display()