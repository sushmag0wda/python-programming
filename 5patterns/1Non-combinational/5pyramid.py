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
------------------------|---------------------------
rows|   RHS             |rows  |  pyramid          |  
    |no of space|no of *|      |no of space|no of *|
 1  |     3     |   1   |  1   |   3       |   1   |
 2  |     2     |   2   |  2   |   2       |   2   |
 3  |     1     |   3   |  3   |   1       |   3   |
 4  |     0     |   4   |  4   |   0       |   4   |
 ---------------------------------------------------

just add a space after * no difference in logic
 
'''
n=int(input("enter a number"))
for i in range(1,n+1):  #always for rows loop first because we cannot go back to the previous line
    for k in range(n,(i),-1): # always column
        print(" ",end="")
    for j in range(1,(i+1)): # always column
            print("* ",end="")
    print()