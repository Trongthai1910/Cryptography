from random import randint
import math

def snt(a):
	for i in range(2,int(math.sqrt(a))+1):
		if a%i == 0:
			return False
	return a>1
def gcd(a,b):
	if a%b == 0:
		return b
	return gcd(b,a%b)
def nd(a,n):
	r = [n,a]
	x = [0,1]
	i = 2
	while (r[i-1]!=1):
		r.append(r[i-2]%r[i-1])
		q = r[i-2]//r[i-1]
		x.append(x[i-2] - q*x[i-1])
		i += 1
	if(x[i-1]<0):
		return x[i-1]+n
	return x[i-1]
def somu(a,k,n):
	f = 1;
	bi = ""
	while (k!=0):
		bi = str(k%2)+bi
		k = k//2
	for i in range(0,len(bi)):
		f = f*f % n
		if bi[i] == '1':
			f = f*a % n 
	return f
#RSA
#tìm p,q
p = randint(0,1000)
while snt(p)==False:
	p = randint(0,1000)
q = randint(0,1000)
while snt(q)==False or p==q:
	q = randint(0,1000)

print("p = "+str(p)+", q = "+str(q))
#tính n, phi
n = p*q 
phi = (p-1)*(q-1)
print("n = "+str(n)+", phi = "+str(phi))
#tìm e,d
e = randint(0,1000)
while e==q or e==p or gcd(e,phi)!=1 or e>phi:
	e = randint(0,1000)

d = nd(e,phi)
print("e = "+str(e)+", d = "+str(d))

# m = int(input("Nhập bản rõ m: "))
# print("Bản mã hóa: "+str(somu(m,e,n)))
# print("Bản giải mã: "+str(somu(somu(m,e,n),d,n)))

text = input("Nhập text cần mã hóa: ")
text = list(text)
for i in range(0,len(text)):
	text[i] = somu(ord(text[i]),e,n)
print(text)
for i in range(0,len(text)):
	text[i] = chr(somu(text[i],d,n))
print(''.join(text))


