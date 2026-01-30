'''def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number"))
            l1.append(n)
        except Exception as e:
            return l1
def issorted(arr,i):
    if i==len(arr)-1:
        return True
    
    if arr[i]>arr[i+1]:
        return False
    
    return issorted(arr,i+1)
   
arr=createarray()
flag=issorted(arr,0)
if flag:
    print("the array is sorted:")
else:
    print("the array is not sorted:")'''

#function to check if the array is sorted or not using recursion
'''def createarry():
    l1=[]
    while True:
        try:
            n=int(input("enter a number"))
            l1.append(n)
        except Exception as e:
            return l1
def isorted(arr,i):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

arr=createarry()
flag=isorted(arr,0)
if flag==True: 
    print("the array is sorted:")
else:
    print("the array is not sorted:")
'''
        

#wap to return the rest part of the string by removing the target character

# def removetar(s,tar):
#     nstr=""
#     for i in range(0,len(s)):
#         if s[i]!=tar:
#             nstr=nstr+s[i]
#     return nstr
    
# s=input("enter a string:")
# tar=input("enter the target character:")
# res=removetar(s,tar)

# '''def removetar(s,tar,nstr,i):
    
#     if i==len(s):
#         return nstr
#     if s[i]!=tar:
#         nstr+=s[i]
#     return removetar(s,tar,nstr,i+1)
# s=input("enter a string:")
# tar=input("enter the target character:")
# res=removetar(s,tar,"",0)
# print("the new string is:",res)'''

#WAP to return the rest part of the string by removing the target substring
'''def substr(s,start,end):
    sub=""
    for i in range(start,end+1):
        sub+=s[i]
    return sub

def removesub(nstr,s,i,tarsub):
    if i==len(s):
        return nstr
    elif tarsub=="":
        return s
    
    if s[i]!=tarsub[0]:
        nstr+=s[i]
        return removesub(nstr,s,i+1,tarsub)
    else :
        length=(i+len(tarsub))-1
        if length<len(s):
            if substr(s,i,length)==tarsub:
                return removesub(nstr,s,length+1,tarsub)
            else:
                return removesub(nstr+s[i],s,i+1,tarsub)
        else:
            return removesub(nstr+s[i],s,i+1,tarsub)

s=input("enter a string")
tarsub=input("enter a substring")
res=removesub("",s,0,tarsub)
print(res)'''

#WAP to find the second maximum value in a given array using recursion
#WAP to implement order agnostic binary search using recursion
#WAP to print all the subarrays of a given array using recursion

#subsequence
def substr(s,index):
    sub=""
    for i in range(index,len(s)):
        sub+=s[i]
    return sub
def formsubstr(nstr,s):
    if s=="":
        print(nstr)
        return
    restsubstr=substr(s,1)
    formsubstr(nstr+s[0],restsubstr)
    formsubstr(nstr,restsubstr)
s=input("enter a string:")
formsubstr("",s)

