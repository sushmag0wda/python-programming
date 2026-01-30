'''
#while loop
-it is used to execute a block of code repeatedly until a condition is met
syntax:
#initialization
while condition:
    #logic
    #increment or decrement
#remaining statements'''

#WAP to print numbers from i to n
n = int(input("Enter a number: "))# input-> 10
i = 2
while i <= n:
    print(i, end=" ")#prints numbers from 2 to 10 op-> 2 3 4 5 6 7 8 9 10
    i += 1
print("program executed")
print("last i: ", i)#op-> 11

#-----------------------------------------------------------------------------
#WAP to print the sequence of numbers in reverse order with decreasing difference
#example:10 9 7 4 0
#WKT the difference between the numbers is increasing by 1 each time

n=int(input("Enter a number: ")) # input-> 10
diff=1
while n>=0:
    print(n, end=" ")# prints numbers in reverse order with incresing difference op-> 10 9 7 4 0
    n =n- diff # decreases the number by the difference
    diff=diff+1 # increases the difference each time by 1
print("\nProgram executed")
print("Last n: ", n)# op-> -3
print("\n-------------------------------------------------------------------------------------------------------")


