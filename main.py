# 백준 수학1. 부녀회장
#k = 2
#n = 3
"""
T = int(input())
for t in range(T):

    k = int(input())
    n = int(input())

    mylist = []
    mylist.append( list(x for x in range(1,n+1)) ) #1층은 그냥 저장해놓기 [[1, 2, 3]]

    for i in range(1, k+1):
        mylist.append(list())

        for x in range(0, n):
            Bsum = 0
            for y in range(0, x+1):
                Bsum += mylist[i-1][y]
            mylist[i].append(Bsum)
        #print(str(i+1)+"번째(층) 리스트:")
        #print(mylist)

    #print("최종")
    print(mylist[k][n-1])
"""
# 수학1. HxW 호텔
"""
T = int(input())
for t in range(T):
    H, W, N = map(int, input().split()) #6, 12, 10
    strYY = ""
    strXX = ""  # YYXX호
    if(N<=H):
        strYY = str(N)
        strXX = "01"
    else:
        YY = N%H   # 10%6 = 4
        if(YY==0):
            YY = H
            XX = N//H
        else:
            XX = N//H + 1   # 10//6 + 1 = 2
        if(XX<10):
            strXX = "0"+str(XX)
        else:
            strXX = str(XX)
        strYY = str(YY)
    print(strYY+strXX) #402
"""
# 수학1. 분수
"""
#5층: 5/1  4/2  3/3  2/4  1/5  홀수 분자: range(5,0,-1)  분모: range(1, 5+1)
#4층: 1/4  2/3  3/2  4/1       짝수 분자: range(1, 4+1)  분모: range(4,0,-1)
#3층: 3/1  2/2  1/3
#2층: 1/2  2/1
#1층: 1/1
N = int(input())
step = 0
def floor(N):
    sub = N
    for i in range(1,N+1):
        sub -= i
        global step
        if(sub==0):
            step = i
            #print(i, "층에서", step, "번째")
            return i
        elif(sub<0):
            step = sub+i
            #print(i,"층에서",step,"번째")
            return i
F = floor(N)
if N!=1:
    F = floor(N)
else:
    F = 1
if(F%2 == 0): #짝수층
    bunlist = list(_ for _ in range(1, F + 1)) #F까지 오름차순
    molist = list(_ for _ in range(F, 0, -1))  #F부터 내림차순
else:
    bunlist = list(_ for _ in range(F, 0, -1))
    molist = list(_ for _ in range(1, F + 1))

print("%d/%d" % (bunlist[step-1], molist[step-1]))
"""
#다른사람 소스 참고하여 리팩토링, 제출은 안해봄
"""
N = int(input())
step = 0
def floor(N):
    sub = N
    for i in range(1,N+1):
        sub -= i
        global step
        if(sub==0):
            step = i
            print(i, "층에서", step, "번째")
            return i
        elif(sub<0):
            step = sub+i
            print(i,"층에서",step,"번째")
            return i
F = floor(N)
if N!=1:
    F = floor(N)
else:
    F = 1
if F%2 != 0:
    print("%d/%d" % (F-step+1, step))
else:
    print("%d/%d" % (step, F - step + 1))
"""
# 수학1. 설탕 11->3이 안나옴
"""
N = int(input())

EA = 0
ea = 0
if N//5 != 0 or N//3 != 0:
    if N%5 == 0:
        print('a1')
        EA = N//5
    elif N%3 == 0:
        print('a2')
        EA = N//3
    ea += N//5
    if (N%5)%3 == 0 :
        print('a3')
        ea += (N%5)//3
    else:
        print('a4')
        ea = -1
else:
    print('a5')
    ea = -1
print('..', EA, ea)
if EA > 0 and ea > 0:
    print('b1', EA, ea)
    print(min([EA, ea]))
elif ea > 0:
    print('b2')
    print(ea)
elif EA > 0:
    print(EA)
else:
    print(-1)
"""
#1. 1712 손익분기점 - 시간 초과
# a, b, c = map(int, input().split())
""" 출력초과
# i = 1 
# while 1:
#     if c==1 or c<b :
#         print(-1)
#         break
#     if(a+b*i) >= c*i:
#         i += 1
#     else:
#         print(i)
#         break  """
# if c == 1 or c<=b :
#     print(-1)
# else:
#     result = a//(c-b) + 1 # a = (c-b)*x
#     print(result)         # 1000 = (170-70)*x  --> result = x+1

# 4. 2869 달팽이
# A, B, V = map(int, input().split())  # (A-B)*X + A >= V
# result = 0
# if (V-A)%(A-B)==0:
#     result = (V-A)//(A-B)+1  # 2 1 5
# else:
#     result = (V-A)//(A-B)+2  # 5 1 6
# print(result)

# 수학1. 설탕2 --> 틀렸습니다.
N = int(input())  # 3x + 5y = 18  --> x = 18/3 - (5/3)y
x = 0
y = 0
result_list = []
while 1:
    x = round(N/3, 2) - round((5/3)*y,2) #반올림 안하면, x=1.999999가 나옴
    print(x,y)
    if x - int(x) == 0 and type(y)==int : #x값 소수점이 0이면(6.0)
        result_list.append(int(x+y))
    y += 1
    if 5*y > N:
        break
if len(result_list)==0:
    print(-1)
else:
    print(min(result_list))