#hollow-RHS-triangle
'''
         *
        **
       * *
      *  *
     *   *
    *    *
   *     *
  *      *
 *       *
**********
'''
n=int(input("enter a number")) 
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        if i==n or j==i or j==1:
            print("*",end="")
        else:
            print(" ",end="")
    print()