#24060

import sys

def merge_sort(p,r):
    if p<r:
        q = (p+r)//2
        merge_sort(p,q)
        merge_sort(q+1,r)
        merge(p,q,r)

def merge(p,q,r):
    global A
    global count
    global K
    i = p; j = q+1; t = 0
    tmp = [0]*(r+1)
    while (i <= q and j <= r):
        if (A[i]<=A[j]):
            tmp[t] = A[i]
            t+=1; i+=1
        else:
            tmp[t] = A[j]
            t+=1; j+=1
    while(i<=q):
        tmp[t] = A[i]
        t+=1; i+=1
    while(j<=r):
        tmp[t] = A[j]
        t+=1; j+=1
    i=p; t=0
    while (i<=r):
        A[i] = tmp[t]
        count += 1
        if count == K:
            print(A[i])
            exit()
        i+=1; t+=1

global A
global count
global K
N,K = map(int,input().split())

A = list(map(int,sys.stdin.readline().split()))
count = 0

merge_sort(0,N-1)
print(-1)