##오븐
# a,b=map(int,input().split())
# c= int(input())
# a+=c//60
# b+=c%60
# if b>=60:
#     a+=1
#     b=b-60
# if a>=24:
#     a=a-24
# print(a,b)

# final_minute=a*60+b+c
# final_hour=(final_minute//60)%24
# final_minute=final_minute%60
# print(final_hour,final_minute)


##별찍기 8
# n=int(input())
# for i in range(1,2*n):
#     col=2*n
#     star=(n-abs(n-i))
#     l = "*"*star+" "*(col-2*star)+'*'*star
#     print(l)

# import sys
# N=int(input())
# s=list(map(int,sys.stdin.readline().split()))
# d=int(input())
# c = 0
# for i in s:
#     if d==i:
#         c+=1
# print(c)

# N,X=map(int,input().split())
# line = list(map(int,input().split()))
# for value in line:
#     if value<X :
#         print(value,end=" ")

# n,m=map(int,input().split())
# a=[list(map(int,input().split()))for _ in range(n)]
# b=[list(map(int,input().split()))for _ in range(n)]
# for i in range(n):
#     for k in range(m):
#         print(a[i][k]+b[i][k],end=" ")
#     print()

# N,M= map(int,input().split())
# d=[0 for _ in range(N)]
# for _ in range(M):
#     a,b,c= map(int,input().split())
#     for i in range(a,b+1):
#         d[i-1]=c
# for j in range(N):
#     print(d[j],end=" ")

# N,M= map(int,input().split())
# ba=[i for i in range(1,N+1)]
# for _ in range(M):
#     i,j=map(int,input().split())
#     tmp=ba[i-1]
#     ba[i-1]=ba[j-1]
#     ba[j-1]=tmp
# for k in range(N):
#     print(ba[k],end=" ")

# a=[int(input()) for _ in range(10)]
# b=[0 for _ in range(10)]
# for i in range(10):
#     b[i]=a[i]%42
#     c=set(b)
# print(len(c))


# import sys
# N=int(input())
# a=[int(sys.stdin.readline())for _ in range(N)]
# a.sort()
# for i in range(N):
#     print(a[i])

##주사위
# import sys
# N,M,r,c,k = map(int,sys.stdin.readline().split())
# dir_r = [0,0,-1,1]
# dir_c = [1,-1,0,0]
# dice = [0,0,0,0,0,0]
# tile = [list(map(int,input().split())) for _ in range(N)]
# move = list(map(int,input().split()))
# for i in range(k):
#     fm = move[i]-1
#     rn = r + dir_r[fm]
#     cn = c + dir_c[fm]
#     if not (0 <= rn <= N-1) or not (0 <= cn <= M-1) :
#         continue
#     if fm == 0:
#         dice = [dice[0], dice[5], dice[1], dice[2], dice[4], dice[3]]
#     elif fm ==1:
#         dice = [dice[0], dice[2], dice[3], dice[5], dice[4], dice[1]]
#     elif fm == 2:
#         dice = [dice[2], dice[1], dice[4], dice[3], dice[5], dice[0]]
#     else :
#         dice = [dice[5], dice[1], dice[0], dice[3], dice[2], dice[4]]
#
#     if tile[rn][cn]==0:
#         tile[rn][cn]=dice[5]
#     else:
#         dice[5]=tile[rn][cn]
#         tile[rn][cn]=0
#     r, c = rn, cn
#     print(dice[2])

## 리모콘
# import sys
# n,m=map(int,sys.stdin.readline().split())
# r,c,d=map(int,sys.stdin.readline().split())
# floor=[list(map(int,sys.stdin.readline().split()))for _ in range(n)]
# area=1
# dr=[-1,0,1,0]
# dc=[0,1,0,-1]
# while True:
#     floor[r][c]=2
#     for i in range(d+3,d-1,-1):
#         if i>3:
#             i=i%4
#         nr=r+dr[i]
#         nc=c+dc[i]
#         if floor[nr][nc]==0:
#             r=nr
#             c=nc
#             d=i
#             area+=1
#             break
#     else:
#         nr=r-dr[i]
#         nc=c-dc[i]
#         if floor[nr][nc] != 1:
#             r=nr
#             c=nc
#         else:
#             break
# print(area)

##블랙잭
# import sys
# N,M=map(int,input().split())
# card=list(map(int,input().split()))
# card.sort()
# last=[]
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             card_sum=card[i]+card[j]+card[k]
#             if card_sum>M:
#                 continue
#             else:
#                 last.append(card_sum)
# print(max(last))

##영화감독 숌
# N = int(input())
# movie = 666
#
# while N:
#     if "666" in str(movie):
#         N -= 1
#     movie += 1
#
# print(movie - 1)


##설탕 배달
# N=int(input())
# a=0
# if N%5==0:
#     a=N//5
# else:
#     while N>0:
#         N -= 3
#         a += 1
#         if N%5==0:
#             a += N//5
#             print(a)
#             break
#         elif N==1 or N==2:
#             print(-1)
#         elif N==0:
#             print(a)
#             break


##날짜 계산
# import sys
# e,s,m=map(int, sys.stdin.readline().split())
# e=e-1
# s=s-1
# m=m-1
# time=1
# while True:
#     if ((time-1)%15)==e and ((time-1)%28)==s and ((time-1)%19)==m:
#         print(time)
#         break
#     time +=1


##난쟁이
# tall=[int(input())for _ in range(9)]
# tall_sum=sum(tall)
# tall.sort()
# is_ok=False
# for i in range(8):
#     for j in range(i+1,9):
#         temp= tall_sum-(tall[i]+tall[j])
#         if temp==100:
#             is_ok=True
#             break
#     if is_ok:
#         break
# tall.remove(tall[j])
# tall.remove(tall[i])
# for i in range(7):
#     print(tall[i])


##색종이
# import sys
# tile=[[0 for _ in range(100)]for _ in range(100)]
# N=int(input())
# dot=[list(map(int,sys.stdin.readline().split()))for _ in range(N)]
# for i in range(N):
#     for j in range(10):
#         for k in range(10):
#             tile[dot[i][0]+j][dot[i][1]+k]=1
# print(sum([sum(t) for t in tile]))

##차이를 최대로
# from itertools import permutations
# import sys
# n=int(input())
# m=list(map(int,sys.stdin.readline().split()))
# a=[]
# # permutation end
# for i in permutations(m,n):
#     a.append(list(i))
# maximum = 0
# # temp_sum
# for i in a:
#     temp_sum = 0
#     for j in range(n-1):
#         temp=abs(i[j]-i[j+1])
#         temp_sum += temp
#     if temp_sum > maximum:
#         maximum = temp_sum
# print(maximum)


# import sys
# max_a=0
# r=0
# c=0
# ar=[list(map(int,sys.stdin.readline().split()))for _ in range(9)]
# for i in range(9):
#     if max(ar[i])>=max_a:
#         max_a=max(ar[i])
#         x=i+1
#         y=ar[i].index(max_a)
# print(max_a)
# print(x, y+1)


# a=[list(input().rstrip())for _ in range(5)]
# max_a=0
# for i in a:
#     if len(i) > max_a:
#         max_a=len(i)
# for i in range(max_a):
#     for j in range(5):
#         try:
#             print(a[j][i],end="")
#         except:
#             pass


# while True:
#     a,b=map(int,input().split())
#     if a==0 and b==0:
#         break
#     if b//a==b/a:
#         print('factor')
#     elif a//b==a/b:
#         print('multiple')
#     else:
#         print('neither')


# n,k=map(int,input().split())
# a=[]
# for i in range(1,n+1):
#     if n%i==0:
#         a.append(i)
# if len(a)<k:
#     print(0)
# else:
#     print(a[k-1])


# #달팽이
# n = int(input())
# k = int(input())
# r, c = n // 2, n // 2
# tile = [[0 for _ in range(n)] for _ in range(n)]
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
# d = 0
# for a in range(1, n ** 2 + 1):
#     tile[r][c] = a
#     if a == k:
#         e = r+1
#         f = c+1
#     if d > 3:
#         d = d % 4
#     nr = r + dr[d]
#     nc = c + dc[d]
#     if tile[nr][nc] != 0:
#         d -= 1
#     r = r + dr[d]
#     c = c + dc[d]
#     d += 1
# for i in range(n):
#     for j in range(n):
#         print(tile[i][j], end=" ")
#     print()
# print(e, f)

# #회의실 배정
# import sys
# n=int(sys.stdin.readline())
# time=[list(map(int,sys.stdin.readline().split()))for _ in range(n)]
# time.sort(key=lambda x:(x[1], x[0]))
# cnt=0
# c=0
# for a, b in time:
#     if a>=c:
#         cnt+=1
#         c=b
# print(cnt)

# #체스판
# import sys
# n,m=map(int,sys.stdin.readline().split())
# a=[]
# paint=[]
# for _ in range(n):
#     a.append(input())
# for i in range(n-7):
#     for j in range(m-7):
#         w_cnt=0
#         b_cnt=0
#         for k in range(i,i+8):
#             for p in range(j,j+8):
#                 if (k+p)%2==0:
#                     if a[k][p]!='W':
#                         w_cnt+=1
#                     else:
#                         b_cnt+=1
#                 else:
#                     if a[k][p]=='W':
#                         w_cnt+=1
#                     else:
#                         b_cnt+=1
#         paint.append(w_cnt)
#         paint.append(b_cnt)
# print(min(paint))

# #리모컨
# import sys
# ch=int(sys.stdin.readline())
# n=int(sys.stdin.readline())
# n_remote=list(map(int,sys.stdin.readline().split()))
# min_click=abs(ch-100)
# for i in range(1000001):
#     i=str(i)
#     for j in range(len(i)):
#         if int(i[j]) in n_remote:
#             break
#         elif j==len(i)-1:
#             min_click=min(min_click,abs(int(i)-ch)+len(i))
# print(min_click)

# # 외판원 순환2
# import sys
# from itertools import permutations
# n=int(input())
# road=[list(map(int,sys.stdin.readline().split()))for _ in range(n)]
# answer=10000000
# for i in permutations(range(1,n),n-1):
#     num=[*i]
#     num=[0]+num+[0]
#     hap=0
#     for k in range(n):
#         cost=road[num[k]][num[k+1]]
#         if cost==0:
#             break
#         hap+=cost
#         if hap>answer:
#             break
#     else:
#         if answer>hap:
#             answer=hap
# print(answer)]

# # 셀프 넘버
# a=list(range(1,10001))
# delete=[]
# for i in a:
#     for k in str(i):
#         i += int(k)
#     if i<=10000:
#         delete.append(i)
# for i in set(delete):
#     a.remove(i)
# for j in a:
#     print(j)

# #덩치
# import sys
# n=int(sys.stdin.readline())
# dung=[list(map(int,sys.stdin.readline().split()))for _ in range(n)]
# rank=[1 for _ in range(n)]
# for i in range(n):
#     for k in range(i+1,n):
#         if dung[i][0]>dung[k][0] and dung[i][1]>dung[k][1]:
#             rank[k]+=1
#         elif dung[i][0]<dung[k][0] and dung[i][1]<dung[k][1]:
#             rank[i]+=1
# for i in range(n):
#     print(rank[i],end=" ")

# #피보나치 수
# import sys
# n=int(sys.stdin.readline())
# pivo=[0,1]
# for _ in range(n-1):
#     a=pivo[len(pivo)-1]+pivo[len(pivo)-2]
#     pivo.append(a)
# print(pivo[n])


# # 저항
# b=[]
# c=0
# for _ in range(2):
#     a= input()
#     if a=='black':
#         b.append(0)
#     if a=='brown':
#         b.append(1)
#     if a=='red':
#         b.append(2)
#     if a=='orange':
#         b.append(3)
#     if a=='yellow':
#         b.append(4)
#     if a=='green':
#         b.append(5)
#     if a=='blue':
#         b.append(6)
#     if a=='violet':
#         b.append(7)
#     if a=='grey':
#         b.append(8)
#     if a=='white':
#         b.append(9)
# for _ in range(1):
#     a= input()
#     if a == 'black':
#         c=b[0]*10+b[1]
#     if a == 'brown':
#         c=b[0]*100+b[1]*10
#     if a == 'red':
#         c=b[0]*1000+b[1]*100
#     if a == 'orange':
#         c=b[0]*10000+b[1]*1000
#     if a == 'yellow':
#         c=b[0]*100000+b[1]*10000
#     if a == 'green':
#         c=b[0]*1000000+b[1]*100000
#     if a == 'blue':
#         c=b[0]*10000000+b[1]*1000000
#     if a == 'violet':
#         c=b[0]*100000000+b[1]*10000000
#     if a == 'grey':
#         c=b[0]*1000000000+b[1]*100000000
#     if a == 'white':
#         c=b[0]*10000000000+b[1]*1000000000
# print(c)


# #행렬 곱셈
# import sys
# ar,ac=map(int,sys.stdin.readline().split())
# a=[list(map(int,sys.stdin.readline().split()))for _ in range(ar)]
# br,bc=map(int,sys.stdin.readline().split())
# b=[list(map(int,sys.stdin.readline().split()))for _ in range(br)]
# c=[[0 for _ in range(bc)] for _ in range(ar)]
# for i in range(ar):
#     for j in range(ac):
#         for k in range(bc):
#             c[i][k]+=a[i][j]*b[j][k]
# for s_c in c:
#     for p in s_c:
#         print(p,end=" ")
#     print()


# #별찍기-20
# n = int(input())
# if n == 1:
#     print('*')
# else:
#     for i in range(n):
#         if i%2==0:
#             print('* '*n)
#         else:
#             print(' *'*n)

# #트럭 주차
# import sys
# one, two, three = map(int, sys.stdin.readline().split())
# time = [list(map(int,sys.stdin.readline().split()))for _ in range(3)]
# parking = [0 for _ in range(max(time[0][1], time[1][1], time[2][1]))]
# p_cost = 0
# for i in time:
#     for k in range((i[0]-1),(i[1]-1)):
#         parking[k] += 1
# for i in range(len(parking)):
#     if parking[i] == 1:
#         p_cost += one
#     elif parking[i] == 2:
#         p_cost += two*2
#     elif parking[i] == 3:
#         p_cost += three*3
# print(p_cost)

# # 새
# a=int(input())
# b=0
# i=0
# while a>0:
#     i+=1
#     a -= i
#     b += 1
#     if i<a:
#         pass
#     else:
#         i=0
# print(b)

# # 큐 2
# from collections import deque
# import sys
# n=int(sys.stdin.readline())
# queue=[]
# yeah=deque(queue)
# for _ in range(n):
#     temp=deque(sys.stdin.readline().split())
#     if temp[0]=='push':
#         yeah.append(int(temp[1]))
#     if temp[0]=='pop':
#         if len(yeah)==0:
#             print(-1)
#         else:
#             print(yeah.popleft())
#     if temp[0]=='size':
#         print(len(yeah))
#     if temp[0]=='empty':
#         if len(yeah)==0:
#             print(1)
#         else:
#             print(0)
#     if temp[0]=='front':
#         if len(yeah)==0:
#             print(-1)
#         else:
#             print(yeah[0])
#     if temp[0]=='back':
#         if len(yeah)==0:
#             print(-1)
#         else:
#             print(yeah[len(yeah)-1])

# # 카드 2
# from collections import deque
# import sys
# n=int(sys.stdin.readline())
# card=deque(i for i in range(1,n+1))
# while len(card)>1:
#     card.popleft()
#     change_card=card.popleft()
#     card.append(change_card)
# print(card[0])

# #요세푸스 0
# from collections import deque
# import sys
# n,k = map(int,sys.stdin.readline().split())
# circle=deque(list(i for i in range(1,n+1)))
# res=[]
# while n:
#     for i in range(k-1):
#         circle.append(circle.popleft())
#     res.append(circle.popleft())
#     n-=1
# print('<',end="")
# for k in range(len(res)-1):
#     print(res[k] ,end=", ")
# print(res[len(res)-1],end=">")


# # 유기농 배추
# # dfs
# import sys
# sys.setrecursionlimit(10**8)
# input=sys.stdin.readline
# n= int(input())
# dr=[1,-1,0,0]
# dc=[0,0,-1,1]
# def dfs(cab_r,cab_c):
#     if 0<=cab_r<=r-1 and 0<=cab_c<=c-1 and grid[cab_r][cab_c]==1:
#         grid[cab_r][cab_c]=0
#         for d in range(4):
#             dfs((cab_r+dr[d]),(cab_c+dc[d]))
#         return True
#     return False
# for _ in range(n):
#     cnt = 0
#     c,r,k=map(int,input().split())
#     grid=[[0 for _ in range(c)] for _ in range(r)]
#     for _ in range(k):
#         cab_c,cab_r=map(int,input().split())
#         grid[cab_r][cab_c]=1
#     for i in range(r):
#         for k in range(c):
#             if dfs(i,k) == True:
#                 cnt+=1
#     print(cnt)

# bfs
# import sys
# from collections import deque
# sys.setrecursionlimit(10**8)
# input=sys.stdin.readline
# n= int(input())
# dr=[1,-1,0,0]
# dc=[0,0,-1,1]
# def bfs(x,y):
#     q=deque([(x,y)])
#     grid[x][y]=0
#     flag=False
#     while q:
#         x,y=q.popleft()
#         for d in range(4):
#             n_r=x+dr[d]
#             n_c=y+dc[d]
#             if 0<=n_r<=r-1 and 0<=n_c<=c-1 and grid[n_r][n_c]==1:
#                 q.append((n_r,n_c))
#                 grid[n_r][n_c]=0
#                 flag=True
#     return flag
# for _ in range(n):
#     c,r,k=map(int,input().split())
#     grid=[[0 for _ in range(c)] for _ in range(r)]
#     for _ in range(k):
#         cab_c,cab_r=map(int,input().split())
#         grid[cab_r][cab_c]=1
#     cnt = 0
#     for i in range(r):
#         for k in range(c):
#             if bfs(i,k):
#                 cnt+=1
#     print(cnt)

# # 숨바꼭질
# from collections import deque
# def bfs(x):
#     q=deque([x])
#     while q:
#         s=q.popleft()
#         if s==k:
#             print(visit[s])
#             break
#         for i in (s-1,s+1,s*2):
#             if 0<=i<=100000 and visit[i]==0:
#                 visit[i] = visit[s]+1
#                 q.append(i)
# visit=[0 for _ in range(100001)]
# n,k=map(int,input().split())
# bfs(n)

# #스택
# import sys
# n=int(sys.stdin.readline())
# stack=[]
# for _ in range(n):
#     command=list(sys.stdin.readline().split())
#     if command[0]=='push':
#         stack.append(command[1])
#     if command[0]=='pop':
#         if len(stack)==0:
#             print(-1)
#         else:
#             print(stack.pop())
#     if command[0]=='size':
#         print(len(stack))
#     if command[0]=='empty':
#         if len(stack)==0:
#             print(1)
#         else:
#             print(0)
#     if command[0]=='top':
#         if len(stack)==0:
#             print(-1)
#         else:
#             print(stack[len(stack)-1])

# #피보나치 수
# import sys
# input=sys.stdin.readline
# def fivo(n):
#     if n==0:
#         return 0
#     if n==1 or n==2:
#         return 1
#     return fivo(n-1)+fivo(n-2)
# n=int(input())
# print(fivo(n))

# #로또
# from itertools import combinations
# import sys
# while True:
#     t=list(map(int,sys.stdin.readline().split()))
#     if t[0]==0:
#             break
#     n=t[1:]
#     for i in list(combinations(n,6)):
#         for k in i:
#             print(k,end=" ")
#         print()
#     print()

# #dfs와 bfs
# from collections import deque
# import sys
# input=sys.stdin.readline
# n, m, v=map(int, input().split())
#
# node=[[] for _ in range(n+1)]
# for _ in range(m):
#     n1, n2=map(int,input().split())
#     node[n1].append(n2)
#     node[n2].append(n1)
# for a in node: # 노드 인접 순서 변경
#     a.sort()
#
# visit_dfs=[0 for _ in range(n+1)]
# result_dfs=[]
#
# def dfs(v):
#     if visit_dfs[v]==0:
#         result_dfs.append(v)
#         visit_dfs[v]=1
#         for i in node[v]:
#             dfs(i)
#     return result_dfs
#
# visit_bfs=[0 for _ in range(n+1)]
# result_bfs=[]
# def bfs(v):
#     q=deque()
#     q.append(v)
#     visit_bfs[v]=1
#     result_bfs.append(v)
#     while q:
#         cur=q.popleft()
#         for k in node[cur]:
#             if visit_bfs[k]==0:
#                 q.append(k)
#                 visit_bfs[k]=1
#                 result_bfs.append(k)
#     return result_bfs
#
# for i in dfs(v):
#     print(i, end=" ")
# print()
# for i in bfs(v):
#     print(i, end=" ")

# #1,2,3 더하기
# import sys
# input=sys.stdin.readline
# t=int(input())
# for _ in range(t):
#     n=int(input())
#     sum_n=[0 for _ in range(12)]
#     sum_n[0]=0
#     sum_n[1]=1
#     sum_n[2]=2
#     sum_n[3]=4
#     for i in range(4,n+1):
#         sum_n[i]=sum_n[i-1]+sum_n[i-2]+sum_n[i-3]
#     print(sum_n[n])

# #암호 만들기
# import sys
# from itertools import combinations
# input=sys.stdin.readline
# l,c = map(int, input().split())
# dict=list(input().split())
# dict.sort()
# vowel=['a','e','i','o','u']
# total=[]
# print_total=set()
# for i in combinations(dict,l):
#     total.append(list(i))
#     for k in total:
#         cnt_v = 0
#         cnt_c=0
#         for j in k:
#             if j in vowel:
#                 cnt_v+=1
#             else:
#                 cnt_c+=1
#         if (1<=cnt_v)and(2<=cnt_c):
#             print_total.add(tuple(k))
# a=list(print_total)
# a.sort()
# for i in a:
#     for k in list(i):
#         print(k,end="")
#     print()

# # 퇴사
# import sys
# input = sys.stdin.readline
# n = int(input())
# time_list = []
# pay_list = []
# final_pay = 0
# for i in range(n):
#     time, pay = map(int, input().split())
#     time_list.append(time)
#     pay_list.append(pay)
# def leave(day, pay_): # 전수조사 > 벗어나는 경우는 생각 x
#     global final_pay
#     if day == n:
#         final_pay = max(pay_, final_pay)
#         return final_pay
#     if day < n:
#         leave(day + time_list[day], pay_ + pay_list[day]) #당일 회의 o
#         leave(day + 1, pay_) #당일 회의 x
# leave(0,0)
# print(final_pay)


# #퇴사 (dynamic programming)
# import sys
# input = sys.stdin.readline
# n = int(input())
# tp_list=[]
# pay_list=[0 for _ in range(n+1)]
# for _ in range(n):
#     time, pay = map(int, input().split())
#     tp_list.append([time,pay])
# for i in range(n):
#     for k in range(i+tp_list[i][0],n+1):
#         if pay_list[k]<pay_list[i]+tp_list[i][1]:
#             pay_list[k]=pay_list[i]+tp_list[i][1]
# print(pay_list)
# print(pay_list[-1])

# #드래곤 커브
# import sys
# input=sys.stdin.readline
# n=int(input())
# grid=[[0 for _ in range(101)]for _ in range(101)]
# dr=[0,-1,0,1]
# dc=[1,0,-1,0]
# n_dragon=0
# for _ in range(n):
#     c,r,d,g=map(int,input().split())
#     grid[r][c]=1
#     curve=[d]
#
#     for i in range(g):
#         for k in range(len(curve)-1,-1,-1):
#             curve.append((curve[k]+1)%4)
#     print(curve)
#     for j in range(len(curve)):
#         r = r + dr[curve[j]]
#         c = c + dc[curve[j]]
#         if r<0 and r>100 and c>100 and c<0:
#             break
#         else :
#             grid[r][c]=1
#
# for i in range(100):
#     for k in range(100):
#         if grid[i][k]==1 and grid[i+1][k]==1 and grid[i][k+1]==1 and grid[i+1][k+1]==1:
#             n_dragon+=1
# print(n_dragon)

# # 뱀
# import sys
# from collections import deque
# input=sys.stdin.readline
# move=[]
#
# n=int(input())
# k=int(input())
#
# board=[[0 for _ in range(n)]for _ in range(n)]
# board[0][0]=1
# for _ in range(k):
#     apple_r,apple_c=map(int,input().split())
#     board[apple_r-1][apple_c-1]=2
#
# l=int(input())
# for _ in range(l):
#     x,d=map(str,input().split())
#     move.append([int(x),d])
#
# snake=deque()
# snake.append((0,0))
# dr=[0,1,0,-1]
# dc=[1,0,-1,0]
# snake_d=0
# time = 0
# r,c=0,0
# def turn(direction):
#     global snake_d
#     if direction=='L':
#         snake_d=(snake_d-1)%4
#         return snake_d
#     elif direction=='D':
#         snake_d=(snake_d+1)%4
#         return snake_d
#
# time_idx=0
# while True:
#     time += 1
#     r=r+dr[snake_d]
#     c=c+dc[snake_d]
#     if r<0 or r>n-1 or c<0 or c>n-1 or (r,c) in snake:
#         break
#     if board[r][c]==2:
#         snake.append((r,c))
#         board[r][c]=0
#     else:
#         snake.popleft()
#         snake.append((r,c))
#     if time==move[time_idx][0]:
#         snake_d=turn(move[time_idx][1])
#         if time_idx<len(move)-1:
#             time_idx+=1
# print(time)


# #톱니바퀴
# from collections import deque
# gear=[deque(list(map(int,input()))) for _ in range(4)]
# k=int(input())
# def turn_gear(gear_idx,d):
#     if d==1:
#         a=gear[gear_idx-1].pop()
#         gear[gear_idx-1].appendleft(a)
#     else:
#         b = gear[gear_idx-1].popleft()
#         gear[gear_idx-1].append(b)
# for _ in range(k):
#     gear_idx, d=map(int,input().split())
#     right_gear, left_gear=gear[gear_idx-1][2], gear[gear_idx-1][6]
#     right_d, left_d = d,d
#     turn_gear(gear_idx,d)
#     for i in range(gear_idx+1,5):
#         if right_gear!=gear[i-1][6]:
#             right_gear=gear[i-1][2]
#             right_d *= -1
#             turn_gear(i,right_d)
#         else:
#             break
#     for k in range(gear_idx-1,0,-1):
#         if left_gear!=gear[k-1][2]:
#             left_gear=gear[k-1][6]
#             left_d *= -1
#             turn_gear(k,left_d)
#         else:
#             break
# # 최종 score구하기
# score=0
# if gear[0][0] == 1:
#     score += 1
# if gear[1][0] == 1:
#     score += 2
# if gear[2][0] == 1:
#     score += 4
# if gear[3][0] == 1:
#     score += 8
# print(score)

#임예빈 바보
