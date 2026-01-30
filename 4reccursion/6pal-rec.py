#6. PALINDROME NUMBER 

def palindrome(n, temp, rev):
    if n <= 0:
        return temp == rev
    rem = n % 10
    rev = (rev * 10) + rem
    n //= 10
    return palindrome(n, temp, rev)

n = int(input("enter a number"))
rev = palindrome(n, n, 0)
print(rev)

'''1️⃣ CONCEPT (WITH EXAMPLE)

A palindrome number is a number that:

Reads the same forward and backward

Examples:

121 → palindrome
1331 → palindrome
123 → NOT palindrome

2️⃣ THINK LIKE THIS

To check palindrome:

Reverse the number

Compare it with the original number

If:

original == reversed


→ palindrome

3️⃣ WHY temp IS USED

n keeps changing during recursion

So we store original number in temp

At the end, we compare:

temp == rev

4️⃣ STEP-BY-STEP EXAMPLE (n = 121)

Last digit = 1 → rev = 1 → n = 12

Last digit = 2 → rev = 12 → n = 1

Last digit = 1 → rev = 121 → n = 0

Compare: 121 == 121 → True

5️⃣ TRACING TABLE
Call	n	rev
1   	121	1
2	    12	12
3	    1	121
4	    0	compare temp == rev
6️⃣ STACK FLOW DIAGRAM
palindrome(121, 121, 0)
 └─ palindrome(12, 121, 1)
     └─ palindrome(1, 121, 12)
         └─ palindrome(0, 121, 121) ← compare
             return True

7️⃣ RECURSIVE TREE
121
└──12
   └──1
      └──0

🔑 KEY EXAM POINTS (VERY IMPORTANT)

Reverse logic is reused for palindrome

temp stores original number

Base condition performs comparison

Returns True or False'''