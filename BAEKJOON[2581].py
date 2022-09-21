#2581

def prime(A):
    if A == 1:
        return 0
    if A == 2:
        return 1
    for i in range(2,A):
        if i == A-1:
            return 1
        if A%i == 0:
            return 0

M = int(input())
N = int(input())

summ = 0
mini = 0
count = 0

for i in range(M,N+1):
    if prime(i)==1:
        if count == 0:
            mini  = i
            count = 1
        summ += i

if count ==1:
    print(summ)
    print(mini)
else:
    print(-1)