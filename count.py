a=[11,45,8,11,23,45,23,45,89]
d=dict()
for c in a:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1
print("Original list",a)
print("Print count of each item",d)
