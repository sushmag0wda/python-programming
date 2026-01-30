#array
'''
-it is data structure
-data structure: storing of data in a organised manner
-ex: sting,array,linked list,ques,stack
-Algorithm -to store data we use some steps it is called algorithm
'''
'''
-Collection of datas (homogeneous,heterogeneous)
-It is a indexed DS
-It is an iterable obj
-Size is dynamic in nature(the allocated memory can be enlarged and shrinked based on the user requirement)
-Arrays are indeicate dby using a pair of []
    syn:
        arr-name=[data,data2,....]
ex:
arr1=[]#empty array
print(arr1)      # []
arr2=[1,"ab",2]
print(arr2)      # [1,"ab",2]
arr3=[1,1,1]
s2=(1,2,3,4)
s3={1,2,3,3}
dict={1:2,2:3,4:5}
arr2=[1,"ab",2,arr3,s2,s3,dict]
print(arr2)          #[1, 'ab', 2, [1, 1, 1], (1, 2, 3, 4), {1, 2, 3}, {1: 2, 2: 3, 4: 5}]
'''
#len()
'''len()-it is a inbuilt function that returns the count of number of elements present in a created iterable obj
    -it returns a whole number
            syn:
                len(created_iterable_obj)
'''
#example
''''arr1=[]#empty array
arr2=[1,"ab",2]
print(arr2)      # [1,"ab",2]
arr3=[1,1,1]
s2=(1,2,3,4)
s3={1,2,3,3}
dict={1:2,2:3,4:5}
arr4=[1,"ab",2,arr3,s2,s3,dict]
print(arr4) 
print(len(arr1)) #0
print(len(arr2)) #3
print(len(arr3)) #3
print(len(s2))  #4
print(len(s3)) #3
print(len(dict))#3
print(len(arr4))#7'''

#Index:
'''
-it is a whole no assigned by the PVM during the insertion of each individual element into the craeted array
-the programmers can only use an index but can never upadate it
-syn:
    arr_name[index]
-if we try to access an index that is not available in the craeted array ,then pvm will immidiately throw a index error
'''
#append()
'''
append is a predefined function that helps to add a value as it is to end of a array
syn:
    arry_name.append(value)
'''
'''arr1 = [1, 2, 3]
arr2 = [100, 200]
print(arr1)
print(arr2)
arr1.append(arr2)
print("==================")
print(arr1)
print(arr2)
print(arr1[3])
print("==================")
print(arr1[3][0])
arr1[3][0] = 999
print(arr1[3][0])
print(arr2)'''
#insert()

#exted
'''def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number"))
            l1.append(n)
        except Exception as e:
            return l1
def findlargest(arr):
    max,maxind=-2147483648,-1
    for i in range(0,len(arr)):
        if max<arr[i]:
            max=arr[i]
            maxind=i
    return max,maxind

def findsmallest(arr):
    min,minind=+2147483648,-1
    for i in range(0,len(arr)):
        if min>arr[i]:
            min=arr[i]
            minind=i
    return min,minind
            
print("enetr val into the array: ")
arr=createarray()
res,resind=findlargest(arr)
res1,res1ind=findsmallest(arr)
print(f"the max element is {res} stored in {resind}")
print(f"the min element is {res1} stored in {res1ind}")'''
#selection sort
'''def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number"))
            l1.append(n)
        except Exception as e:
            return l1

def selectionsort(arr):
    n=len(arr)
    #cycles
    for i in range(0,n-1):
        actind=(n-1-i)
        #curr max ele ind
        currmax=-2**31
        currmaxind=-1
        for j in range(0,n-i):
            if currmax<arr[j]:
                currmax=arr[j]
                currmaxind=j
        arr[actind], arr[currmaxind]=(arr[currmaxind],arr[actind]) 

print("enetr val into the array: ")
arr=createarray()
print("array before sorting",arr)
selectionsort(arr)
print("array after sorting",arr)
'''
'''def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number"))
            l1.append(n)
        except Exception as e:
            return l1

def selectionsort(arr):
    n=len(arr)
    #cycles
    for i in range(0,n-1):
        actind=(n-1-i)
        #curr max ele ind
        currmax=2**31
        currmaxind=-1
        for j in range(0,n-i):
            if currmax>arr[j]:
                currmax=arr[j]
                currmaxind=j
        arr[actind], arr[currmaxind]=(arr[currmaxind],arr[actind]) 

print("enetr val into the array: ")
arr=createarray()
print("array before sorting",arr)
selectionsort(arr)
print("array after sorting",arr)'''

#merging
#Wap to merge the given 2 customizrd arrays at alternate indexes
'''
i/p
a1=[2,1,3]
a2=[]10,11,12,13,45,65
0/p=[2,10,1,11,3,12,13,45,65]
'''
'''def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number"))
            l1.append(n)
        except Exception as e:
            return l1
def merge(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    i=0
    j=0
    res=[]
    for k in range(0,(n1+n2)):
        if (i<n1 and (k%2==0)):
            res.append(arr1[i])
            i+=1
        elif  (j<n2 and (k%2!=0)):
            res.append(arr2[j])
            j+=1 
        else:
            if i<n1:
                res.append(arr1[i])
                i+=1
            elif j<n2 :
                res.append(arr2[j])
                j+=1
    return res  
print("enetr val into the array1: ")
arr1=createarray()
print(f"given array 1 is :{arr1}")
print("enetr val into the array2: ")
arr2=createarray()
print(f"given array 2 is :{arr2}")
arr3=merge(arr1,arr2)
print(f"resultent array is :{arr3}")'''


'''def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number"))
            l1.append(n)
        except Exception as e:
            return l1
def merge(arr1,arr2):
   odd=1
   n1=len(arr1)
   n2=len(arr2)
   for j in range(0,n2):
       arr1.insert(odd,arr2[j])
       odd+=2
       
print("enetr val into the array1: ")
arr1=createarray()
print("enetr val into the array2: ")
arr2=createarray()
print(f"given array 1 is :{arr1}")
print(f"given array 2 is :{arr2}")
merge(arr1,arr2)
print(f"resultent array is :{arr1}")'''


#merging 2 sorted errors
'''def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number"))
            l1.append(n)
        except Exception as e:
            return l1
def merge(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    i=0
    j=0
    res=[]
    for k in range(0,(n1+n2)):
        if (i<n1 and j<n2):
            if (arr1[i]<arr2[j]):
                res.append(arr1[i])
                i+=1
            else:
                res.append(arr2[j])
                j+=1
        else:
            if (i<n1):
                    res.append(arr1[i])
                    i+=1
            else:
                    res.append(arr2[j])
                    j+=1            
    return res  
print("enetr val into the array1: ")
arr1=createarray()
print("enetr val into the array2: ")
arr2=createarray()
print(f"given array 1 is :{arr1}")
print(f"given array 2 is :{arr2}")
arr3=merge(arr1,arr2)
print(f"resultent array is :{arr3}")'''

'''def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number"))
            l1.append(n)
        except Exception as e:
            return l1
def merge(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    i=0
    j=0
    res=[]
    for k in range(0,(n1+n2)):
        if (i<n1 and j<n2):
            if (arr1[i]<arr2[j]):
                res.append(arr2[j])
                i+=1
            else:
                res.append(arr1[i])
                j+=1
        else:
            if (i<n1):
                    res.append(arr1[i])
                    i+=1
            else:
                    res.append(arr2[j])
                    j+=1            
    return res  
print("enetr val into the array1: ")
arr1=createarray()
print("enetr val into the array2: ")
arr2=createarray()
print(f"given array 1 is :{arr1}")
print(f"given array 2 is :{arr2}")
arr3=merge(arr1,arr2)
print(f"resultent array is :{arr3}")'''

'''def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number"))
            l1.append(n)
        except Exception as e:
            return l1
        
def mergedivide(arr,start,end):
     if start>=end:
          return
     mid=(start+end)//2
     #LHS
     mergedivide(arr,start,mid)
     #RHS
     mergedivide(arr,mid+1,end)
     #merging
     mergecon(arr,start,mid,end)

#conquer and affect the original array
def mergecon(arr,start,mid,end):
    
    i=start
    j=mid+1
    res=[]
    for k in range(0,(mid+end)+1):
        if i<=mid and j<=end:
            if arr[i]<arr[j]:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j += 1
        else:
            if i<=mid:
                res.append(arr[i])
                i += 1
            elif j<=end:
                res.append(arr[j])
                j += 1
    for k in range(0,len(res)):
        arr[start]=res[k]
        start+=1
print("enetr val into the array: ")
arr=createarray()
print(f"given array 1 is :{arr}")
mergedivide(arr,0,(len(arr)-1))
print(f"resultent array is :{arr}")'''
#binary search
'''def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number"))
            l1.append(n)
        except Exception as e:
            return l1

def binary_search(arr,tar):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if tar==arr[mid]:
            return mid
        if tar<arr[mid]:
            end=mid-1
        else:
            start=mid+1
    return -1
     

print("enetr val into the array in sorted order: ")
arr=createarray()
tar=int(input("enter the target element"))
print(f"given array is :{arr}")
flag=binary_search(arr,tar)
if flag!=-1:
    print(f"the target element {tar} is in {flag} index")
else:
    print(f"the target element {tar} is not found")'''

# the process of analysind the order of given array and applying binary search is called order agnostic binary search
# 0(log n) is time complexity of B search because array is divided into 2 parts 
'''def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number"))
            l1.append(n)
        except Exception as e:
            return l1

def orbinary_search(arr,tar):
    start=0
    end=len(arr)-1
    flag="asc"
    if arr[start]>arr[end]:
        flag="desc"
    while start<=end:
        mid=(start+end)//2
        if flag =="asc":
            if tar==arr[mid]:
                return mid
            if tar<arr[mid]:
                end=mid-1
            else:
                start=mid+1
        else:
            if tar==arr[mid]:
                return mid
            if tar<arr[mid]:
                start=mid+1
            else:
                end=mid-1
    return -1
     

print("enetr val into the array in sorted order: ")
arr=createarray()
tar=int(input("enter the target element"))
print(f"given array is :{arr}")
flag=orbinary_search(arr,tar)
if flag!=-1:
    print(f"the target element {tar} is in {flag} index")
else:
    print(f"the target element {tar} is not found")
'''

#dictinoary 
'''
- it is a data structure
- it is a key value pair based DS
- it is an iterable obj
-immutable in nature

-syn:
    dict_name={key1:value1,key2:value2}
-keys
    -it is an identifier
    -it is immutable in nature
    -it should be unique
    -it should be of homogeneous type
    -mutable ds cannot be a key
    -keys cannot be duplicated if duplicated it will consider the lastest key value pair
    -to get the count of keys we use len()
-values
    -it is a data
    -it is mutable in nature
    -it can be of heterogeneous type
    -it can be duplicated
    -to get the count of values we use len()
- to get the count of key value pairs we use len()
-{:} is used to represent a dictionary
- when do we use a dictionary in coding?
    -when we want to track the frequency of elements
    -to store elements in key value pair format
- to traverse a dictinoary we use for loop with dict.items() function
    -syn:
        for key,value in dict_name.items():
            print(key,value)
- to access a value we use dict_name[key]
    -syn:
        dict_name[key]
- to update a value we use dict_name[key]=new_value
    -syn:
        dict_name[key]=new_value
- to add a new key value pair we use dict_name[new_key]=new_value
    -syn:
        dict_name[new_key]=new_value

'''
#WAP to segregate bwteen duplicated on duplicates and unique elements present in an integer array 
'''
duplicates-elements that are repeated more than once
unique elements-elements that are not repeated
nonduplicates-elements that are repeated only once
'''
def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number"))
            l1.append(n)
        except Exception as e:
            return l1
def segregate(arr):
    dict={}
    dup,nondup,uniq=[],[],[]
    for i in range(0,len(arr)):
        if arr[i] in dict:
            dict[arr[i]]=dict[arr[i]]+1
        else:
            dict[arr[i]]=1
    for key,value in dict.items():
        if value>1:
            dup.append(key)
        if value>=1:
            nondup.append(key)
        if value==1:
            uniq.append(key)
    return dup,nondup,uniq
    
print("enetr val into the array: ")
arr=createarray()
dup,nondup,uniq=segregate(arr)
print(f"the given array is :{arr}")
print(f"the duplicates elements are :{dup}")
print(f"the nonduplicates elements are :{nondup}")
print(f"the unique elements are :{uniq}")
