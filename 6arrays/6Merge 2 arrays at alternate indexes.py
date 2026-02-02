#Merge 2 arrays at alternate indexes
'''
a1 = [2, 1, 3]
a2 = [10, 11, 12, 13, 45, 65]

Output = [2, 10, 1, 11, 3, 12, 13, 45, 65]'''

def createarray():
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
print(f"resultent array is :{arr3}")

#Merge Two Arrays at Alternate Indexes (Using insert() In-Place)

def createarray():
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
print(f"resultent array is :{arr1}")
