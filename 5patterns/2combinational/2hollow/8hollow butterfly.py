#hollow butterfly
'''
*     *
**   **
* * * *
*  *  *
* * * *
**   **
*     *
'''
n=int(input("enter a number"))
noc=1
nor=(n*2)-1
for i in range(1,n*2):
    for j in range(1,n*2):
        if j==noc or j==nor or j==1 or j==(n*2)-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i<n:
        noc+=1
        nor-=1
    else:
        noc-=1
        nor+=1