#1912

n = int(input())
A = list(map(int,input().split()))

max1 = max(A)
total1 = 0
max2 = max(A)
total2 = 0

for i in range(n):
    total1 += A[i]
    total2 += A[n-1-i]
    if total1>max1:
            max1 = total1
    if total2>max2:
            max2 = total2
    if total1<0:   
        total1 = 0
    if total2<0:   
        total2 = 0

print(max(max1,max2))