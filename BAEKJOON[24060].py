#24060

def merge_sort(A,p,r):
    if p<r:
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

def merge(A,p,q,r):
    i = p; j = q+1; t = 0
    tmp = [0]*r
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
        t+=1; i+=1