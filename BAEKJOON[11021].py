#11021
import sys

T = int(input())
A = []
B = []

for i in range(T):
    a,b = map(int,sys.stdin.readline().split())
    A.append(a)
    B.append(b)

for i in range(T):
    print("Case #"+str(i+1)+":",A[i]+B[i])