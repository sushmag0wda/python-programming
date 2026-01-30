#Arm Strong Numbers
#-if the sum of exponent val (base-->extracted digit and pow-->count of dig) is same as the original number then it is Arm Strong Number
#normal logic
def digits(n):#using function to count the digits
    count=0
    while n>0:
        n=n//10
        count+=1
    return(count)

n=int(input("enter a number"))
temp=n
if n<0:#checking if its -ve
    n=n*-1#converting it to +ve by multiplying by -1
pow=digits(n)
asn=0
while n>0:
    if(pow>0):
        base=n%10
        asn+=base**pow
        n//=10
if temp<0: #checking if the original number was -ve
    asn=asn*-1
if asn==temp:
    print(f"{asn} = {temp} therefore is an ASN")
else:
    print(f"{asn} not = {temp} therefore not an ASN")
#-------------------------------------------------------------------------------------------------------------
#using functions
def digits(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return(count)
def ASN(n,pow):
    asn=0
    while n>0:
        if(pow>0):
            base=n%10
            asn+=base**pow
            n//=10
    if temp<0:
        asn=asn*-1
    return(asn==temp)
n=int(input("enter a number"))#user input
temp=n
if n<0:#checking if its -ve
    n=n*-1#converting it to +ve by multiplying by -1
pow=digits(n)
flag=ASN(n,pow)
if flag:
    print(f"{temp} is an ASN")
else:
    print(f"{temp}not an ASN")
#-------------------------------------------------------------------------------------------------------------
# c. WAP to print all the ASN's in a user defined range.
def digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count if count > 0 else 1   # handles n = 0

def ASN(n, power):
    temp = n
    asn = 0
    while n > 0:
        base = n % 10
        asn += base ** power
        n //= 10
    return asn == temp   # returns True/False

start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))

if start > end:
    print("Invalid input")
else:
    print("asn numbers are : ")
    for i in range(start, end + 1):
        num = i
        if num < 0:
            pos_num = num*-1             # work with positive value
            power = digits(pos_num)
            flag = ASN(pos_num, power)  # catch return value in flag
            if flag:                    # check the flag
                print(num, end=" ")
        else:
            power = digits(num)
            flag = ASN(num, power)      # catch return value in flag
            if flag:                    # check the flag
                print(num, end=" ")

#-------------------------------------------------------------------------------------------------------------
# d. WAP to print all the ASN and non-ASN's seperateley in a user defined range.
def digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count if count > 0 else 1   # handles n = 0

def ASN(n, power):
    temp = n
    asn = 0
    while n > 0:
        base = n % 10
        asn += base ** power
        n //= 10
    return asn == temp   # returns True/False

start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))

if start > end:
    print("Invalid input")
else:
    print("asn numbers are : ")
    for i in range(start, end + 1):
        num = i
        if num < 0:
            pos_num = num*-1             # convert to +ve
            power = digits(pos_num)
            flag = ASN(pos_num, power)  # catch return value in flag
            if flag:                    # check the flag
                print(num, end=" ")
        else:
            power = digits(num)
            flag = ASN(num, power)      # catch return value in flag
            if flag:                    # check the flag
                print(num, end=" ")
    print("\nnot asn numbers are : ")
    for i in range(start, end + 1):
        num = i
        if num < 0:
            pos_num = num*-1             
            power = digits(pos_num)
            flag = ASN(pos_num, power)  
            if not flag:                 
                print(num, end=" ")
        else:
            power = digits(num)
            flag = ASN(num, power)      
            if not flag:                    
                print(num, end=" ")
#-------------------------------------------------------------------------------------------------------------
# e. WAP to print first "n" ASN's.
def digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count if count > 0 else 1   # handles n = 0

def ASN(n, power):
    temp = n
    asn = 0
    while n > 0:
        base = n % 10
        asn += base ** power
        n //= 10
    return asn == temp   # returns True/False

end = int(input("Enter the ending value: "))
start=0
print("asn numbers are : ")
for i in range(start, end + 1):
    num = i
    power = digits(num)
    flag = ASN(num, power)      
    if flag:                    
        print(num, end=" ")