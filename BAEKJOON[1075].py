#1075

N = input()
F = input()
n = int(N)
f = int(F)
a = len(N)
b = n%f
c = f-b
N = str(int(N[a-2:])+c)

while int(N)>=0:
    N = str(int(N)-f)

N = str(int(N)+f)

if len(N)==2:
    print(N)
else:
    print("0"+N)