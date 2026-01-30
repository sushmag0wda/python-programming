#9 Euclidean Subtraction Method – Idea

'''The idea is simple:

If you subtract the smaller number from the larger number repeatedly,
GCD does not change

Rule:

If n1 > n2 → subtract n2 from n1

If n2 > n1 → subtract n1 from n2

Repeat until both numbers become equal

That equal value is the GCD

3️⃣ Example (Think like this 🧠)

Find GCD of 20 and 12

20 - 12 = 8      → (8, 12)
12 - 8  = 4      → (8, 4)
8  - 4  = 4      → (4, 4)


Now both numbers are equal (4)
👉 GCD = 4

4️⃣ How to convert this idea into recursion
Recursive thinking:

Base case:
If n1 == n2, return n1

Recursive case:

If n1 > n2 → findHCF(n1 - n2, n2)

Else → findHCF(n1, n2 - n1)

5️⃣ Code (USER INPUT – same style as yours)'''

def findHCF(n1,n2):
    if n1==0:
        return n2
    if n1<n2:
        n1,n2=n2,n1
    return findHCF((n1-n2),n2)

n1=int(input("enter a first number"))
n2=int(input("enter a second number"))
res=findHCF(n1,n2)
print("HCF = "res)

'''6️⃣ Tracing the program (VERY IMPORTANT FOR EXAMS)

Input:

n1 = 20
n2 = 12

Call	n1	n2	Action
1	    20	12	20 > 12 → (20−12, 12)
2	    8	12	12 > 8 → (8, 12−8)
3	    8	4	8 > 4 → (8−4, 4)
4	    4	4	n1 == n2 → return 4
7️⃣ Stack Flow Diagram (Function Calls)
findHCF(20,12)
   ↓
findHCF(8,12)
   ↓
findHCF(8,4)
   ↓
findHCF(4,4)  → return 4


Now stack unwinds and prints 4.

8️⃣ Recursive Tree (Linear tree here)
(20,12)
   |
(8,12)
   |
(8,4)
   |
(4,4)  ← GCD


📌 Note: This recursion forms a single path, not branching.

9️⃣ Why this method works

Because:

Subtracting does not change common factors

You are slowly reducing numbers until only the greatest common factor remains

🔟 Important exam points to remember

✔ Base condition: n1 == n2
✔ Uses repeated subtraction
✔ Slower than modulo method
✔ Conceptually easy to understand
✔ Classic Euclidean approach'''