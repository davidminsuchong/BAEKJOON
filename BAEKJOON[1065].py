#1065

def hansu(n):
    if len(str(n))<=2:
        return 1
    A = []
    for i in(str(n)):
        A.append(int(i))
    for i in range(len(A)-1):
        diff = A[i+1]-A[i]
        if i==0:
            old = diff
        elif diff != old:
            return 0
    return 1

N = int(input())
hans = 0

for i in range(N):
    hans += hansu(i+1)

print(hans)