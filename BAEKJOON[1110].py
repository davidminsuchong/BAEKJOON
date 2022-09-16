#1110

N = int(input())
count = 0
n = N

while True:
    count += 1
    if n<10:
        number = n*10+n
    else:
        number = (n//10 + n%10)%10 + (n%10)*10
    if number == N:
        print(count)
        break
    else:
        n = number