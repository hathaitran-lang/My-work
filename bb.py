c=[3,5,1,4,9,7,5]
d=list(range(len(c)-1))
ok=False
for x in d:
    ok=False
    for x in d:
        if c[x]>c[x+1]:
            c[x],c[x+1]=c[x+1],c[x]
            ok=True
    if not ok:
            break
print(c)