#prime numbers
'''A prime number is a number that has only two factors, 1 and itself.
- 1 and 0 and negative numbers are not considered as prime numbers.
- The first prime number is 2.'''

#WAp to check if a number is prime or not using function
def isprime(n):
    i=1
    count=0
    while i*i<=n:
        if n%i==0:
            #print(i,end=" ")
            count+=1
            if(i!=(n//i)):
                #print((n//i),end=" ")
                count+=1
        i=i+1
    return count==2
n=int(input("enter a number "))
c=isprime(n)
if c:
    print(f"{n} is a prime number")
else:
    print(f"{n} is a not prime number")

#WAP to print all the prime numbers in a user defined range
def isprime(n):
    i=1
    count=0
    while i*i<=n:
        if n%i==0:
            #print(i,end=" ")
            count+=1
            if(i!=(n//i)):
                #print((n//i),end=" ")
                count+=1
        i=i+1
    return count==2
start=int(input("enter the start number "))
end=int(input("enter the end number "))
print("prime numbers are")
if start > end:
    print("Invalid input")
else:
    for i in range(start,end+1):
        c=isprime(i)
        if c:
            print(i,end=" ")

#WAP to print all the Prime number's and non Prime Number's seperateley present in a user defined range.
def isprime(n):
    i=1
    count=0
    while i*i<=n:
        if n%i==0:
            #print(i,end=" ")
            count+=1
            if(i!=(n//i)):
                #print((n//i),end=" ")
                count+=1
        i=i+1
    return count==2
start=int(input("enter the start number "))
end=int(input("enter the end number "))
print("prime numbers are")
if start > end:
    print("Invalid input")
else:
    for i in range(start,end+1):
        c=isprime(i)
        if c:
            print(i,end=" ")
    print("\nnon prime numbers are")
    for i in range(start,end+1):
        c=isprime(i)
        if not c:
            print(i,end=" ")
#WAP to print first "n" Prime number's.
def isprime(n):
    i=1
    count=0
    while i*i<=n:
        if n%i==0:
            #print(i,end=" ")
            count+=1
            if(i!=(n//i)):
                #print((n//i),end=" ")
                count+=1
        i=i+1
    return count==2
n=int(input("enter the number of prime numbers u want to print "))
series=1
for i in range(series,n+1):
    c=isprime(i)
    if c:
        print(i,end=" ")
        series+=1

#WAP to print first "n" non Prime number's.   
def isprime(n):
    i=1
    count=0
    while i*i<=n:
        if n%i==0:
            #print(i,end=" ")
            count+=1
            if(i!=(n//i)):
                #print((n//i),end=" ")
                count+=1
        i=i+1
    return count==2
n=int(input("enter the number of non prime numbers u want to print "))
series=1
for i in range(series,n+1):
    c=isprime(i)
    if not c:
        print(i,end=" ")
        series+=1   
