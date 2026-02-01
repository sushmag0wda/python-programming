#Patterns
'''
it is the combination of rows and columns
------------ ==> sleeping/horizontal/row
|
|
| ===> standing/vertical/colmuns

we can make this dynamic by taking total number rows to be printed in the pattern
range of n
4<=n<=15
- 2types :
            i)non combinational patterns:right angle triangle,square,rombhus
                                        -direct n value will be taken as I/P
            ii)combinational patterns: K pattern,diamond,buttrfly
                                        -"(2*n)" val will be taken as I/P
-varities:star,hollow,number,alphabetic
-print()-it moves the control to the beginning of the next line
        -if any argument is passed then display it on the output screen then move the contol to the next line
'''
'''
print("hello")
print("WORLD")
print()
print("hi")
print("hello",end="")
print("world")
'''
#note : once u move the control to the next line u can never get it back to the previousline

#1)
print("*")
print("\n-------------------------------------------------------------------------------------------------------------------------")

#2)* column
n=int(input("enter a number"))
for i in range(1,(n+1)): #rows
    print("*")
print("\n-------------------------------------------------------------------------------------------------------------------------")

#3)* row
n=int(input("enter a number"))
for j in range(1,(n+1)): #column
    print("*",end="")
print("\n-------------------------------------------------------------------------------------------------------------------------")
