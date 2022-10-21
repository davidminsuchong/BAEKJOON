#2477

K = int(input())
A = ""
B = []
C = [0,0,0,0]
Answer = 1

for i in range(6):
    a,b = map(int,input().split())
    A += str(a)
    B.append(b)
    C[a-1]+=1

for i in range(4):
    for j in range(6):
        if C[i]==1 and int(A[j])==(i+1):
            Answer = Answer*B[j]

A = A*2
B = B*2

if C[0]==2:
    if C[3]==2:
        S = "1414"
    else:
        S = "3131"
else:
    if C[3]==2:
        S = "4242"
    else:
        S = "2323"

position = A.find(S)

Answer = Answer - B[position+1]*B[position+2]
print(Answer*K)