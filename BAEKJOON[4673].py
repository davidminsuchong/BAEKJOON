#4673

def d(n):
    return int(n-9*(n//10000)-9*(n//1000)-9*(n//100)+n//10+n%10)

A = list(range(1,10001))

for i in range(1,10001):
    if d(i) <= 10000:
        A[d(i)-1] = 0

for i in A:
    if i != 0:
        print(i)