#3036

N = int(input())
A = list(map(int,input().split()))

def GCD(a,b):
    a1 = max(a,b)
    b1 = min(a,b)
    while b1!=0:
        a1 = a1%b1
        a1,b1 = b1,a1
    return a1

for i in range(1,len(A)):
    print(str(int(A[0]/GCD(A[i],A[0])))+"/"+str(int(A[i]/GCD(A[i],A[0]))))