#1934

import sys

T = int(input())

for i in range(T):
    N = list(map(int,sys.stdin.readline().split()))
    N.sort()
    A = N[0]
    B = N[1]

    while A!=0:
            B = B%A
            A,B = B,A
    
    print(B*(N[0]//B)*(N[1]//B))