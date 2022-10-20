#11478

S = input()
A = set()
length = len(S)

for i in range(length):
    for j in range(length-i):
        A.add(S[j:j+1+i])

print(len(A))