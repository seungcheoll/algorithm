## 파일은 2가지
#텍스트 파일
#(메모장에서 글자로 보이면(영어기준 1글자 1bite))
#(1bite를 끊어서 입력)
#(아스키 코드(a~z까지 숫자가 부여됨. A=64))
#바이너리 파일 > 이미지 파일 중 raw 파일. (1bite를 기준으로 한 픽셀을 표현함)(1bite > 8bit로 표현가능한 글자 (0~255))
#(2진 파일)
#(bit가 기준)
#(hwp는 크기, 색이 있기에 1bite를 범주별로 쪼갬)>(텍스트로 옮기니 오류)
#(고유의 프로그램이 필요함)(모든 바이너리 파일은 복제가 가능하기에 비밀)

#바이너리 파일 중 raw 파일 > 크기에 root 씌우면 가로=세로
import os.path
import math

filename = 'Etc_Raw(squre)\LENA256.RAW'
# 파일 크기 알아내기
fSize = os.path.getsize(filename) # Byte 단위
height = width = int(math.sqrt(fSize))
print(height, 'x', width)
# 메모리 확보 (영상 크기)
image = [ [0 for _ in range(width)] for _ in range(height)]
# 파일 --> 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height) :
    for k in range(width) :
        image[i][k] = ord(rfp.read(1)) #하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
rfp.close()
## 일부만 확인
# for i in range(100, 105, 1):
#     for k in range(100, 105, 1):
#         print("%3d " % image[i][k], end='')
#     print()
# print()
#함수 처리
def display():
    for i in range(100,105,1):
        for k in range(100,105,1):
            print('%3d'%image[i][k],end=" ")
        print()
    print()
#반전
for i in range(height):
    for k in range(width):
        image[i][k]=255-image[i][k]
display()
#흑백처리
# hap=0
# for i in range(height):
#     for k in range(width):
#         hap+=image[i][k]
# avg=hap/(height*width)
# print(avg)
#
# for i in range(height):
#     for k in range(width):
#         if image[i][k]<avg:
#             image[i][k]=0
#         else :
#             image[i][k]= 255
# display()

#big@python 문서 암호


