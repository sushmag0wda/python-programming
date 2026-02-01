#RHS right angle triangle
'''
   *
  **
 ***
****


🧠 Just observe (most important)
Each row has two parts:

[spaces][stars]
✅ What happens row by row
As rows go down:

spaces go down

stars go up

That’s it. That’s the whole pattern.

✅ Row control (i loop)
i → 1 to n
Why?

Pattern starts small

Grows line by line

✅ Spaces logic (k loop)
spaces = n - i
Why?

First row → max spaces

Each next row → one space less

Last row → zero spaces

So:

k → n to i
✅ Stars logic (j loop)
stars = i
Why?

Row number = star count

Each row adds exactly one star

So:

j → 1 to i
✅ One-line understanding (remember this)
Right side pattern = print spaces first, then stars

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
n=int(input("enter a number"))
for i in range(1,n+1):  #always for rows loop first because we cannot go back to the previous line
    for k in range(n,(i),-1): # always column
        print(" ",end="")
    for j in range(1,(i+1)): # always column
            print("*",end="")
    print()