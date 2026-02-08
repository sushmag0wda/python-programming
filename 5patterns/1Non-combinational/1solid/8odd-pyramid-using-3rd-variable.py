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
n=int(input("enter a number"))
odd=1
for i in range(1,n+1):  #always for rows loop first because we cannot go back to the previous line
    for k in range(n,i,-1): # always column
        print(" ",end="")
    for j in range(1,odd+1): # always column
        print("*",end="")
    print() 
    odd+=2
    
#inverted odd pyramid using 3rd variable
'''
*******
 *****
  ***
   *
   
'''
n=int(input("enter a number"))
odd=(n*2)-1
for i in range(1,n+1):  #always for rows loop first because we cannot go back to the previous line
    for k in range(1,i): # always column
        print(" ",end="")
    for j in range(odd,1-1,-1): # always column
        print("*",end="")
    print() 
    odd-=2