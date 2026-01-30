#2. COUNT DIGITS IN A NUMBER
'''
1️⃣ CONCEPT (EXAMPLE)

Number = 4567

Think like this:

Last digit = 7 → count = 1
Remaining number = 456

Last digit = 6 → count = 1 + 1 = 2
Remaining number = 45

Last digit = 5 → count = 1 + 1 + 1 = 3
Remaining number = 4

Last digit = 4 → count = 1 + 1 + 1 + 1 = 4
Remaining number = 0

Number becomes 0 → stop

✅ Final Result

Total number of digits = 4

2️⃣ LOGIC

Remove one digit each time using n // 10

Each removal adds 1 to count

Stop when n == 0

3️⃣ CODE'''

def countDigits(n, count):
    if n <= 0:
        return count
    n //= 10
    count += 1
    return countDigits(n, count)

n = int(input("enter a number"))
res = countDigits(n, 0)
print("count of digits =", res)

'''
4️⃣ TRACING (n = 123)
| Call | n   | count      |
| ---- | --- | ---------- |
| 1    | 123 | 0          |
| 2    | 12  | 1          |
| 3    | 1   | 2          |
| 4    | 0   | 3 ← return |

5️⃣ STACK FLOW
countDigits(123, 0)
 └─ countDigits(12, 1)
     └─ countDigits(1, 2)
         └─ countDigits(0, 3) ← base


6️⃣ RECURSIVE TREE
123
└──12
   └──1
      └──0
      
'''
