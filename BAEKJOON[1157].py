#1157

A = input()
A = A.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
count = [0]*26

for i in A:
    for j in range(26):
        if i==alphabet[j]:
            count[j]+=1

max_num = max(count)
check_same=0

for i in range(26):
    if count[i] == max_num:
        P = alphabet[i]
        check_same += 1

if check_same != 1:
    print("?")
else:
    print(P.upper())