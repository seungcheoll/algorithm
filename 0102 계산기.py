#두 숫자의 더하기/뺴기 등등을 계산하기

#함수
def add_func(n1,n2):
    return n1+n2
#변수
num1,num2=0,0
result=0
#메인
num1=int(input('숫자 1 : '))
num2=int(input('숫자 2 : '))

result=add_func(num1,num2)
print(num1,"+",num2,'=',result)

#퀴즈 나머지 3개 곱하기 나누기 나머지, 제곱
#함수
def min_func(n1,n2):
    return n1-n2
#변수
num1,num2=0,0
result=0
#메인
num1=int(input('숫자 1 : '))
num2=int(input('숫자 2 : '))

result=min_func(num1,num2)
print(num1,"-",num2,'=',result)

#함수
def b_func(n1,n2):
    return n1*n2
#변수
num1,num2=0,0
result=0
#메인
num1=int(input('숫자 1 : '))
num2=int(input('숫자 2 : '))

result=b_func(num1,num2)
print(num1,"*",num2,'=',result)

#함수
def slash_func(n1,n2):
    return n1/n2
#변수
num1,num2=0,0
result=0
#메인
num1=int(input('숫자 1 : '))
num2=int(input('숫자 2 : '))

result=slash_func(num1,num2)
print(num1,"/",num2,'=',result)