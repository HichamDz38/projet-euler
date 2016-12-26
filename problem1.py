m35=[]
i=3
while i<1000:
    m35.append(i)
    i=i+3
l=5
while l<1000:
    if l not in m35:
        m35.append(l)
    l=l+5
d=sum(m35)
print d
