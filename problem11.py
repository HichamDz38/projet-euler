import numpy as np
T=[]
for i in xrange(0,20):
	T.append(map(int,raw_input().split()))
t=np.array(T)
p=0
a=4
for j in xrange(0,20):
	for i in xrange(0,20-a+2):
		if reduce(lambda x,y:x*y,t[i:i+a,j])>p:
			p=reduce(lambda x,y:x*y,t[i:i+a,j])
		if reduce(lambda x,y:x*y,t[j,i:i+a])>p:
			p=reduce(lambda x,y:x*y,t[j,i:i+a])
for j in xrange(0,20-a+2):
	for i in xrange(0,20-a+2):
		if reduce(lambda x,y:x*y,np.diag(t[i:i+a,j:j+a]))>p:
			p=reduce(lambda x,y:x*y,np.diag(t[i:i+a,j:j+a]))
		if reduce(lambda x,y:x*y,np.diag(np.fliplr(t[j:j+a,i:i+a])))>p:
			p=reduce(lambda x,y:x*y,np.diag(np.fliplr(t[j:j+a,i:i+a])))
print p
