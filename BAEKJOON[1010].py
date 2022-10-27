#1010

from math import factorial
T = int(input())
A = []

for i in range(T):
    N,M = map(int,input().split())
    answer = 1
    for i in range(N):
        answer = answer*(M-i)/(i+1)
    A.append(int(answer))

print(*A)