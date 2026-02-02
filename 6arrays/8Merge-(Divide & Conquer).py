#Merge Sort (Divide & Conquer – Single Array)
def createarray():
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
print(f"resultent array is :{arr}")
