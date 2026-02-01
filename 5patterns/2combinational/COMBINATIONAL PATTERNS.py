#COMBINATIONAL PATTERNS
'''
1)
*
* *
* * *
* * * *
* * *
* *
*
'''
n=int(input("enter the number : "))
noc=1
for i in range(1,n*2):
    for j in range(1,noc+1):
        print("*",end=" ")
    print()
    if i < n:
        noc+=1
    else:
        noc-=1

'''
2)
   *
  **
 ***
****
 ***
  **
   *
'''
'''n=int(input("enter the number : "))
noc=1
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print("*",end="")
    print()
    if i < n:
        noc+=1
    else:
        noc-=1
'''
#3)
'''
   * 
  * *
 * * *
* * * *
 * * *
  * *
   *
'''
'''n=int(input("enter the number : "))
noc=1
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print("*",end=" ")
    print()
    if i < n:
        noc+=1
    else:
        noc-=1'''
#4)
'''
      * 
    * * *
  * * * * *
* * * * * * *
  * * * * *
    * * *
      *
'''
'''n=int(input("enter the number : "))
noc=1
for i in range(1,n*2):
    for k in range((n*2)-1,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print("* ",end="")
    print()
    if i < n:
        noc+=2
    else:
        noc-=2'''

#5)
'''
****
***
**
*
**
***
****
'''
'''n=int(input("enter the number : "))
noc=n
for i in range(1,n*2):
    for j in range(1,noc+1):
        print("*",end="")
    print()
    if i < n:
        noc-=1
    else:
        noc+=1'''
#6)
'''
****
 ***
  **
   *
  **
 ***
****
'''
'''n=int(input("enter the number : "))
noc=n
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ", end="")
    for j in range(1,noc+1):
        print("*",end="")
    print()
    if i < n:
        noc-=1
    else:
        noc+=1'''

#7)
'''
* * * * 
 * * *
  * *
   *
  * *
 * * *
* * * *
'''
'''n=int(input("enter the number : "))
noc=n
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ", end="")
    for j in range(1,noc+1):
        print("* ",end="")
    print()
    if i < n:
        noc-=1
    else:
        noc+=1
'''
#8)
'''
*     *
**   **
*** ***
*******
*** ***
**   **
*     *
'''
#note : if there is spaces in between the patterns we should take a if-else block in the j loop 
#any changes made on if block should also be done on else block
'''n=int(input("enter the number : "))
noc=1
nor=(n*2)-1
for i in range(1,n*2):
    for j in range(1,n*2):
        if j<=noc or j>=nor:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i < n:
        noc+=1
        nor-=1
    else:
        noc-=1
        nor+=1
'''