#hollow patterns 
#1)
'''
*****
*   *
*   *
*   *
*****
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
#2)
'''
*****
** **
* * *
** **
*****
'''
'''n=int(input("enter the value"))
if n%2==0:
    n+=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==j or (i+j)==(n+1):
            print("*",end="")
        else:
            print(" ",end="")
    print()'''
#3)
'''
*****
 * *
  *
 * *
*****
'''
'''n=int(input("enter the value"))
if n%2==0:
    n+=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or i==j or (i+j)==(n+1):
            print("*",end="")
        else:
            print(" ",end="")
    print()'''

#4)
'''
*   *
** **
* * *
** **
*   *
'''
'''n=int(input("enter the value"))
if n%2==0:
    n+=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==n or i==j or (i+j)==(n+1):
            print("*",end="")
        else:
            print(" ",end="")
    print()'''

#5)
'''
*
**
* *
*  *
*****
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or j==1 or i==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()'''
#6)
'''
    *
   **
  * *
 *  *
*****
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or j==n or (i+j)==(n+1):
            print("*",end="")
        else:
            print(" ",end="")
    print()'''

'''n=int(input("enter the value"))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,n+1):
            if i==n or j==1 or (i==j):
                print("*",end="")
            else:
                print(" ",end="")
    print()'''

#7)
'''
    *
   * *
  *   *
 *     *
* * * * *
'''

'''n=int(input("enter the value"))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,n+1):
            if i==n or j==1 or (i==j):
                print("* ",end="")
            else:
                print("  ",end="")
    print()'''
#8)
'''
*****
 *  *
  * *
   **
    *
'''
'''n=int(input("enter the value"))
for i in range(n,0,-1):
    for j in range(1,n+1):
        if i==n or j==n or (i+j)==(n+1):
            print("*",end="")
        else:
            print(" ",end="")
    print()'''
#9)
'''
*****
 *  *
  * *
   **
    *
'''
'''n=int(input("enter the value"))
for i in range(n,0,-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,n+1):
            if i==n or j==1 or (i==j):
                print("*",end="")
            else:
                print(" ",end="")
    print()'''