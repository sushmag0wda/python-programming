'''
Leap year rules (important 💡)

A year is a leap year if:

It is divisible by 4

BUT if it is a century year (divisible by 100), then
➜ it must also be divisible by 400

#leap year or not:
#WAP to check weather a given year is a leap year or not
                               year
                                |
            ------------------------------------------
            |                                        |                                                 
      non-century year                         century year
            |                                        |
--------------------------                  ----------------------
|                        |                  |                    |
leap                   non-leap           leap                non-leap
'''
#---------------------------------------------------------------
#brute force approach
y=int(input("enter a year"))
if(y%100!=0):
    if(y%4==0):
        print("its a leap year")
    else:
        print("its not a leap year")
elif(y%400==0):
    print("its a leap year")
else:
    print("its not a leap year")
#----------------------------------------------------------------------------------------------------------
#using logical operators
y=int(input("enter a year"))
if ((y%100!=0 and y%4==0) or y%400==0):
    print("its a leap year ")
else:
    print("its not a leap year")
#-------------------------------------------------------------------------------------------------------------

#using functions (leap year)
def isLeap(y):
     return((y%100!=0 and y%4==0) or y%400==0)     

y=int(input("enter a year"))
flag=isLeap(y)
if flag:
    print("its a leap year ")
else:
    print("its not a leap year")

#to print the leap year and non leap year in a range of years
def isLeap(y):
     return((y%100!=0 and y%4==0) or y%400==0)  

start=int(input("enter the starting year value "))
end=int(input("enter the ending year value "))
if start>end:
    print("invalid input")
else:
    i=start
    print("leap years are: ")
    for i in range(start,end+1):
        flag=isLeap(i)
        if flag:
            print(i,end=" ")
    print("\nNon leap years are")
    for i in range(start,end+1):
        flag=isLeap(i)
        if not flag:
            print(i,end=" ")
#-------------------------------------------------------------------------------------------------------------
