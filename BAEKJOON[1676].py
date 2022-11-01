#1676

N = int(input())
count = 0
factorial = 1

for i in range(1,N+1):
    factorial = factorial*i
    while factorial%10==0:
        factorial = factorial//10
        count += 1

print(count)