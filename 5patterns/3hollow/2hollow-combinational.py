

#combinatinoal
#1)
'''
*
**
* *
*  *
*   *
*  *
* *
**
*
'''
'''n=int(input("enter the value"))
noc=1
for i in range(1,n*2):
    for j in range(1,noc+1):
        if j==1 or j== noc:
            print("*",end="")
        else:
            print(" ",end="")
        
    print()
    if i<n:
        noc+=1
    else:
        noc-=1'''
#2)


'''n=int(input("enter the number : "))
noc=1
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        if j==n or j== noc:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i < n:
        noc+=1
    else:
        noc-=1'''