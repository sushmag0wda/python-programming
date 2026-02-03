#integer num to string num
'''Example
Input : 123

Steps:
123 % 10 = 3 → chr(3 + 48) = '3'
12  % 10 = 2 → chr(2 + 48) = '2'
1   % 10 = 1 → chr(1 + 48) = '1'

Result → "123"

🔹 Code (using digit + 48)'''
def int_to_char(num):
    res = ""
    while num > 0:
        rem = num % 10
        res = chr(rem + 48) + res
        num = num // 10
    return res

n = int(input("Enter number: "))
print(int_to_char(n))