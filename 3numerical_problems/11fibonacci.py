#fibonacci series
'''
it is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
The sequence commonly starts with 0 and 1, and the next number is found by adding the two numbers before it.
The beginning of the Fibonacci sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

ex
0+1=1
1+1=2
1+2=3
2+3=5
3+5=8 ....
series = 1,2,3,5,8.....'''
#normal code
n=int(input("enter a number"))
n1=0                    #first value is always 0
n2=1                    #second value is always 1
print("fibonnaci series")
while n>0:
    print(n1,end=" ")
    temp=n1+n2
    n1=n2               #updating n1
    n2=temp             #updaing n2
    n-=1                #decrementing n value which holds the position
#using decrementing while
n=int(input("enter a number"))
n1=0
n2=1
print("fibonnaci series")
i=1                     #using a looping variable to incerement
while i<=n:
    print(n1,end=" ")
    temp=n1+n2
    n1=n2
    n2=temp
    i+=1                #incrementing i 

#using incrementing for loop
n=int(input("enter a number"))
n1=0
n2=1
i=1
print("fibonnaci series")
for i in range(i,n+1):   #looping from 1 to 6
    print(n1,end=" ")
    temp=n1+n2
    n1=n2
    n2=temp
#using decrementing for loop
n=int(input("enter a number"))
n1=0
n2=1
i=1
print("fibonnaci series")
for i in range(n+1,i,-1):    # range is from n to 1 and we are decrementing by 1
    print(n1,end=" ")
    temp=n1+n2
    n1=n2                 #updating n1
    n2=temp              #updating n2
#using functions
def fib(n):
    n1=0
    n2=1
    print("fibonnaci series")
    while n>0:
        print(n1,end=" ")
        temp=n1+n2
        n1=n2
        n2=temp
        n-=1
n=int(input("enter a number"))
fib(n)