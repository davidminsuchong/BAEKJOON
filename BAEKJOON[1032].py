#1032

N = int(input())
A = set()

if N==1:
    a = input()
else:
    a = input()
    n = len(a)
    for i in range(N-1):
        b = input()
        for j in range(n):
            if a[j]!=b[j]:
                a=a[:j]+"?"+a[j+1:]
print(a)