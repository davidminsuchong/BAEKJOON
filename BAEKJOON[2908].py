#2908

def flip(A):
    return (A%10)*100 -99*(A//100) + (A//10)*10

A,B = map(int,input().split())

A = flip(A)
B = flip(B)

print(max(A,B))