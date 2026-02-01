#square pattern
'''
* * * * 
* * * * 
* * * *
* * * *
'''
'''Thinking

Rows = n

Columns = n

Nothing depends on i

Logic

i → 1 to n

j → 1 to n

Always print *

✅ Constant pattern'''

n=int(input("enter a number"))
for i in range(1,(n+1)):  #always for rows loop first because we cannot go back to the previous line
    for j in range(1,(n+1)): # always column
        print("*",end=" ")
    print()        
print("\n-------------------------------------------------------------------------------------------------------------------------")

'''#note- i loop is always dependent on n value
        -j loop is dependent on n,i,or 3rd valiable'''
