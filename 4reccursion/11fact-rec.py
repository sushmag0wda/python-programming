#11 FACTORIAL (using recursion)
'''🔹 Concept

Factorial of a number n is the product of all positive integers from 1 to n.

factorial(4) = 4 × 3 × 2 × 1 = 24
factorial(5) = 5 × 4 × 3 × 2 × 1 = 120

🔹 Recursive thinking (VERY IMPORTANT)

Recursion means:

Solve a big problem by reducing it into 
a smaller version of the same problem

So,

factorial(n) = n × factorial(n−1)

Base condition
factorial(1) = 1
factorial(0) = 1


Without base condition → infinite recursion

🔹 Example: factorial(4)

Think like this:

factorial(4)
= 4 × factorial(3)
= 4 × (3 × factorial(2))
= 4 × (3 × (2 × factorial(1)))
= 4 × 3 × 2 × 1
= 24

🔹 Code '''
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

n = int(input("enter a number: "))
res = factorial(n)
print(res)

'''🔹 Stack Flow
factorial(4)
 → factorial(3)
   → factorial(2)
     → factorial(1) → return 1
     ← 2×1 = 2
   ← 3×2 = 6
 ← 4×6 = 24
'''