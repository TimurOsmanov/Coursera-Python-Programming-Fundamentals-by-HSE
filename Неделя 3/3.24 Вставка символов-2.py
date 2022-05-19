s = input()
i = 0
sMod = str()
while i < (len(s)):
    sMod = sMod + s[i]
    i += 1
    if i < len(s):
        sMod = sMod + '*'
print(sMod)
