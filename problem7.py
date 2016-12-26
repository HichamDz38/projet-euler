i=2
g=[2]
p=3
while len(g)<10001:
    t='true'
    for j in g:
        if p%j==0:
            t='false'
            break
    if t=='true':
        g.append(p)
    p+=1
print g[10000]
