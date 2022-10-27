#11050

N,K = map(int,input().split())

count = 1
oldA = [1,1]

for i in range(N-1):
    newA = [1]
    for i in range(len(oldA)-1):
        newA.append((oldA[i]+oldA[i+1])%10007)
    newA.append(1)
    oldA = [] + newA

print(oldA[K])