#factors of a number
'''
    -A val is said to be a factor of a number only when the val is able to completely reduce the number to 0.
    -All the factors of a number will always lie between 1 to the number itself.
    -The least of a number is 1.
    '''
#normal code
n=int(input("enter a number"))
i=1
for i in range(i,n+1):
    if n%i==0: #check if the number is divisible by i
        print(i,end=" ")

#using function
def factors(n):
    i=1
    count=0
    for i in range(i,n+1):
        if n%i==0:
            print(i,end=" ")  
        
n=int(input("enter a number"))
factors(n)

#WAP to print all the factors and display the count of number of factors of a given number
def factors(n):
    i=1
    count=0
    for i in range(i,n+1):
        if n%i==0:
            print(i,end=" ")  
            count+=1
    return count
        
n=int(input("enter a number"))
c=factors(n)

print(f"\nnum of factors is {c}")

#WAP to print all the factors and display the count of number
# of factors of a given number and also the number of cycles taken to find the factors
def factors(n):
    i=1
    count=0
    cycles=0
    for i in range(i,n+1):
        if n%i==0:
            print(i,end=" ")  
            count+=1
        cycles+=1
    return count,cycles
        
n=int(input("enter a number"))
c,cy=factors(n)

print(f"\nnum of factors is {c}")
print(f"num of cycles is {cy}")

#optimised code
#As this program is taking n cycles we are optimizing the code
'''
All the factors of a number can be listed within the direct 
square root or the lower 
nearest square root of the number.
'''
#Square root of a number is the number which when 
# multiplied by itself gives the original number.
'''example :
1 is the square root of 1 because 1*1=1
2 is the square root of 4 because 2*2=4
3 is the square root of 9 because 3*3=9
4 is the square root of 16 because 4*4=16
5 is the square root of 25 because 5*5=25
basic idea
lets take an example 
n=6
then lets take i=2
then 2*(6//2)= 6
so 2 is a factor of 6 and 3 is also a factor of 6

now lets consider n=15
so to set up the i value we have to start from 1
and the end will be nearest square root of the number
so the nearest square is 9 and its square root is 3
therefore i ranges from 1 to 3
so if we start from i=1
then we have to check if 
1*1<=15
if yes then we have to check if 1*(15//1)=15
it is true
so 1 is a factor of 15 and 15//1=15 is also a   
'''
#factors using optimised code
def factors(n):
    i=1
    cycles=0
    count=0 
    while i*i<=n:
        if n%i==0:
            print(i,end=" ")
            count+=1
            if(i!=(n//i)):
                print((n//i),end=" ")
                count+=1
        i=i+1
        cycles+=1
    return count,cycles
n=int(input("enter a number"))
c,cy=factors(n)
print(f"\nnumber of factors {c}")
print(f"number of cycles {cy}")
