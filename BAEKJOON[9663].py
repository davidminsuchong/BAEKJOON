#9663

N = int(input())

board = dict()
for i in range(N*N):
    board[i]==[1]

count = 0

for i in range(N*N):
    board[i]=0
    