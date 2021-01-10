# 백준 수학1. 부녀회장
#k = 2
#n = 3
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

