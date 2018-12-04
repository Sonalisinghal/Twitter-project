df=[tt,tr,et,er]
sentiment=[]
for d in df['polarity']:
	print()
	p=0
	n=0
	r=0
	for i in d:
		if i>0:
			p+=1
		elif i<0:
			n+=1
		else:
			r+=1
	t=p+n+r
	sentiment.append([p,n,r,t])

#sentiment=[tt[p,n,r,t],tr[],et[],er[]]
