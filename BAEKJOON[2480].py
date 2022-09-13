#2480

A,B,C = map(int,input().split())

if A==B and B==C:
    print(10000+A*1000)
elif A==B or B==C:
    print(1000+B*100)
elif not(A==C):
    print(max(A,B,C)*100)
else:
    print(1000+A*100)

