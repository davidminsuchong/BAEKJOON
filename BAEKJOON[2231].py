#2231

def sum_M(M):
    sumM = int(M)
    for i in range(len(M)):
        sumM += int(M[i])
    return sumM

N = input()
a = int(N[0])+9*(len(N)-1)

M = str(int(N)-a)

for i in range(a):
    if sum_M(M) == int(N):
        print(M)
        exit()
    M = str(int(M)+1)

print(0)