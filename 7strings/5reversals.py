#Character Alignment Concepts (THEORY)

# Normal Alignment:
# If traversal is from LHS → store result in LHS
# If traversal is from RHS → store result in RHS

# Reverse Alignment:
# If traversal is from LHS → store result in RHS
# If traversal is from RHS → store result in LHS

'''
📌 Program: Reverse Each Word (Word-wise Reverse, Same Order)

👉 Example

Input : "hello world"
Output: "olleh dlrow"

Logic used:

Traverse from LHS

Store characters in reverse order (RHS) → reverse alignment'''

# Reverse each word but keep word order same
def reverse(s):
    s = s + " "
    nsen = ""
    nwrd = ""

    for i in range(len(s)):
        if s[i] != " ":
            nwrd = s[i] + nwrd
        elif nwrd != "":
            if nsen == "":
                nsen = nsen + nwrd
            else:
                nsen = nsen + " " + nwrd
            nwrd = ""
    return nsen

'''
📌 Program: Reverse Word Order (Sentence Reverse)

👉 Example

Input : "hello world"
Output: "world hello"

Logic used:

Traverse from LHS

Store words in LHS of result → reverse sentence'''

# Reverse the order of words in sentence
def reverse(s):
    s = s + " "
    nsen = ""
    nwrd = ""

    for i in range(len(s)):
        if s[i] != " ":
            nwrd = nwrd + s[i]
        elif nwrd != "":
            if nsen == "":
                nsen = nwrd + nsen
            else:
                nsen = nwrd + " " + nsen
            nwrd = ""
    return nsen

'''📌 Program: Reverse Word Order + Capitalize First Letter

👉 Example

Input : "hello world"
Output: "World Hello"

Extra feature:

First letter of each word → converted to uppercase
'''
# Reverse word order and capitalize first letter of each word
def reverse(s):
    s = s + " "
    nsen = ""
    nwrd = ""

    for i in range(len(s)):
        if s[i] != " ":
            if nwrd == "" and 'a' <= s[i] <= 'z':
                nwrd = nwrd + chr(ord(s[i]) - 32)
            else:
                nwrd = nwrd + s[i]
        elif nwrd != "":
            if nsen == "":
                nsen = nwrd + nsen
            else:
                nsen = nwrd + " " + nsen
            nwrd = ""
    return nsen

'''📌 Program: String Filter (Remove Special Characters & Lowercase)

👉 Example

Input : "A man, a plan!"
Output: "amanaplan"

Purpose:

Convert uppercase → lowercase

Remove special characters

Keep only alphabets and digits'''

# Filter string: lowercase + remove special characters
def strfilt(s):
    nstr = ""
    for i in range(len(s)):
        if 'A' <= s[i] <= 'Z':
            nstr = nstr + chr(ord(s[i]) + 32)
        elif ('a' <= s[i] <= 'z') or ('0' <= s[i] <= '9'):
            nstr = nstr + s[i]
    return nstr

'''📌 Program: Palindrome Check (Ignoring Case & Special Characters)

👉 Example

Input : "A man, a plan, a canal: Panama"
Output: Palindrome

Logic:

Filter string

Use two-pointer technique'''

# Check palindrome ignoring case and special characters
def palindrome(s):
    s1 = strfilt(s)
    i = 0
    j = len(s1) - 1

    while i < j:
        if s1[i] != s1[j]:
            return False
        i += 1
        j -= 1
    return True

'''✅ Final Classification Summary
Program No	|What it does
1	        |    Character alignment concepts
2	        |    Reverse each word
3	        |    Reverse word order
4	        |    Reverse word order + capitalize
5	        |    String filtering
6	        |    Palindrome check (cleaned string)'''

'''LeetCode 680 – Valid Palindrome II, clean and exam/interview-ready.

🔹 Problem (Valid Palindrome II)

You are given a string s.
You can delete at most one character.
Return True if the string can become a palindrome, else False.

🔹 Example
Input : "abca"
Output: True
Explanation: remove 'b' → "aca" (palindrome)

Input : "abc"
Output: False

✅ Code (Two Pointer Approach)'''
class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                # try skipping either left or right character
                return isPalindrome(i+1, j) or isPalindrome(i, j-1)
            i += 1
            j -= 1

        return True

#🔹 Logic (Short – write as comments)
# Use two pointers (i, j)
# If characters match → move inward
# On first mismatch:
#   try deleting left char OR right char
# If any case forms palindrome → True
