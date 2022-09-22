#11653

N = int(input())
A = [2]
A.extend(list(range(3,N+1,2)))

while True:
    if N == 1:
        exit()
    for i in A:
        if N%i==0:
            print(i)
            N = int(N/i)
            break