#1316

def group(A):
    used=[0]
    old_streak = A[0]
    for i in A:
        if i != old_streak:
            used.append(old_streak)
            old_streak = i
            for j in used:
                if i == j:
                    return 0
    return 1



N = int(input())
count = 0

for i in range(N):
    string = input()
    count += group(string)

print(count)