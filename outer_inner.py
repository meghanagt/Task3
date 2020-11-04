def outerfun(a,b):
    def innerfun(a,b):
        return a+b
    add=innerfun(a,b)
    return add+5
result=outerfun(5,10)
print(result)
