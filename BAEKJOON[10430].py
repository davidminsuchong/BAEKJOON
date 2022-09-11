#10430

A,B,C = map(int,input().split())
D = [(A+B)%C,((A%C)+(B%C))%C,(A*B)%C,((A%C)*(B%C))%C]
for i in D:
    print(i)