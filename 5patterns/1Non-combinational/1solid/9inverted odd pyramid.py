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