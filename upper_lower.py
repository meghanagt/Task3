def case(s):
    d={"Uppercase":0,"Lowercase":0}
    for c in s:
        if c.isupper():
            d["Uppercase"]+=1
        elif c.islower():
            d["Lowercase"]+=1
        else:
            pass
    print("No of upper case characters:",d["Uppercase"])
    print("No of lower case characters:",d["Lowercase"])

s=input()
case(s)
