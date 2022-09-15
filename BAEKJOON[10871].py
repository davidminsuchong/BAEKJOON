#10871
import sys

N,X = map(int,sys.stdin.readline().split())
S = list(input().split())
string=''

for i in range(N):
    if int(S[i])<X:
        string+=S[i]+" "

print(string)