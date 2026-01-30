#conditional statements

#if,if else,elif,nested if
#----------------------------------------------------------------------------------------------

#if condition
age=int(input("enter your age "))
if age>18:
    print("you can vote")
#----------------------------------------------------------------------------------------------
#if else condition
num=int(input("enter a number"))
if num%2==0:
    print(f"{num} even number")
else:
    print(num,"is odd")
print("program executed")
#note: fators,divisibilty,reductions--->modulus

#----------------------------------------------------------------------------------------------
#elif 
#write a program to print the largest value among the three given number
a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if a>b and a>c:
    print(a,"is largest")
elif b>a and b>c:
    print(b,"is largest")
else:
    print(c,"is largest")
#----------------------------------------------------------------------------------------------
#nested if
#write a program to check whether the given number is positive,negative or zero
num=int(input("enter a number"))
if num>=0:
    if num==0:
        print("number is zero")
    else:
        print("number is positive")
else:
    print("number is negative")
#----------------------------------------------------------------------------------------------
#reducing the number of line in code is called code optimization
a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if b<a>c:
    print(a,"is largest")
elif c<b>a:
    print(b,"is largest")
else:
    print(c,"is largest")