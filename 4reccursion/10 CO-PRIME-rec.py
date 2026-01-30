#10 CO-PRIME CHECK USING GCD
'''1️⃣ Concept: What are Co-Prime numbers?

Two numbers are called co-prime if:

Their GCD (HCF) is 1

📌 They do NOT need to be prime numbers themselves

Examples:

(8, 15) → GCD = 1 → ✅ Co-prime

(14, 21) → GCD = 7 → ❌ Not co-prime

(9, 10) → GCD = 1 → ✅ Co-prime

2️⃣ Logic (Think like this 🧠)

Take two numbers from user

Find their GCD using Euclidean method

If GCD == 1 → Co-prime

Else → Not co-prime

3️⃣ Recursive GCD (Euclidean – Modulo Method)
Why modulo?

Because it is faster and cleaner, and commonly used for co-prime check.

4️⃣ Code '''
def findHCF(n1, n2):
    if n2 == 0:
        return n1
    return findHCF(n2, n1 % n2)

n1 = int(input("enter first number: "))
n2 = int(input("enter second number: "))

gcd = findHCF(n1, n2)

if gcd == 1:
    print("Co-prime numbers")
else:
    print("Not co-prime numbers")
'''
5️⃣ Example Walkthrough
Input:
n1 = 9
n2 = 10

GCD calculation:
9 % 10 = 9  → (10,9)
10 % 9 = 1  → (9,1)
9 % 1 = 0   → stop
GCD = 1


👉 Since GCD = 1 → Co-prime

6️⃣ Tracing Table
Call	n1	n2	n1 % n2
1	9	10	9
2	10	9	1
3	9	1	0
4	1	0	return 1
7️⃣ Stack Flow Diagram
findHCF(9,10)
   ↓
findHCF(10,9)
   ↓
findHCF(9,1)
   ↓
findHCF(1,0) → return 1

8️⃣ Recursive Tree
(9,10)
   |
(10,9)
   |
(9,1)
   |
(1,0)  ← GCD

9️⃣ Important Exam Notes ✍️

✔ Co-prime condition: GCD = 1
✔ Uses Euclidean algorithm
✔ Efficient and widely used
✔ Works for any integers

🔟 One-line definition (Exam ready)

Two numbers are said to be co-prime if their 
GCD is equal to 1.'''