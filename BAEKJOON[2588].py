#2588

A = int(input())
B = int(input())

C = A*(B%10)
D = A*(B//10-(B//100)*10)
E = A*(B//100-(B//1000)*10)
F = A*B

for i in [C,D,E,F]:
    print(i)