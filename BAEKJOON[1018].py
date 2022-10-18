#1018

N,M = map(int,input().split())
n = N-7; m = M-7
A = []
for i in range(N):
    A.append([0]*m)
B = []

def count(a,b):
    count = 0
    if b == 0:
        for i in range(4):
            if a[i*2]=="W":
                count +=1
            if a[i*2+1]=="B":
                count +=1
    else:
        for i in range(4):
            if a[i*2]=="B":
                count +=1
            if a[i*2+1]=="W":
                count +=1
    return count


for i in range(N):
    a = input()
    b = i%2
    for j in range(m):
        A[i][j]=count(a[j:j+8],b)

for i in range(n):
    for j in range(m):
        count1 = 0
        for k in range(8):
            count1 += A[i+k][j]
        B.append(count1)

print(min(min(B),(64-max(B))))