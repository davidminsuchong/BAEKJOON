#10870

def Fibonacci(N):
    if N <= 1:
        return N
    else:
        return Fibonacci(N-1)+Fibonacci(N-2)

N = int(input())

print(Fibonacci(N))