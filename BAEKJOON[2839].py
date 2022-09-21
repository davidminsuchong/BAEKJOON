#2839

N = int(input())

count = N//5
N = N%5

while True:
    if N%3 == 0:
        print(count + N//3)
        break
    else:
        count -= 1
        N += 5
    if count == -1:
        print(-1)
        break