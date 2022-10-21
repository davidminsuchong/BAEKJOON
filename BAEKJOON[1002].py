#1002

T = int(input())

for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    l = (x1-x2)**2 + (y1-y2)**2
    R1 = (r1+r2)**2
    R2 = (r1-r2)**2
    if l==0 and r1==r2:
        print(-1)
    elif R1==l or R2==l:
        print(1)
    elif R1<l or R2>l:
        print(0)
    else:
        print(2)