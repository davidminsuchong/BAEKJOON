#1009

T = int(input())
B = []

for i in range(T):
    a,b = map(int,input().split())
    k = 1
    A = []
    for j in range(b):
        k = (k*a)%10
        if k==0:
            B.append(10)
            break
        if k in A:
            k=-1
            B.append(A[b%len(A)-1])
            break
        A.append(k)
    if k==-1 or k==0:
        continue
    else:
        B.append(k)
        
for i in B:
    print(i)