#2525

H,M = map(int,input().split())
m = int(input())

if M+m<60:
    print(H,M+m)
else:
    H += (M+m)//60
    M = (M+m)%60
    if H<=23:
        print(H,M)
    else:
        print(H-24,M)