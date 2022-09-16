#3052

count = 1
A = [0]*42
for i in range(10):
    a = int(input())%42
    A[a]=1
print(sum(A))