#1004

T = int(input())

for i in range(T):
    count = 0
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    for j in range(n):
        cx,cy,r = map(int,input().split())
        l1 = (cx-x1)**2+(cy-y1)**2
        l2 = (cx-x2)**2+(cy-y2)**2
        R = r**2
        if l1 < R and l2 > R:
            count += 1
        elif l1 > R and l2 < R:
            count += 1
    print(count)