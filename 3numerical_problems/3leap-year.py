#-------------------------------------------------------------------------------------------------------
'''
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

'''
steps
1)identify the major logic
2)include the function declaration and within it paste the major logic
3)analyse the I/P required by the function to start with logic
4)design the o/p statement
5)call the function by passing the value to the i/p parameter if any
6)reuse the o/p of the function by holding it in a variable if any
'''
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
