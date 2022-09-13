#25304

X = int(input())
N = int(input())

total = 0
for i in list(range(N)):
    price,number = map(int,input().split())
    total += price*number
if X == total:
    print("Yes")
else:
    print("No")