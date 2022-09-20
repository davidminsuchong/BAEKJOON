#10250

import math

T = int(input())
A = []

for i in range(T):
    A.append(list(map(int,input().split())))

for i in A:
    flour = i[2]%i[0]
    if flour == 0:
        flour = i[0]
    number = math.ceil(i[2]/i[0])
    if number<10:
        number = "0"+str(number)
    print(str(flour)+str(number))