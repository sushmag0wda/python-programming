#paralleogram inverse
'''
     ******
    *    *
   *    *
  *    *
 *    *
******
'''
n=int(input("enter a number"))
for i in range(n,0,-1):
    for k in range(1,i):
        print(" ",end="")
    for j in range(n,0,-1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()