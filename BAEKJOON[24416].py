#24416

def fib(n):
    f = [1,1]
    i = 2
    while i<n:
        f.append(f[i-2]+f[i-1])
        i+=1
    return (f[n-1])

n = int(input())

print(fib(n),n-2)