#5597

A = []
for i in range(30):
    A.append(i+1)

for i in range(28):
    A.remove(int(input()))

A.sort()

for i in A:
    print(i)