#11653

def prime(A):
    if A == 1:
        return 0
    if A == 2:
        return 1
    if A == 3:
        return 1
    for i in range(3,int(A**0.5+1),2):
        if i == A-1:
            return 1
        if A%i == 0:
            return 0

N = int(input())
A = []
for i in range(2,10000001):
    if prime(i)==1:
        A.append(i)

while True:
    if N == 1:
        exit()
    for i in A:
        if N%i==0:
            print(i)
            N = int(N/i)
            break