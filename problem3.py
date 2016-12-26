def primefactors(x):
    li=[]
    loop=2
    while loop<=x:
        if x%loop==0:
            x = x /loop
            li.append(loop)
        else:
            loop+=1
    return li

print primefactors(124)
