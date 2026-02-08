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
--------------------------------------------------
rows|   RHS             |     pyramid            |
    |no of space|no of *|rows|no of space|no of *|
 1  |     0     |   4   |  1 |     0     |   4   |
 2  |     1     |   3   |  2 |     1     |   3   |
 3  |     2     |   2   |  3 |     2     |   2   |
 4  |     3     |   1   |  4 |     3     |   1   |
 -------------------------------------------------
 
'''
n=int(input("enter a number"))
for i in range(1,n+1):  #always for rows loop first because we cannot go back to the previous line
    for k in range(1,i): # always column
        print(" ",end="")
    for j in range(n,(i-1),-1): # always column
        print("* ",end="")
    print() 