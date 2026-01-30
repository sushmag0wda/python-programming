#reverse a num
'''
a)extarct the digit
b)align the extracted dig by making space(*10)
c)remove the dig'''
#normal logic
num=int(input("Enter a number: "))
rev=0
temp=num
if num<0:
    num=-num

while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10

if temp<0:
    rev=-rev
print(f"The reversal of {temp} is: {rev}")

#using function
def reversal(n):
    temp=n
    rev=0
    if n<0:
        n*=-1
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n//=10
    if temp<0:
        rev=rev*-1
    return rev

n=int(input("enter a number"))
rev=reversal(n)
print(f"reverse of {n} is :{rev}")

#WAP to reverse each individual numbers among the range of val's I/p
def reversal(n):
    temp=n
    rev=0
    if n<0:
        n*=-1
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n//=10
    if temp<0:
        rev=rev*-1
    return rev

start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))

if start > end:
    print("Invalid input")
else:
    for i in range(start,end+1):
        rev=reversal(i)
        print(f"the reversal of {i} = {rev}")
        