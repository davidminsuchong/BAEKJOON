#1427

N = input()
A = []
B = ""
for i in range(len(N)):
    A.append(int(N[i]))

A.sort()

for i in range(len(A)):
    B += str(A[len(A)-i-1])

print(B)