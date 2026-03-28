#hollow-odd-py
'''
       *
      * *
     *   *
    *     *
   *       *
  *         *
 *           *
***************
'''
n=int(input("enter a num"))
odd=1
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,odd+1):
        if i==n or j==odd or j==1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    odd+=2

