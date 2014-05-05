fr1=open("suratnuclear.txt","w")
fr2=open("suratdams.txt","w")
fr3=open("suratnbuildings.txt","w")
fr4=open("suratbbuildings.txt","w")
fr5=open("suratx.txt","w")
fr6=open("suraty.txt","w")
import math
dams=[]
nuclear=[]
nbuildings=[]
bbuildings=[]
def mean(x):
	avg=0
	for i in range(0,len(x)):
		if x[i]==0:
			x[i]=x[i]+0.25
		avg=avg+float(x[i])
	mean=float(avg)/(1.0*len(x))
	var=0
	for i in range(0,len(x)):
		temp=1.0 * (float(x[i])-mean) * (float(x[i])-mean)
		var=var+temp
	variance=float(var)/(1.0 * len(x))
	s=[]
	s.append(mean)
	s.append(variance)
	return s

def logcalc(m,v):
	t1=m**2
	t2=v+t1
	t3=1.0*float(t1)/float(math.sqrt(t2))
	mean=math.log(t3,2.7183)
	t4=1.0*((1.0*v)/(1.0*t1))
	t5=1+t4
	variance=math.sqrt(math.log(t5,2.7183))
	arrys=[]
	arrys.append(mean)
	arrys.append(variance)
	return arrys

def function(x,mean,variance):
	variance=math.sqrt(variance)
	t1=1.0/(x * variance * 2.506 * 1.0)
	t2=math.log(x,2.7183)
	t3=(t2-mean)*(t2-mean)*1.0
	t4=2.0*variance*variance
	t5=(-1.0 * t3)/(1.0 * t4)
	t6=(2.7183)**t5
	t7=1.0 * t1 * t6
	t7=round(t7,6)
	fr5.write(str(x)+'\n')
	fr6.write(str(t7)+'\n')
	t8=float((math.log(x,2.7183)-mean)/(variance * 1.414))
	t9 = 0.5*(1 + math.erf(t8))
	if t9==1:
		return 0
	t10=float(1.0*t7/(1-t9))
	return t10

def integration(lower,higher,mean,variance,magns):	
	delta = 0.1
	sum = 0
	while (lower + delta <= higher):
		temp1 = function(lower,mean,variance)
		temp2 = function(lower + delta,mean,variance)
		if temp1 >= 0.02 or temp2 >= 0.02:
			if magns not in nuclear:
				nuclear.append(magns)
		if temp1 >= 0.05 or temp2 >= 0.05:
			if magns not in dams:
				dams.append(magns)
		if temp1 >= 0.1 or temp2 >= 0.1:
			if magns not in bbuildings:
				bbuildings.append(magns)
		if temp1 >= 0.15 or temp2 >= 0.15:
			if magns not in nbuildings:
				nbuildings.append(magns)
		darea = delta * (temp1+temp2)/2.0
		sum += darea
		lower += delta
	return sum

f=open("surat.txt","r")
gre=f.readlines()
final=[]
f1=iter(gre)
j=0
for line in f1:
	j+=1
	if(j==9):
		break 
	a=line.split(' ')
	if "new" in a[0]:
		final1=[]
		final=[]
	for i in range(5):
		line=next(f1)
		a=line.split(' ')
		t=len(a)-1
		if "->"==a[0]:
			for i in range(1,len(a)-1):
				temp=int(a[i])
				if temp!=0:
					final1.append(temp)
	
	final1.sort()
	a_size=len(final1)
	if a_size>=1:
		sed=int(final1[a_size-1])
	for i in range(1,len(final1)):
		temp=final1[i]-final1[i-1]
		final.append(temp)

		
	if len(final)>=1:
		sed=2014-sed
		sed=1
		means=0
		s=mean(final)
		s=logcalc(s[0],s[1])
		if s[1]==0:
			s[1]=s[1]+0.2
		variances=s[1]
		means=s[0]
		if variances==0:
			variances=variances+0.2				
		ans=integration(sed,sed+100,means,variances,j)
		ans=int(ans)+1
		print ans
		
	else:
		if len(final1)==0:
			print '0'
		else:
			print '1'
for i in dams:
	if i==1:
		fr1.write('3-3.5\n')
	if i==2:
		fr1.write('3.5-4\n')
	if i==3:
		fr1.write('4-4.5\n')
	if i==4:
		fr1.write('4.5-5\n')
	if i==5:
		fr1.write('5-5.5\n')
	if i==6:
		fr1.write('5.5-6\n')
	if i==7:
		fr1.write('6-6.5\n')
	if i==8:
		fr1.write('6.5-7\n')
for i in nuclear:
	if i==1:
		fr2.write('3-3.5\n')
	if i==2:
		fr2.write('3.5-4\n')
	if i==3:
		fr2.write('4-4.5\n')
	if i==4:
		fr2.write('4.5-5\n')
	if i==5:
		fr2.write('5-5.5\n')
	if i==6:
		fr2.write('5.5-6\n')
	if i==7:
		fr2.write('6-6.5\n')
	if i==8:
		fr2.write('6.5-7\n')
for i in nbuildings:
	if i==1:
		fr3.write('3-3.5\n')
	if i==2:
		fr3.write('3.5-4\n')
	if i==3:
		fr3.write('4-4.5\n')
	if i==4:
		fr3.write('4.5-5\n')
	if i==5:
		fr3.write('5-5.5\n')
	if i==6:
		fr3.write('5.5-6\n')
	if i==7:
		fr3.write('6-6.5\n')
	if i==8:
		fr3.write('6.5-7\n')
for i in bbuildings:
	if i==1:
		fr4.write('3-3.5\n')
	if i==2:
		fr4.write('3.5-4\n')
	if i==3:
		fr4.write('4-4.5\n')
	if i==4:
		fr4.write('4.5-5\n')
	if i==5:
		fr4.write('5-5.5\n')
	if i==6:
		fr4.write('5.5-6\n')
	if i==7:
		fr4.write('6-6.5\n')
	if i==8:
		fr4.write('6.5-7\n')
