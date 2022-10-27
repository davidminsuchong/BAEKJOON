#9375

T = int(input())

for i in range(T):
    n = int(input())
    A = dict()
    B = set()
    count = 1
    answer = 1
    for j in range(n):
        a,b = input().split()
        try:
            A[b] += 1
        except:
            A[b] = 1
        B.add(b)
    print(A,B)
    for j in B:
        for k in range(1,A[j]+1):
            answer = answer*count/k
            count += 1
    print(int(answer))