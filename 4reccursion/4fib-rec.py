#3. FIBONACCI SERIES 
'''CONCEPT (WHAT IS FIBONACCI?)

Fibonacci series is a sequence where
👉 each number is the sum of the previous two numbers.

The series usually starts with 0 and 1.

Example series:

0 1 1 2 3 5 8 ...

🔹 HOW TO THINK (WITH A REAL EXAMPLE)

Assume:

pos = 5
n1 = 0
n2 = 1


Think like this:

First number = 0 → print it
Next two numbers become 1 and 1

Second number = 1 → print it
Next two numbers become 1 and 2

Third number = 1 → print it
Next two numbers become 2 and 3

Fourth number = 2 → print it
Next two numbers become 3 and 5

Fifth number = 3 → print it
pos becomes 0 → stop

So output is:

0 1 1 2 3

🔹 RECURSIVE IDEA (VERY IMPORTANT)

Each recursive call:

Prints the current number (n1)

Moves to the next Fibonacci pair

Decreases pos by 1

Base condition:

When pos <= 0 → stop recursion

🔹 YOUR CODE'''
def fibonacci(pos, n1, n2):
    if pos <= 0:
        return
    print(n1, end=" ")
    fibonacci(pos - 1, n2, n1 + n2)

pos = int(input("Enter number of terms: "))
print("Fibonacci series:")
fibonacci(pos, 0, 1)
'''
🔹 TRACING (pos = 5)
Call	pos	n1	n2	Printed
1	    5	0	1	0
2	    4	1	1	1
3	    3	1	2	1
4	    2	2	3	2
5	    1	3	5	3
6	    0	—	—	stop
🔹 STACK FLOW DIAGRAM
fibonacci(5, 0, 1)
 └─ fibonacci(4, 1, 1)
     └─ fibonacci(3, 1, 2)
         └─ fibonacci(2, 2, 3)
             └─ fibonacci(1, 3, 5)
                 └─ fibonacci(0, 5, 8) ← base

🔹 RECURSIVE TREE

This program has no branching, so the tree is just a single path:

(5,0,1)
└──(4,1,1)
   └──(3,1,2)
      └──(2,2,3)
         └──(1,3,5)

🔑 KEY EXAM POINTS (MEMORIZE)

pos controls how many terms to print

n1 is the current Fibonacci number

n2 is the next Fibonacci number

Printing happens before recursive call

Single recursive call → no branching'''