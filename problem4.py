a=999
c=[]
while a>0:
    b=999
    while b>0:
        p=a*b
        if str(p)==str(p)[::-1]:
            c.append(p)
        b-=1
    a-=1
print max(c)
