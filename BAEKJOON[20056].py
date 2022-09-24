#20056

N,M,K = map(int,input().split())
coor = []

for i in range(M):
    r,c,m,s,d = list(map(int,input().split()))
    coor.append([(r+N-1)%N,(c+N-1)%N,m,s,d])

for i in range(K):
    count = []
    for j in range(N):
        count.append([0]*N)
    multi = []
    M = len(coor)

    for j in range(M):
        if coor[j][4]==0:
            coor[j][0] = (coor[j][0]+2*N-coor[j][3])%N
        elif coor[j][4]==1:
            coor[j][0] = (coor[j][0]+2*N-coor[j][3])%N
            coor[j][1] = (coor[j][1]+coor[j][3])%N
        elif coor[j][4]==2:
            coor[j][1] = (coor[j][1]+coor[j][3])%N
        elif coor[j][4]==3:
            coor[j][0] = (coor[j][0]+coor[j][3])%N
            coor[j][1] = (coor[j][1]+coor[j][3])%N
        elif coor[j][4]==4:
            coor[j][0] = (coor[j][0]+coor[j][3])%N
        elif coor[j][4]==5:
            coor[j][0] = (coor[j][0]+coor[j][3])%N
            coor[j][1] = (coor[j][1]+2*N-coor[j][3])%N
        elif coor[j][4]==6:
            coor[j][1] = (coor[j][1]+2*N-coor[j][3])%N
        elif coor[j][4]==7:
            coor[j][0] = (coor[j][0]+2*N-coor[j][3])%N
            coor[j][1] = (coor[j][1]+2*N-coor[j][3])%N
        
        count[coor[j][0]][coor[j][1]]+=1
        if count[coor[j][0]][coor[j][1]]==2:
            multi.append([coor[j][0],coor[j][1]])

    for j in range(len(multi)):
        A = []
        A = multi[j] + [0,0,0]
        for k in range(count[multi[j][0]][multi[j][1]]):
            for l in range(len(coor)):
                if [coor[l][0],coor[l][1]] == multi[j]:
                    B = coor.pop(l)
                    A[2]+=B[2]
                    A[3]+=B[3]
                    A[4]+=B[4]%2
                    break
            
        A[2] = int(A[2]//5)
        if A[2]==0:
            continue
            
        A[3]=int(A[3]//count[multi[j][0]][multi[j][1]])
            
        if A[4]==0 or A[4]==count[multi[j][0]][multi[j][1]]:
            for m in range(4):
                coor.append(A[0:4]+[m*2])
        else:
            for m in range(4):
                coor.append(A[0:4]+[m*2+1])
    if len(coor) == 0:
        print(0)
        exit()

m = 0
for i in range(len(coor)):
    m += coor[i][2]
print(m)