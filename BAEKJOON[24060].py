#24060

def merge_sort(p,r,A):
    if p<r:
        q = (p+r)//2
        merge_sort(p,q,A)
        merge_sort(q+1,r,A)
        merge(p,q,r,A)

def merge(p,q,r,A):
    global count
    i = p; j = q+1
    tmp = []
    while (i <= q and j <= r):
        if (A[i]<=A[j]):
            tmp.append(A[i])
            i+=1
        else:
            tmp.append(A[j])
            j+=1
    while(i<=q):
        tmp.append(A[i])
        i+=1
    while(j<=r):
        tmp.append(A[j])
        j+=1
    i=p; t=0
    while i<=r:
        A[i] = tmp[t]
        count += 1
        if count ==K:
            print(A[i])
            exit()
        i+=1; t+=1

global count

N,K = map(int,input().split())
A = list(map(int,input().split()))
count = 0

merge_sort(0,N-1,A)
print(-1)