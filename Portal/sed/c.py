fr=open("vprob.txt","w")
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

	t8=float((math.log(x,2.7183)-mean)/(variance * 1.414))
	t9 = 0.5*(1 + math.erf(t8))
	if t9==1:
		return 0
	t10=float(1.0*t7/(1-t9))

	return t10

def integration(lower,higher,mean,variance,magns):	
	delta = 0.1
	sum = 0
	while (lower <= higher):
		temp1 = function(lower,mean,variance)
		temp2 = function(lower + delta,mean,variance)
		if temp1 >= 0.02 or temp2 >= 0.02:
			print temp1
			if magns not in nuclear:
				nuclear.append(magns)
		if temp1 >= 0.05 or temp2 >= 0.05:
			print temp1
			if magns not in dams:
				dams.append(magns)
		if temp1 >= 0.1 or temp2 >= 0.1:
			print temp1
			if magns not in bbuildings:
				bbuildings.append(magns)
		if temp1 >= 0.15 or temp2 >= 0.15:
			print temp1
			if magns not in nbuildings:
				nbuildings.append(magns)
		fr.write(str(temp1)+"\n"+str(magns))
		darea = delta * (temp1+temp2)/2.0
		sum += darea
		lower += delta
	return sum

f=open("vadodara.txt","r")
f1=open("vadodarares.txt","w")
gre=f.readlines()
magns=0
count=0
for line in gre:
	count=count+1
	if count%6==0:
		magns=magns+1
	a=line.split(' ')
	if "new" in a[0]:
		f1.write("new\n")
	elif "->"==a[0]:
		final=[]
		a_size=len(a)
		sed=int(a[a_size-2])
		for i in range(1,a_size-2):
			temp=int(a[i+1])-int(a[i])
			final.append(temp)
		if len(final)>0:
			sed=2014-sed
			means=0
			s=mean(final)
			s=logcalc(s[0],s[1])
			if s[1]==0:
				s[1]=s[1]+0.2
			variances=s[1]
			means=s[0]
			if variances==0:
				variances=variances+0.2				
			ans=integration(sed,sed+100,means,variances,magns)
			ans=int(ans)+1
			f1.write(str(ans))
			f1.write("\n")
		else:
			if a[1]=='0':
				f1.write("0\n")
			else:
				f1.write("1\n")
print nuclear
print dams
print bbuildings
print nbuildings
