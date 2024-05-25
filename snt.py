def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)
def nd(a,n):
    if gcd(a,n)!=1:
        return "Error!"
    x = [0,1]
    r = [n,a]
    i = 2
    while r[i-1]!=1:
        r.append(r[i-2]%r[i-1])
        q = r[i-2]//r[i-1]
        x.append(x[i-2]-q*x[i-1])
        i += 1
    if(x[i-1]<0):
        return x[i-1]+n 
    return x[i-1]
def somu(a,k,n):
    f = 1
    bi = ""
    while k!=0:
        bi = str(k%2) + bi
        k = k//2
    for i in range(0,len(bi)):
        f = f*f % n
        if bi[i]=='1':
            f = f*a % n
    return f
print(somu(2,4,14))