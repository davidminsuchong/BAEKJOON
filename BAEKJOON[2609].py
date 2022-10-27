#2609

N,M = map(int,input().split())
minmul = 0
maxdiv = 0
A = N
B = M

for i in range(1,1+min(N,M)):
    if N%i==0 and M%i==0:
        maxdiv = i

while True:
    if A == B:
        minmul = A
        break
    if A<B:
        A += N
    else: 
        B += M

print(maxdiv)
print(minmul)