
'''def gcd(n1, n2, i, current_gcd, lower):
    if i > lower:
        return current_gcd
    if n1 % i == 0 and n2 % i == 0:
        current_gcd = i
    return gcd(n1, n2, i + 1, current_gcd, lower)  # increment i

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

lower = n1
if n2 < n1:
    lower = n2

res = gcd(n1, n2, 1, 1, lower)
print("GCD =", res)
'''

#euclidian's algorithm
'''
given
n1,n2
findgcd(n1,n2)=find((n1-n2),n2), keep repeating until n1 is reduced to 0,once n1==0,n2 is HCF
'''
'''def findHCF(n1,n2):
    if n1==0:
        return n2
    if n1<n2:
        n1,n2=n2,n1
    return findHCF((n1%n2),n2)

n1=int(input("enter a first number"))
n2=int(input("enter a second number"))
res=findHCF(n1,n2)
print(res)'''

'''def findHCF(n1,n2):
    if n1==0:
        return n2
    if n1<n2:
        n1,n2=n2,n1
    return findHCF((n1-n2),n2)

n1=int(input("enter a first number"))
n2=int(input("enter a second number"))
res=findHCF(n1,n2)
print(res)
'''
'''def findHCF(n1, n2):
    if n2 == 0:
        return n1
    return findHCF(n2, n1 % n2)

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

res = findHCF(n1, n2)

if res == 1:
    print("They are co-primes")
else:
    print("They are not co-primes")'''

#factorial 
'''
factorial(4)===>24
factorial(5)===>120
-----------------------------
factorial(24)==>24*fact(24-1)
factorial(50)==>50*fact(50-1)

'''
#recursion helps to reduce complex expression to simplest form then calculate 
'''def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)
n=int(input("enter a number"))
res=factorial(n)
print(res)'''

#fibonacci series
'''
it is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
The sequence commonly starts with 0 and 1, and the next number is found by adding the two numbers before it.
The beginning of the Fibonacci sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

ex
0+1=1
1+1=2
1+2=3
2+3=5
3+5=8 ....
series = 1,2,3,5,5.....'''
'''
recursive logic
logic = print(n1)
para= pos,n1,n2
    argu:(pos-1),n1,
    n1+n2
base cond =if pos<=0:
return
'''
#fibonacci using recursion 
'''
def fib(pos,n1,n2):
    if pos<=0:
        return
    print(n1,end=" ")
    fib(pos-1,n2,n1+n2)
pos=int(input("enter the pos"))
print("fibonacci series")
fib(pos,0,1)'''

#write a program to print the nth fibonacci number
'''def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input("enter the n"))
res=fib(n)
print(res)'''

#happy numbers
#a number is said to be happy when the number is reduced to 1,if the num is reduced to 4 then it is said to be unhappy and if it not 1 or 4 then sum up the square of each didgit of the number and repeat the same
'''
example:

n=32

'''
#whenevr we want to repeat a repeated logic we use nested loop and loop inside recursive logic
'''def happy(n):
    sum=0
    if n==1:
        return True
    elif n==4:
        return False
    while n>0:
        base=n%10
        sum+=base**2
        n=n//10
    return happy(sum)
n=int(input("enter the n"))
res=happy(n)
if res:
    print("happy")
else:
    print("not happy")'''
#-------------------------------------------------------------------------------------------------------------------------------------
#Patterns
'''
it is the combination of rows and columns
------------ ==> sleeping/horizontal/row
|
|
| ===> standing/vertical/colmuns

we can make this dynamic by taking total number rows to be printed in the pattern
range of n
4<=n<=15
- 2types :
            i)non combinational patterns:right angle triangle,square,rombhus
                                        -direct n value will be taken as I/P
            ii)combinational patterns: K pattern,diamond,buttrfly
                                        -"(2*n)" val will be taken as I/P
-varities:star,hollow,number,alphabetic
-print()-it moves the control to the beginning of the next line
        -if any argument is passed then display it on the output screen then move the contol to the next line
'''
'''print("hello")
print("WORLD")
print()
print("hi")
print("hello",end="")
print("world")
'''
#note : once u move the control to the next line u can never get it back to the previousline
'''#1)
print("*")
print("\n-------------------------------------------------------------------------------------------------------------------------")
#2)* column
n=int(input("enter a number"))
for i in range(1,(n+1)): #rows
    print("*")
print("\n-------------------------------------------------------------------------------------------------------------------------")'''
'''#3)* row
n=int(input("enter a number"))
for j in range(1,(n+1)): #column
    print("*",end="")
print("\n-------------------------------------------------------------------------------------------------------------------------")
'''
#square pattern
'''n=int(input("enter a number"))
for i in range(1,(n+1)):  #always for rows loop first because we cannot go back to the previous line
    for j in range(1,(n+1)): # always column
        print("*",end=" ")
    print()        
print("\n-------------------------------------------------------------------------------------------------------------------------")
'''
'''#note- i loop is always dependent on n value
        -j loop is dependent on n,i,or 3rd valiable

'''
#triangular patterns
#a)LHS right angle triangle
'''
*
**
***
****
relationship table
i|j
1|1-1
2|1-2
3|1-3
4|1-4

i loop==> 1 to 4
j loop==> 1 to i

'''
'''n=int(input("enter a number"))
for i in range(1,(n+1)):  #always for rows loop first because we cannot go back to the previous line
    for j in range(1,(i+1)): # always column
        print("*",end="")
    print() '''
#LHS inverted Right angle triangle
'''
****
***
**
*
relationship table
i|j
4|1-4
3|1-3
2|1-2
1|1-1
i loop==>n till(1-1),
[decerementing]    -ve step

j loop==>1 till (i+1),
[incerementing]    +ve step

'''

'''n=int(input("enter a number"))
for i in range(n,(1-1),-1):  #always for rows loop first because we cannot go back to the previous line
    for j in range(1,(i+1)): # always column
        print("*",end="")
    print() '''

#RHS right angle triangle
'''
   *
  **
 ***
****
relationship table
i|k[explicit] |j
1|4-2[till 1] |1-4
2|4-3[till 2] |1-3
3|4-2[till 3] |1-2
4| 0 [till 4] |1-1
i loop==>1 till(n+1),
[decerementing]    +ve step

k loop==>n till(i),
[decerementing]    -ve step

j loop==>1 till (i+1),
[incerementing]    +ve step

'''
'''n=int(input("enter a number"))
for i in range(1,n+1):  #always for rows loop first because we cannot go back to the previous line
    for k in range(n,(i),-1): # always column
        print(" ",end="")
    for j in range(1,(i+1)): # always column
            print("*",end="")
    print()'''
#pyramid
'''
   * 
  * *
 * * *
* * * *
comparision table
   *                    |    *
  **                    |   * *
 ***                    |  * * *
****                    | * * * *
------------------------|--------------------
rows|   RHS             |     pyramid       |
    |no of space|no of *|no of space|no of *|
 1  |     3     |   1   |     3     |   1   |
 2  |     2     |   2   |     2     |   2   |
 3  |     1     |   3   |     1     |   3   |
 4  |     0     |   4   |     0     |   4   |
 --------------------------------------------
 
'''
'''n=int(input("enter a number"))
for i in range(1,n+1):  #always for rows loop first because we cannot go back to the previous line
    for k in range(n,(i),-1): # always column
        print(" ",end="")
    for j in range(1,(i+1)): # always column
            print("* ",end="")
    print()'''
#LHS inverted Right angle triangle
'''
****
 ***
  **
   *

relationship table
i|k[explicit] |j
1|0  [till 1] |4-1
2|1-1[till 2] |4-2
3|1-2[till 3] |4-3
4|1-3[till 4] |4-4
i loop==>1 till(n+1)
[incerementing]    +ve step

k loop==>1 to i
[incerementing] +ve step

j loop==>n till (i-1)
[decerementing]    -ve step

'''
'''n=int(input("enter a number"))
for i in range(1,n+1):  #always for rows loop first because we cannot go back to the previous line
    for k in range(1,i): # always column
        print(" ",end="")
    for j in range(n,(i-1),-1): # always column
        print("*",end="")
    print() '''
#inverted pyramid
'''
* * * * 
 * * *
  * *
   *

comparision table


****                    |  * * * *
 ***                    |   * * *   
  **                    |    * *
   *                    |     *
---------------------------------------------
rows|   RHS             |     pyramid       |
    |no of space|no of *|no of space|no of *|
 1  |     0     |   4   |     0     |   4   |
 2  |     1     |   3   |     1     |   3   |
 3  |     2     |   2   |     2     |   2   |
 4  |     3     |   1   |     3     |   1   |
 --------------------------------------------
 
'''
'''n=int(input("enter a number"))
for i in range(1,n+1):  #always for rows loop first because we cannot go back to the previous line
    for k in range(1,i): # always column
        print(" ",end="")
    for j in range(n,(i-1),-1): # always column
        print("* ",end="")
    print() '''

#odd pyramid using 3rd variable
'''
   *
  ***
 *****
*******

relationship table
i|k[explicit] |j   |3rd variable(odd)
1|4-2[till 1] |1-1 |1
2|4-3[till 2] |1-3 |3
3|4-2[till 3] |1-5 |5
4| 0 [till 4] |1-7 |7
'''
'''n=int(input("enter a number"))
odd=1
for i in range(1,n+1):  #always for rows loop first because we cannot go back to the previous line
    for k in range(n,i,-1): # always column
        print(" ",end="")
    for j in range(1,odd+1): # always column
        print("*",end="")
    print() 
    odd+=2'''
#inverted odd pyramid using 3rd variable
'''
*******
 *****
  ***
   *


   '''
'''n=int(input("enter a number"))
odd=(n*2)-1
for i in range(1,n+1):  #always for rows loop first because we cannot go back to the previous line
    for k in range(1,i): # always column
        print(" ",end="")
    for j in range(odd,1-1,-1): # always column
        print("*",end="")
    print() 
    odd-=2'''
#parallelogram
'''
****
 ****
  ****
   ****
'''
'''n=int(input("enter a number"))
for i in range(1,n+1):  #always for rows loop first because we cannot go back to the previous line
    for k in range(1,i): # always column
        print(" ",end="")
    for j in range(1,n+1): # always column
        print("*",end="")
    print() 
'''
#inverted paralellogram
'''
    ****
   ****
  ****
 ****'''
'''n=int(input("enter a number"))
for i in range(1,n+1):  #always for rows loop first because we cannot go back to the previous line
    for k in range(n,i-1,-1): # always column
        print(" ",end="")
    for j in range(1,n+1): # always column
        print("*",end="")
    print() '''

#COMBINATIONAL PATTERNS
'''o/p
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
    for j in range(1,noc+1):
        print("*",end=" ")
    print()
    if i < n:
        noc+=1
    else:
        noc-=1
'''
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
#combinatinoal
#1)
'''
*
**
* *
*  *
*   *
*  *
* *
**
*
'''
'''n=int(input("enter the value"))
noc=1
for i in range(1,n*2):
    for j in range(1,noc+1):
        if j==1 or j== noc:
            print("*",end="")
        else:
            print(" ",end="")
        
    print()
    if i<n:
        noc+=1
    else:
        noc-=1'''
#2)


'''n=int(input("enter the number : "))
noc=1
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        if j==n or j== noc:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i < n:
        noc+=1
    else:
        noc-=1'''
#number patterns 
# at every updated row if the complete row displays the same value then it is printing the value present in the variable i
#at every updated row if it starts from the same point and moves till certain point or viseversa then it is printing the value present in the value present in the variable j
#if the pattern is of continueous series then it is a third variable 
#1)
'''
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''
'''n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()'''

#2)
'''
1 
1 2
1 2 3
1 2 3 4
'''
'''n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
#3)
'''
1 2 3 4 
1 2 3
1 2
1
'''
'''n=int(input("enter a number"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

#4)

'''
4 
4 3
4 3 2
4 3 2 1
'''
'''n=int(input("enter a number"))
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print()'''

#5)
'''
1 
2 1
3 2 1
4 3 2 1
'''
'''n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(i,1-1,-1):
        print(j,end=" ")
    print()'''

#6)
'''
4 3 2 1 
3 2 1
2 1
1
'''
'''n=int(input("enter a number"))
for i in range(n,0,-1):
    for j in range(i,1-1,-1):
        print(j,end=" ")
    print()'''

#7)
'''
1 2 3 4 
1     4
1     4
1 2 3 4
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()'''
#8)
'''
1 
0 1
1 0 1
0 1 0 1
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()'''
#9)
'''
1 0 0 0 
0 2 0 0
0 0 3 0
0 0 0 4
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print(i,end=" ")
        else:
            print("0",end=" ")
    print()'''
#10)
'''
1 0 0 1 
0 2 2 0
0 3 3 0
4 0 0 4
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or (i+j)==(n+1):
            print(i,end=" ")
        else:
            print("0",end=" ")
    print()'''

#11)
'''
1 0 0 4 
0 2 3 0
0 2 3 0
1 0 0 4
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or (i+j)==(n+1):
            print(j,end=" ")
        else:
            print("0",end=" ")
    print()'''


#12)
'''
1 1 1 1 
1 2 2 2 
1 2 3 3 
1 2 3 4
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()'''
#13)
'''
4 3 2 1 
3 3 2 1
2 2 2 1
1 1 1 1\4\4\\4
'''
'''n=int(input("enter the value"))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if i>j:
            print(j,end=" ")
        else:
            print(i,end=" ")
    print()'''
#14)
'''
1 2 3 4 
2 2 3 4
3 3 3 4
4 4 4 4
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<=j:
            print(j,end=" ")
        else:
            print(i,end=" ")
    print()'''

#15)
'''
4 4 4 4 
4 3 3 3
4 3 2 2
4 3 2 1
'''
'''n=int(input("enter the value"))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if i>j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()'''
#16)
'''
1 2 3 4 
5 6 7 8
9 10 11 12
13 14 15 16
'''
'''n=int(input("enter the value"))
count=1
for i in range(1,n+1):
    for j in range(1,n+1):
            print(count,end=" ")
            count+=1
    print()'''

#17
'''
1 2 3 4 
8 7 6 5
9 10 11 12
16 15 14 13
'''
'''n=int(input("enter the value"))
count1=1
count2=0
for i in range(1,n+1):
    for j in range(1,n+1):
            if i%2!=0:
                  print(count1,end=" ")
                  count2=count1
            else:
                  print(count2,end=" ")
                  count2-=1  
            count1+=1            
    print()
    count2=count2+n'''

#18
'''
1
3 2
4 5 6
10 9 8 7

'''
'''n=int(input("enter the value"))
count1=1
count2=0
for i in range(1,n+1):
    for j in range(1,i+1):
            if i%2!=0:
                  print(count1,end=" ")
                  count2=count1
            else:
                  print(count2,end=" ")
                  count2-=1  
            count1+=1            
    print()
    count2=(count2+i)+1'''
#Alphabetical patterns
#!)
'''
A
BB
CCC
DDDD
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end="")
    print()'''

#2)
'''
abcd
abc
ab
a
'''
'''n=int(input("enter the value"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(96+j),end="")
    print()'''

#3
'''
D
CC
BBB
AAAA
'''
'''n=int(input("enter the value"))
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(chr(64+i),end="")
    print()'''

#4
'''
ABCD
abcd
ABCD
abcd
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2!=0:
            print(chr(64+j),end="")
        else:
            print(chr(96+j),end="")
    print()'''
#5
'''
A
aB
AbC
aBcD
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print(chr(64+j),end="")
        else:
            print(chr(96+j),end="")  
    print()'''
#6
'''
DcBa
dCbA
DcBa
dCbA
'''

'''n=int(input("enter the value"))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if (i+j)%2==0:
            print(chr(64+j),end="")
        else:
            print(chr(96+j),end="")  
    print()
'''
#7
'''
abcd
abc
ab
a
ab
abc
abcd
'''
'''n=int(input("enter the number : "))
noc=n
for i in range(1,n*2):
    for j in range(1,noc+1):
        print(chr(96+j),end="")
    print()
    if i < n:
        noc-=1
    else:
        noc+=1'''
#8
'''
a b c d 
e f g h
i j k l
m n o p
'''
'''n=int(input("enter the value"))
count=97
for i in range(1,n+1):
    for j in range(1,n+1):
            print(chr(count),end=" ")
            count+=1
    print()'''