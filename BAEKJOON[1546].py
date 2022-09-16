#1546

N = int(input())
A = list(map(int,input().split()))

print(sum(A)/max(A)*100/N)