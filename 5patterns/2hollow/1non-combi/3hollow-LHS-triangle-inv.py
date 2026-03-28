#hollow LHS inverse Triangle
'''
**********
*       *
*      *
*     *
*    *
*   *
*  *
* *
**
*
'''
n=int(input("enter a number"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        if i==n or j==1 or j==n or j==i:
            print("*",end="")
        else:
            print(" ",end="")
    print()