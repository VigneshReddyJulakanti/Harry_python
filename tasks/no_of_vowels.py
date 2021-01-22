
a=["fheb","abcaa"]
res=0
for i in a:
    for e in i:
        if e in "aeiou":
        # if e in ["a","e","i","o","u"]:
        # if e in ("a","e","i","o","u"):
        # if e==("a" or "e" or "i" or "o" or "u"):
            res+=1
print(res)
