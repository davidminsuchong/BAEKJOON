#2292

import math

N = int(input())
x = (N-1)/6
n = math.ceil((-1+math.sqrt(1+8*x))/2 + 1)

print(int(n))