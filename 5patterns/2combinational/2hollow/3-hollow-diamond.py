#hollow diamond
'''
   * 
  * *
 *   *
*     *
 *   *
  * *
   *
'''
n=int(input("enter a num"))
noc=1
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        if j==1 or j==noc:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1
