#14888

import math

N = int(input())
A = list(map(int,input().split()))

old_num = [list(map(int,input().split()))]
old_Answer = [A[0]]

for i in range(1,N):
    new_num = []
    new_Answer = []
    for j in range(len(old_Answer)):
        if old_num[j][0]!=0:
            new_Answer.append(old_Answer[j]+A[i])
            new_num.append([old_num[j][0]-1,old_num[j][1],old_num[j][2],old_num[j][3]])
        if old_num[j][1]!=0:
            new_Answer.append(old_Answer[j]-A[i])
            new_num.append([old_num[j][0],old_num[j][1]-1,old_num[j][2],old_num[j][3]])
        if old_num[j][2]!=0:
            new_Answer.append(old_Answer[j]*A[i])
            new_num.append([old_num[j][0],old_num[j][1],old_num[j][2]-1,old_num[j][3]])
        if old_num[j][3]!=0:
            new_Answer.append(int(abs(old_Answer[j])//A[i]*math.copysign(1,old_Answer[j])))
            new_num.append([old_num[j][0],old_num[j][1],old_num[j][2],old_num[j][3]-1])
    old_num = new_num.copy()
    old_Answer = new_Answer.copy()
print(max(old_Answer))
print(min(old_Answer))