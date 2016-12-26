import math
a=2000000
P=[False,False,True,True,False,True,False,True,False,False,False]
S=[(i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0) for i in xrange(11,a)]
P.extend(S)
print len(P)
for i in xrange(2,int(math.sqrt(a))+1):
	if P[i]:
		for j in xrange(i**2,a,i):
			P[j]=False
def g(h):
	if h:return h
P2=[i for i,j in enumerate(P) if j]
print sum(P2)
		
