#1620

import sys

N,M = map(int,input().split())
inventory = dict()
A = []

for i in range(N):
    a = sys.stdin.readline().rstrip()
    inventory[a] = str(i+1)
    A.append(a)

for i in range(M):  
    a = sys.stdin.readline().rstrip()
    try:
        print(inventory[a])
    except:
        print(A[int(a)-1])