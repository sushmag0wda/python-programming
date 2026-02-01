#strings
'''
strings are collection of character enclosed in quotes
'''
#WAp to convert the upper csae character to lower case in a given string
'''def lower_case(s1):
    nstr=""
    for i in range (0,len(s1)):
        if "A"<=s1[i]<="Z":
            nstr=nstr+chr(ord(s1[i])+32)
        else:
            nstr=nstr+s1[i]
    return nstr
def upper_case(s1):
    nstr=""
    for i in range (0,len(s1)):
        if "a"<=s1[i]<="z":
            nstr=nstr+chr(ord(s1[i])-32)
        else:
            nstr=nstr+s1[i]
    return nstr

def swap_case(s1):
    nstr=""
    for i in range (0,len(s1)):
        if "a"<=s1[i]<="z":
            nstr=nstr+chr(ord(s1[i])-32)
        elif "A"<=s1[i]<="Z":
            nstr=nstr+chr(ord(s1[i])+32)
        else:
            nstr=nstr+s1[i]
    return nstr

s1=input("enter a string")
print("given string :",s1)
#s2=lower_case(s1)
#s2=upper_case(s1)
s2=swap_case(s1)
print("converted string: ",s2)'''

#WAP to sum of all the individual character digits present in a given string
'''
I/P:a12d34c4

o/p: (1+2+3+4+4)
    =14
'''
#i/p : "a12d34c4"
#OP:adc(12+34+4)=adc50
'''def digsum(str):
    sum=0# to collect the sum of the digits present in the string
    res=""#to collect left over character
    for i in range(0,len(str)):
        if "0"<=str[i]<="9":
            sum=sum+(ord(str[i])-48)  #to convert char '1' to int 1
        else:
            res=res+str[i]   #to add the leftover characters from the string from a2b4cs to abcs

    nstr=''
    while sum>0:
        rem=sum%10
        nstr=chr(rem+48)+nstr  
        sum=sum//10
        #this logic can be replaced with newstr=string(sum)

    return res+nstr

str=input("enter a string : ")
res=digsum(str)
print(res)
'''
#alignment of character

#normal alignment: if traversal is from LHS then keep the memory in LHS
                #  if traversal is from RHS then keep the memory in RHS
#reverse alignment :
                #if traversal is from LHS then keep the memory in RHS
                #if traversal is from RHS then keep the memory in LHS
#reversal of strings

'''def reverse(str):
    str=str+" "
    nsen=""
    nwrd=""
    for i in range(0,len(str)):
        if str[i]!=" ":
            nwrd=str[i]+nwrd      
        elif nwrd!="":
            if nsen=="":
                nsen=nsen+nwrd
            else:
                nsen=nsen+" "+nwrd
            nwrd=""
    return nsen

str=input("enter a string")
print("og sentence=",str)
str1=reverse(str)
print("new str=",str1)
'''

'''def reverse(str):
    str=str+" "
    nsen=""
    nwrd=""
    for i in range(0,len(str)):
        if str[i]!=" ":
            nwrd=nwrd+str[i]    
        elif nwrd!="":
            if nsen=="":
                nsen=nwrd+nsen
            else:
                nsen=nwrd+" "+nsen
            nwrd=""
    return nsen

str=input("enter a string")
print("og sentence=",str)
str1=reverse(str)
print("new str=",str1)'''

'''def reverse(str):
    str=str+" "
    nsen=""
    nwrd=""
    for i in range(0,len(str)):
        if str[i]!=" ":
            if nwrd==""and ("a"<=str[i]<="z"):
                nwrd=nwrd+chr(ord(str[i])-32)
            else:
                nwrd=nwrd+str[i]    
        elif nwrd!="":
            if nsen=="":
                nsen=nwrd+nsen
            else:
                nsen=nwrd+" "+nsen
            nwrd=""
    return nsen

str=input("enter a string")
print("og sentence=",str)
str1=reverse(str)
print("new str=",str1)
'''

def strfilt(s):
    nstr=""
    for i in range(0,len(s)):
        if 'A'<=s[i]<='Z':
            nstr=nstr+chr(ord(s[i])+32)
        elif ('a'<=s[i]<='z') or ('0'<=s[i]<='9'):
            nstr=nstr+s[i]
    return nstr

def plaindrome(str):
    str1=strfilt(str)
    i=0
    j=len(str1)-1

    while i<j:
        if str1[i]!=str1[j]:
            return False
        i+=1
        j-=1
    return True
str=input("enter a string : ")
print("og sentence=",str)
flag=plaindrome(str)
if flag==True:
    print("palindrome")
else:
    print("not palindrome")