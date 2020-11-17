from fractions import Fraction
m=int(input(" introduceti numaratorul primei fractii m="))
l=int(input("introduceti numaratorul la a doua fractie l="))
n=int(input("introduceti numitorul primei fractii n="))
x=int(input("introduceti numitorul la a doua fractie x="))
print("suma este:", Fraction(m,n)+Fraction(l,x))
print("produsul este:", Fraction(m,n)*Fraction(l,x))