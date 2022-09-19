#5662

def alp_to_time(A):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if A=="S":
        return 8
    elif A=="V":
        return 9
    elif A=="Y":
        return 10
    elif A=="Z":
        return 10
    for i in range(26):
        if A==alphabet[i]:
            return i//3 + 3

string = input()
time = 0

for i in string:
    time += alp_to_time(i)

print(time)