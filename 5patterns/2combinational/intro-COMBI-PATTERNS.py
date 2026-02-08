#COMBINATIONAL PATTERNS
'''
1)LHS half diamond
*
**
***
****
***
**
*
'''
def lhshd(n):
    noc=1
    for i in range(1,n*2):
        for j in range(1,noc+1):
            print("*",end="")
        print()
        if i<n:
            noc+=1
        else:
            noc-=1
'''
2)RHS half diamond
   *
  **
 ***
****
 ***
  **
   *
'''
def rhshd(n):
    noc=1
    for i in range(1,n*2):
        for k in range(n,noc,-1):
            print(" ",end="")
        for j in range(1,noc+1):
            print("*",end="")
        print()
        if i<n:
            noc+=1
        else:
            noc-=1
'''
3)diamond
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
'''
def dia(n):
    noc=1
    for i in range(1,n*2):
        for k in range(n,noc,-1):
            print(" ",end="")
        for j in range(1,noc+1):
            print("*",end=" ")
        print()
        if i<n:
            noc+=1
        else:
            noc-=1
'''
4)odd diamond
       *
     * * *
   * * * * *
 * * * * * * *
   * * * * *
     * * *
       *
'''
def odddia(n):
    noc=1
    for i in range(1,n*2):
        for k in range(n*2,noc,-1):
            print(" ",end="")
        for j in range(1,noc+1):
            print("*",end=" ")
        print()
        if i<n:
            noc+=2
        else:
            noc-=2
'''
5)k
****
***
**
*
**
***
****
'''
def k(n):
    noc=n
    for i in range(1,n*2):
        for j in range(1,noc+1):
            print("*",end="")
        print()
        if i<n:
            noc-=1
        else:
            noc+=1
'''
6)k inverse
****
 ***
  **
   *
  **
 ***
****
'''
def kin(n):
    noc=n
    for i in range(1,n*2):
        for k in range(n,noc,-1):
            print(" ",end="")
        for j in range(1,noc+1):
            print("*",end="")
        print()
        if i<n:
            noc-=1
        else:
            noc+=1
'''
7)Hourglass
* * * *
 * * *
  * *
   *
  * *
 * * *
* * * *
'''
def hg(n):
    noc=n
    for i in range(1,n*2):
        for k in range(n,noc,-1):
            print(" ",end="")
        for j in range(1,noc+1):
            print("*",end=" ")
        print()
        if i<n:
            noc-=1
        else:
            noc+=1
'''
8)Butterfly
*     *
**   **
*** ***
*******
*** ***
**   **
*     *
'''
def bf(n):
    noc=1
    nor=(n*2)-1
    for i in range(1,n*2):
        for j in range(1,n*2):
            if j<=noc or j>=nor:
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
n=int(input("enter a number"))
lhshd(n)
print("==========================================================================")
rhshd(n)
print("==========================================================================")
dia(n)
print("==========================================================================")
odddia(n)
print("==========================================================================")
k(n)
print("==========================================================================")
kin(n)
print("==========================================================================")
hg(n)
print("==========================================================================")
bf(n)
print("==========================================================================")