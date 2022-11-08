#9461

T = int(input())

A = [1,1,1,2,2]

for i in range(T):
    N = int(input())
    try:
        print(A[N-1])
    except:
        while len(A)<N:
            A.append(A[-1]+A[len(A)-5])
        print(A[N-1])