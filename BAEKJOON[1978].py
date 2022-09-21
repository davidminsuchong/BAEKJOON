#1978

N = int(input())
numbers = list(map(int,input().split()))
count = 0

for i in range(N):
    for j in range(numbers[i]):
            if j+2 == numbers[i]:
                count += 1
                break
            if numbers[i]%(j+2) == 0 or numbers[i]== 1:
                break

print(count)