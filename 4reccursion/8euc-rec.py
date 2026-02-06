#8. EUCLIDEAN ALGORITHM (MODULUS METHOD)

def findHCF(n1, n2):
    if n1 == 0:
        return n2
    if n1 < n2:
        n1, n2 = n2, n1
    return findHCF(n1 % n2, n2)

n1 = int(input("enter a first number"))
n2 = int(input("enter a second number"))
res = findHCF(n1, n2)
print(res)

'''1️⃣ CONCEPT (WITH EXAMPLE)

Euclidean Algorithm is based on the rule:

GCD(a, b) = GCD(b, a % b)

Example:

GCD(48, 18)
48 % 18 = 12 → GCD(18, 12)
18 % 12 = 6  → GCD(12, 6)
12 % 6 = 0   → GCD = 6

2️⃣ WHY THIS WORKS

Remainder keeps getting smaller

Eventually remainder becomes 0

When remainder is 0, the divisor is the GCD

3️⃣ TRACING
n1	n2	n1 % n2
48	18	12
18	12	6
12	6	0
4️⃣ STACK FLOW
findHCF(48,18)
 └─ findHCF(12,18)
     └─ findHCF(6,12)
         └─ findHCF(0,6) ← base
             return 6

5️⃣ RECURSIVE TREE
(48,18)
└──(12,18)
   └──(6,12)
      └──(0,6)

🔑 EXAM NOTE

Euclidean algorithm is efficient and widely used.'''

