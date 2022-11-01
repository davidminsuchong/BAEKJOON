#2004

n,m = map(int,input().split())
factorial1 = 1
count1 = 0
factorial2 = 1
count2 = 0


for i in range(n-m+1,n+1):
    factorial1 = factorial1*i
    while factorial1%10==0:
        factorial1 = factorial1//10
        count1+=1

for i in range(1,m):
    factorial2 = factorial2*i
    while factorial2%10==0:
        factorial2 = factorial2//10
        count2+=1

print(count1-count2)