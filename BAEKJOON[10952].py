#10952

T = 0
A = []
B = []

while(True):
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    A.append(a)
    B.append(b)
    T += 1
if T != 0:
    for i in range(T):
        print(A[i]+B[i])