#triangular patterns
#a)LHS right angle triangle
'''
*
**
***
****

✅ Relationship
Row (i)	Stars
1	    1
2	    2
3	    3
4	    4

Thinking Stars increase with row number

✅ Logic

i → 1 to n

j → 1 to i

✅ Stars depend on row

'''
n=int(input("enter a number"))
for i in range(1,(n+1)):  #always for rows loop first because we cannot go back to the previous line
    for j in range(1,(i+1)): # always column
        print("*",end="")
    print() 