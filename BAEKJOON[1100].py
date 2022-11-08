#1100

count = 0
for i in range(8):
    A = input()
    if i%2==0:
        for j in range(4):
            if A[j*2]=="F":
                count += 1
    else:
        for j in range(4):
            if A[j*2+1]=="F":
                count += 1

print(count)