#9184

while True:
    a,b,c = map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    if a>20 or b>20 or c>20:
        a=20;b=20;c=20
    total = 0
    