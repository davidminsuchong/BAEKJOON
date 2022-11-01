#2004

def count_2(a,total):
    count = 0
    b = 2
    while b<=a:
        count += 1
        b = b*2
    total += 2**(count)-1
    b = int(b/2)
    if a<=1:
        return int(total)
    else:
        return count_2(a-b,total)

def count_5(a,total):
    count = 0
    b = 5
    while b<=a:
        count += 1
        b = b*5
    total1 = 0
    for i in range(count):
        total1 = total1*5+1
    total = total+total1
    b = int(b/5)
    if a<=4:
        return int(total)
    else:
        return count_5(a-b,total)

n,m = map(int,input().split())
count2 = count_2(n,0)-count_2(m,0)-count_2(n-m,0)
count5 = count_5(n,0)-count_5(m,0)-count_5(n-m,0)
print(min(count2,count5))