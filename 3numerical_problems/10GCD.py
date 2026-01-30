#GCD /HCF:
'''-every number will have its factors only from 1 to the number itself
-As GCD means finding the common factor that completely divides both the numbers,therefore 
the GCD of two numbers will always be less than or equal to the smaller number.
eg:
n1=15 n2=9
==>GCD of 15,9 will lie between 1 to 9
GCD will always have 1 as a factor
'''
#WAP to print the gcd of a given number using function
def gcd(n1,n2):
    gcd=1
    lower=n2
    if n2>n1:
        lower=n1
    for i in range(2,(lower+1)):
        if n1%i==0  and n2%i==0:
            gcd = i
    return gcd

n1=int(input("enter a first number"))
n2=int(input("enter a second number"))
res=gcd(n1,n2)
print("GCD = ",res)

#WAP to check if the numbers are co primes
def gcd(n1,n2):
    gcd=1
    lower=n2
    if n2>n1:
        lower=n1
    for i in range(2,(lower+1)):
        if n1%i==0  and n2%i==0:
            gcd = i
    return gcd==1

n1=int(input("enter a first number"))
n2=int(input("enter a second number"))
res=gcd(n1,n2)
if res:
    print("co primes")
else:
    print("not co primes")