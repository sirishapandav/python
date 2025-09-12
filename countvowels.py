def count_vowels(s):
    v='a,e,i,o,u,A,E,I,O,U'
    c=0
    for char in s:
        if char in v:
            c+=1
    return c
s="Sridevi"
print(count_vowels(s))        