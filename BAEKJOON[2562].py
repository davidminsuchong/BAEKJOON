#2562

big = 0
count = 0

for i in range(1,10):
    a = int(input())
    if a > big:
        big = a
        count = i

print(big)
print(count)