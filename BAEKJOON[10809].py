#10809

S = input()
Alphabet = "abcdefghijklmnopqrstuvwxyz"
pos=[-1]*26

for i in range(26):
    for j in range(len(S)):
        if S[j]==Alphabet[i] and pos[i]==-1:
            pos[i]=j

print(*pos,sep=" ")