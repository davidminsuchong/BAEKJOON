#9663

def update(newboard,i,N):
    k = i
    while k<N*N:
        newboard[k]=0
        k = k+N
    k = i
    while k<N*N and (k+1)%N!=0:
        newboard[k]=0
        k = k+N+1
    k = i
    while k<N*N and k%N!=0:
        newboard[k]=0
        k = k+N-1
    k = i
    while k>-1:
        newboard[k]=0
        k = k-N
    k = i
    while k>-1 and k%N!=0:
        newboard[k]=0
        k = k-N-1
    k = i
    while k>-1 and (k+1)%N!=0:
        newboard[k]=0
        k = k-N+1
    k = i//N
    for j in range(N):
        newboard[k+j]=0
    return newboard

N = int(input())

newboard = []

for i in range(N*N):
    A = []+[1]*N*N
    newboard.append(update(A,i,N))

for i in range(N):
    board = []
    for j in range(len(newboard)):
        for k in range(N*N):
            if newboard[j][k]==1:
                board0 = [] + newboard[j]
                board1 = update(board0,k,N)
                if sum(board1)>=N-i-1:
                    board.append(board1)
    newboard = [] + board

print(len(newboard))