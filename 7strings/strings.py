
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