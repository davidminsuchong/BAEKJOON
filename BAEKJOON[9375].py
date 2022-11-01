#9375

T = int(input())
Total = []

for i in range(T):
    n = int(input())
    A = dict()
    B = []
    for j in range(n):
        a,b = input().split()
        try:
            A[b] += 1
        except:
            A[b] = 1

    for j in A.values():
        B.append(j+1)

    total = 1
    for j in B:
        total = total*j
    total = total-1
    Total.append(total)

for j in Total:
    print(j)