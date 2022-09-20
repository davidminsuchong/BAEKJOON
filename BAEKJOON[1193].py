#1193

import math

N = int(input())
Line = int(math.ceil((-1+math.sqrt(1+8*N))/2))
position = int((N)-(Line*(Line-1)/2))

if Line%2==1:
    print(str(Line+1-position)+"/"+str(position))
else:
    print(str(position)+"/"+str(Line+1-position))