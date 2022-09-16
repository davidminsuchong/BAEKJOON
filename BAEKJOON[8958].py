#8958

T = int(input())
A = []

for i in range(T):
    score = 0
    count = 0
    a = input()
    for j in range(len(a)):
        if a[j]=="X":
            count = 0
        else:
            count += 1
            score += count
    A.append(score)
    
for i in range(len(A)):
    print(A[i])