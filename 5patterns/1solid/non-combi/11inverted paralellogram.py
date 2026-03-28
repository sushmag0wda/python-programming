#inverted paralellogram
'''
    ****
   ****
  ****
 ****'''
n=int(input("enter a number"))
for i in range(1,n+1):  #always for rows loop first because we cannot go back to the previous line
    for k in range(n,i-1,-1): # always column
        print(" ",end="")
    for j in range(1,n+1): # always column
        print("*",end="")
    print() 