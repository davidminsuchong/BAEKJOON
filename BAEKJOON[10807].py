#10807

N = int(input())
A = list(map(int,input().split()))
B = int(input())
count = 0

for i in A:
    if i == B:
        count += 1

print(count)