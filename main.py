# 백준 부녀회장

k = 2
n = 3
mylist = []
mylist.append( list(x for x in range(1,n+1)) )

for i in range(1, n):
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
