a=[87,45,41,65,94,41,99,94]
res=[]
for i in a:
    if i not in res:
        res.append(i)
print("unique items",res)
print("tuple",tuple(res))
print("min:",min(res))
print("max:",max(res))
