a=int(input("introduceti virsta lui mihai a="))
c=1
if a<20:
    for i in range(1, a+1 ):
        if i==1:
            c+=2
        else:
            c=(c*2)+i
print("la aceasta virsta de " ,a, "ani mihai a primit " ,c, "dolari") 
print("la virsta de 6 ani cadoul lui mihai depaseste suma de 100 de dolari")    