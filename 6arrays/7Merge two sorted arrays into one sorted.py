#Merge two sorted arrays into one sorted array

#(Ascending Order)
def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number: "))
            l1.append(n)
        except:
            return l1

def merge(arr1,arr2):
    i=j=0
    res=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    while i<len(arr1):
        res.append(arr1[i])
        i+=1
    while j<len(arr2):
        res.append(arr2[j])
        j+=1
    return res

arr1=createarray()
arr2=createarray()
print("Result:",merge(arr1,arr2))

#(Descending Order)
def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number: "))
            l1.append(n)
        except:
            return l1

def merge(arr1,arr2):
    i=j=0
    res=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]>arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    while i<len(arr1):
        res.append(arr1[i])
        i+=1
    while j<len(arr2):
        res.append(arr2[j])
        j+=1
    return res

arr1=createarray()
arr2=createarray()
print("Result:",merge(arr1,arr2))
