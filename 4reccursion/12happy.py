#12 HAPPY NUMBER
'''🔹 Concept

A number is happy if:

Repeatedly sum the square of its digits

If result becomes 1 → happy

If result becomes 4 → unhappy

Why 4?
👉 All unhappy numbers eventually fall into a loop ending at 4

🔹 Example: n = 32
3² + 2² = 9 + 4 = 13
1² + 3² = 1 + 9 = 10
1² + 0² = 1


✅ Happy number

🔹 Recursive idea

Split digits using % 10

Square and sum

Call function again with new sum

🔹 Code '''
def happy(n):
    sum = 0
    if n == 1:
        return True
    elif n == 4:
        return False
    while n > 0:
        digit = n % 10
        sum += digit ** 2
        n //= 10
    return happy(sum)

n = int(input("enter the n: "))
res = happy(n)
if res:
    print("happy")
else:
    print("not happy")

'''🔹 Stack Flow (n = 32)
happy(32)
 → happy(13)
   → happy(10)
     → happy(1) → True

🧠 Final Exam Tips

✔ Always write base condition first
✔ Explain recursion as problem → smaller problem
✔ Draw stack flow for factorial
✔ Draw recursive tree for fibonacci(n)
✔ Mention 1 and 4 rule for happy numbers'''