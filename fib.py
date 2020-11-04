def fab(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fab(a-1)+fab(a-2)
n=int(input("enter n"))
for i in range(n):
    print(fab(i))


    
