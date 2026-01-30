#WAP to count the digits of a given number without using any predefined functions
#whenever we need to carry forward the current cycle value to the cycle we should use the same variable on RHS for operation and LHS for updatiion

#normal logic
n=int(input("enter a number"))
if n<0:                     # check if number is negative
    n=n*-1                  # convert negative to positive
count=0
while n>0:                  # repeat until number becomes 0
    n=n//10                 # remove the last digit
    count+=1                # count digits
print(count)                # final digit count'''
#-------------------------------------------------------------------------------------------------------------
#using function
def digits(n):
    if n<0:#checking if its -ve
        n=n*-1#converting it to +ve by multiplying by -1
    count=0
    while n>0:
        n=n//10
        count+=1
    return(count)

n=int(input("enter a number"))
res=digits(n)
print("no of digits= ",res)