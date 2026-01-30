#5. REVERSE OF A NUMBER 

def reversal(n, rev):
    if n <= 0:
        return rev
    rem = n % 10
    rev = (rev * 10) + rem
    n //= 10
    return reversal(n, rev)

n = int(input("enter a number"))
rev = reversal(n, 0)
print("reversal =", rev)

'''1️⃣ CONCEPT (WITH CLEAR EXAMPLE)

Let the number be:

n = 1234


To reverse a number, we:

Take the last digit

Add it to a new number

Remove that digit from the original number

Repeat until number becomes 0

2️⃣ THINK LIKE THIS (STEP BY STEP)

Number = 1234

Last digit = 4
New number = 0 * 10 + 4 = 4
Remaining number = 123

Last digit = 3
New number = 4 * 10 + 3 = 43
Remaining number = 12

Last digit = 2
New number = 43 * 10 + 2 = 432
Remaining number = 1

Last digit = 1
New number = 432 * 10 + 1 = 4321
Remaining number = 0

Number becomes 0 → stop

👉 Reversed number = 4321

3️⃣ HOW RECURSION FITS HERE

n → keeps getting smaller (n // 10)

rev → stores the result so far

Each recursive call handles one digit

Base condition: n <= 0

4️⃣ TRACING (n = 123)
Call	n	rem	rev
1	   123	3	3
2	   12	2	32
3	   1	1	321
4	   0	—	return 321

🔑 KEY EXAM POINT

The variable rev is used to store the reversed
number during recursive calls and is returned 
when the base condition is reached.'''