##과제 1 흑백처리를 중앙값으로 하기

#필요한 모듈 불러오기
import random
##함수 정의 코드(디스플레이(화면출력))
def display():
    for i in range(ROW):
        for k in range(COL):
            print('%3d'%image[i][k],end=" ")
        print()
    print()


##변수 정의 코드
ROW,COL=5,5
image=None

##메인 코드
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

##중앙값을 기준으로 흑백 구분하기
#1차원 배열로 만들기
image1=[]
for i in range(ROW):
    for k in range(COL):
        a=image[i]
        b=a[k]
        image1.append(b)
print(f'2차원 배열을 1차원 배열로 만들면 {image1} 입니다.')

#퀵 소트 알고리즘
def quick_sort(image1):
    if len(image1)<=1:
        return image1
    pivot=image1[len(image1)//2]
    less, more, equal=[], [], []
    for each in image1:
        if each<pivot:
            less.append(each)
        elif each>pivot:
            more.append(each)
        else:
            equal.append(each)
    return quick_sort(less)+equal+quick_sort(more)
print(f'정렬한 이미지 list는 {quick_sort(image1)} 입니다.')
#중앙값 구하기
rcm = (ROW*COL) // 2
med = (quick_sort(image1)[rcm] + quick_sort(image1)[rcm + 1]) / 2
print(f'중앙값은 {med} 입니다.')

#이미지 변환
for i in range(ROW):
    for k in range(COL):
        if image[i][k]<med:
            image[i][k]=0
        else :
            image[i][k]= 255
display()