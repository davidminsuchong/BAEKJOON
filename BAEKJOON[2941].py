#2941

string = input()
count = 0

for i in range(len(string)):
    if string[i]=="=" or string[i]=="-":
        count -= 1
        if i-2 >= 0 and string[i-2]=="d" and string[i-1] == "z":
            count-=1
    if i!=0 and string[i]=="j":
        if string[i-1]=="l" or string[i-1]=="n":
            count -= 1
    count += 1

print(count)