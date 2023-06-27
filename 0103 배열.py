import random
#함수
ary1=[]
#메인부
for i in range(10):
    ary1.append(0)
print(ary1)

#배열의 값 대입 2부터 짝수를 대입하자.
num=2
ary1=[]
for i in range(0,10,1):
    ary1.append(num)
    num+=2
print(ary1)

#랜덤한 숫자 10개
for i in range(0,10,1):
    ary1[i]=random.randint(0, 1000)
print(ary1)

#배열 처리
#1. 배열의 값의 합계
hap=0
for i in range(0,10,1):
    hap+=ary1[i]
print(hap)
#2. 배열 중 홀수만 합계
hap=0
for i in range(0,10,1):
    if (ary1[i]%2 != 0) :
        hap+=ary1[i]
print(hap)