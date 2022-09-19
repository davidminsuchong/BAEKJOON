#2675

T = int(input())
P = [""]*T

for i in range(T):
    R,S = input().split()
    R = int(R)
    for j in range(len(S)):
        P[i]+=S[j]*R

for i in P:
    print(i)