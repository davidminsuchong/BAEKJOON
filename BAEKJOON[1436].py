#1436

N = int(input())

count = 0
number = "665"

while True:
    number = str(int(number)+1)
    if number.find("666") >= 0:
        count += 1
        if count == N:
            print(number)
            break