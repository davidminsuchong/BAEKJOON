#25501

import sys

def recursion(S,l,r,n):
    if l >= r:
        return [1,n]
    elif S[l] != S[r]:
        return [0,n]
    else:
        return recursion(S,l+1,r-1,n+1)

def isPalindrome(S):
    n = 1
    return recursion(S,0,len(S)-1,n)

T = int(input())
A = []
for i in range(T):
    A.append(isPalindrome(sys.stdin.readline().strip()))

for i in range(T):
    print(A[i][0],A[i][1])