print("Hello~world!")

num=100
if num>100:
    print('100보다크다')
else :
    print('100보다 작다')

hap=0
for i in range(1,101,1):
    hap+=1
print(hap)

hap=0
i=1
while (i<101) :
    hap+=i
    i+=1
print(hap)

hap=0
while hap<100:
    hap+=1
print(hap)

##함수 선언부
def addNumber(n1,n2):
    addhap=0
    for i in range(n1,n2+1):
        addhap+=1
    return addhap
##전역 변수부
hap=0
##메인 코드부
hap=addNumber(1,100)
print(hap)