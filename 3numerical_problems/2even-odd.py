                 
#numerical programs
#WAP to check even or odd without functions
num=int(input("enterr a number"))
if num%2==0:
    print(f"{num}even number")
else:
    print(f"{num}odd number")
#-------------------------------------------------------------------------------------------------------

#WAP to check even or odd using functions
def isEvenOdd(num):
    if num%2==0:
        return True
    else:
        return False
num=int(input("enter a number : "))
flag=isEvenOdd(num)
if flag:
    print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")
#-------------------------------------------------------------------------------------------------------

#optimised code 
def isEvenOdd(num):
    return(num%2==0) #using only one line of code as the function is returning a boolean value

num=int(input("enetr a number : "))
flag=isEvenOdd(num)
if flag:
    print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")
#-------------------------------------------------------------------------------------------------------

#WAP to print all the even numbers in a user defined range
def isEvenOdd(num):
    return(num%2==0)
start=int(input("enter the starting value "))
end=int(input("enter the ending value "))
if start>end:
    print("invalid input")
else:
    i=start
    print("even numbers are: ")
    for i in range(start,end+1):
        flag=isEvenOdd(i)
        if flag:
            print(i,end=" ")
#-------------------------------------------------------------------------------------------------------

#WAP to print all the even numbers and odd in a user defined range
def isEvenOdd(num):
    return(num%2==0)
start=int(input("enter the starting value "))
end=int(input("enter the ending value "))
if start>end:
    print("invalid input")
else:
    i=start
    print("even numbers are: ")
    for i in range(start,end+1):
        flag=isEvenOdd(i)
        if flag:
            print(i,end=" ")
    print("\nodd number are: ")
    for i in range(start,end+1):#just additional loop to print odd numbers
        flag=isEvenOdd(i)
        if flag==False:#(or if not flag)
            print(i,end=" ")
#-------------------------------------------------------------------------------------------------------

#WAP to print first n even numbers
def isEvenOdd(num):
    return(num%2==0)
count=int(input("enter the number of even numbers u want to"))
series=1
while count>0:
    flag=isEvenOdd(series)
    if flag:
        print(series,end=" ")
        count-=1
    series+=1