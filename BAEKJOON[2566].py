#2566

A = []
max = -1
num = 0
for i in range(9):
    A = A + list(map(int,input().split()))

for i in range(len(A)):
    if A[i]>max:
        max=A[i]
        num = i

print(max)
print(num//9+1,num%9+1)