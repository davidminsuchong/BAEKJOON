#1037

N = int(input())

A = list(map(int,input().split()))
A.sort()
B = dict()

number = 1

for i in range(N):
    k = A[i]
    for j in range(N):
        count = 0
        num = A[j]

        if k==0 or num==0:
            continue
        if num%k != 0:
            continue
        while num%k == 0:
            num = num//k
            count += 1 
            if num == 1:
                B[k] = count
        A[j] = 0

for key in B.keys():
    number = number*(key**B[key])

if len(B)==1:
    print(number*key)
else:
    print(number)