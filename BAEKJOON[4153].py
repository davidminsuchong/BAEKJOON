#4153

A = []

while True:
    B = list(map(int,input().split()))
    B.sort()
    if B==[0,0,0]:
        break
    if B[2]**2==B[0]**2+B[1]**2:
        A.append("right")
    else:
        A.append("wrong")

for i in A:
    print(i)