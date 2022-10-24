#2587

A = []
average = 0
for i in range(5):
    A.append(int(input()))
    average += A[i]//5

A.sort()

print(average)
print(A[2])