#7. GCD USING FACTOR CHECKING 

def gcd(n1, n2, i, current_gcd, lower):
    if i > lower:
        return current_gcd
    if n1 % i == 0 and n2 % i == 0:
        current_gcd = i
    return gcd(n1, n2, i + 1, current_gcd, lower)

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

lower = n1
if n2 < n1:
    lower = n2

res = gcd(n1, n2, 1, 1, lower)
print("GCD =", res)

'''1️⃣ CONCEPT (WITH EXAMPLE)

GCD (HCF) means:

The largest number that divides both numbers exactly

Example:

n1 = 12, n2 = 18
Common factors: 1, 2, 3, 6
GCD = 6

2️⃣ THINKING BEHIND THIS METHOD

Check all numbers starting from 1

If a number divides both n1 and n2, it is a common factor

Keep updating the largest common factor

Stop at the smaller number

This is a brute-force approach.

3️⃣ HOW RECURSION IS USED

Parameters:

i → current divisor being checked

current_gcd → stores largest common factor found so far

lower → smaller of n1 and n2

Base condition:

if i > lower → stop

4️⃣ TRACING (n1 = 12, n2 = 18)
i	n1%i	n2%i	current_gcd
1   0	     0	        1
2	0	     0	        2
3	0	     0	        3
4	0	     ✗	        3
5	✗	    ✗	       3
6	0	     0	        6
7…	—	     —	        6

5️⃣ STACK FLOW (SIMPLIFIED)
gcd(12,18,1,1,12)
 └─ gcd(12,18,2,1,12)
     └─ gcd(12,18,3,2,12)
         └─ ...
             └─ gcd(12,18,13,6,12) ← stop

6️⃣ RECURSIVE TREE

This is a single-path recursion:

i=1
└──2
   └──3
      └──...
         └──13

🔑 EXAM NOTE

This method is simple but inefficient because it 
checks all possible divisors.'''