#RHS inverted Right angle triangle
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