#LHS inverted Right angle triangle
'''
****
***
**
*

✅ Relationship
Row	    Stars
1	    n
2	    n-1
3	    n-2
4	    1
Thinking Stars decrease each row

✅ Logic

i → n to 1

j → 1 to i

✅ Reverse of previous pattern
'''
n=int(input("enter a number"))
for i in range(n,(1-1),-1):  #always for rows loop first because we cannot go back to the previous line
    for j in range(1,(i+1)): # always column
        print("*",end="")
    print()