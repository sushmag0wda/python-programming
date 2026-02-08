#hollow k
'''
*  *
* *
**
*
**
* *
*  *
'''
n=int(input("enter a number"))
noc=n
for i in range(1,n*2):
    for j in range(1,noc+1):
        if j==1 or j==noc:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1