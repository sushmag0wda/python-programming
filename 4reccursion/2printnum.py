#1. PRINT NUMBERS FROM 1 TO N
'''
1️⃣ CONCEPT (REAL-LIFE EXAMPLE)

Imagine your teacher says:

“Stand in a line and call your friend who has number one less than you
and ask them to stand first.
After they stand, you stand.”

If you are number 5, you will say:

“4, you go first”

4 says “3, you go first”

…

1 says “0, stop”

Then everyone stands in order:
👉 1 → 2 → 3 → 4 → 5

That’s recursion.

2️⃣ NORMAL THINKING (WITHOUT CODE)

To print 1 to n:

You cannot print n until 1 is printed

So first reach 1

Then print while coming back

3️⃣ RECURSIVE IDEA

Base condition: when n == 0 → stop

Recursive call: printTillN(n-1)

Print after recursive call

4️⃣ CODE'''

def printTillN(n):
    if n == 0:
        return
    printTillN(n - 1)
    print(n, end=" ")

n = int(input("Enter the number: "))
printTillN(n)

'''
5️⃣ TRACING (n = 3)

printTillN(3)
printTillN(2)
printTillN(1)
printTillN(0) → stop
print 1
print 2
print 3

5️⃣ STACK FLOW DIAGRAM
printTillN(3)
 └─ printTillN(2)
     └─ printTillN(1)
         └─ printTillN(0) ← base
         ↑ print 1
     ↑ print 2
 ↑ print 3
6️⃣ RECURSIVE TREE
3
└──2
   └──1
      └──0
'''