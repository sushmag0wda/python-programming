#WAp to convert the upper csae character to lower case in a given string
def lower_case(s1):
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
print("converted string: ",s2)