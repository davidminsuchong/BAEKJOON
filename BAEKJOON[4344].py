#4344

C = int(input())
A = []
for i in range(C):
    A.append(list(map(int,input().split())))

for i in range(C):
    count = 0
    mean = sum(A[i][1:])/A[i][0]
    for j in range(1,A[i][0]+1):
        if A[i][j] > mean:
            count += 1
    print("{:.3f}".format(count/A[i][0]*100)+"%")