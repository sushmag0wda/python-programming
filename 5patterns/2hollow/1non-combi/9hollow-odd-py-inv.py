#hollow-odd-py-inv
'''
***************
 *           *
  *         *
   *       *
    *     *
     *   *
      * *
       *
'''
n=int(input("enter a number"))
odd=(n*2)-1
for i in range(n,0,-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,odd+1):
        if i==n or j==1 or j==odd:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    odd-=2
