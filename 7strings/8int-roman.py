#Integer to Roman – Logic (with example in code)
'''Roman symbols:
I  = 1
IV = 4
V  = 5
IX = 9
X  = 10
XL = 40
L  = 50
XC = 90
C  = 100
CD = 400
D  = 500
CM = 900
M  = 1000

Idea:

Always subtract the largest possible Roman value

Append its symbol

Repeat until number becomes 0

✅ Code (Dictionary approach – very exam friendly)'''
def intToRoman(num):
    # key   → Roman symbol
    # value → Integer value
    roman = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    res = ""

    # Example: num = 58
    # 58 >= 50 → add "L", num = 8
    # 8  >= 5  → add "V", num = 3
    # 3  >= 1  → add "III", num = 0

    for key in roman:
        while num >= roman[key]:
            res = res + key
            num = num - roman[key]

    return res


# -------- MAIN PART --------
n = int(input("Enter an integer: "))
print("Roman numeral:", intToRoman(n))

'''🧠 Example Walkthrough 
Input: 1994

1994 >= 1000 → "M"   → num = 994
994  >= 900  → "CM"  → num = 94
94   >= 90   → "XC"  → num = 4
4    >= 4    → "IV"  → num = 0

Output: MCMXCIV'''
