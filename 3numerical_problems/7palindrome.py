#Integer palindrome
#a num is a palindrome if its reversal is same as itself
#a)normal logic

num=int(input("Enter a number: "))
rev=0
temp=num
if num<0:#check if the number is negative
    num=-num#convert it to positive by multiplying by -1

while num>0: #reverse the number
    rem=num%10
    rev=(rev*10)+rem
    num=num//10

if temp<0:#if the original number was -ve, then make the reversed num -ve
    rev=-rev

if temp==rev:#check if the original number is same as the reversed num
    print(f"{temp} is a palindrome")

else:
    print(f"{temp} is not a palindrome")
#--------------------------------------------------------------------------------------------------------------'''
#b)using functions
def palindrome(n):
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
    return temp==rev

n=int(input("enter a number"))
flag=palindrome(n)
if flag:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")

#d) WAP to print all the integer palindrome's and non integer palindrome's of a user defined range seperateley.
def palindrome(n):
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
    if temp==rev:
        return temp

start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))

if start > end:
    print("Invalid input")
else:
    print("palindrome")
    for i in range(start,end+1):
        rev=palindrome(i)
        if rev==i:
            print(rev, end=" ")
    print("\nnot palindrome")
    for i in range(start,end+1):
        rev=palindrome(i)
        if rev!=i:
            print(i, end=" ")


#e) WAP to print first "n" non-palindromic numbers.
def palindrome(n):
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
    if temp==rev:
        return temp

end = int(input("Enter the ending value: "))
start=0
print("palindrome numbers are: ")
for i in range(start,end+1):
        rev=palindrome(i)
        if rev==i:
            print(rev, end=" ")