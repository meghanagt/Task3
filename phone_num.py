import re
while True:
    n =input("Enter phone num")
    if (len(n)==10 and n.isdigit()):
        output=re.findall(r"^[789]\d{9}$",n)
        if(len(output)==1):
            break
        


            
       
