from math import log
m=int(input("introduceti un numar:"))
n=int(input("introduceti un numar n mai mare ca m:"))
i=log(m,n)
l=int(i)
if i-l==0:
    print("n este puterea lui m")
else:
    print("n nu este putere lui m")    