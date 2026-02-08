#hollow-RHS-triangle-inv
'''
********
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
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        if j==i or i==n or j==1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

    