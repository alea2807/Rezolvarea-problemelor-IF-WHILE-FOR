v=int(input("introduceti virsta lui mihai:"))
c=1
if v<20:
    for i in range(1, v+1 ):
        if i==1:
            c+=2
        else:
            c=(c*2)+i
print("la aceasta virsta de " ,v, "ani mihai a primit " ,c, "dolari") 
if v==6:
    print("la virsta de 6 ani cadoul lui mihai depaseste suma de 100 de dolari")    
