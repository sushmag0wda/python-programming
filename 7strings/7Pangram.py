#Pangram

'''What is a Pangram?

A pangram is a sentence/string that contains all 26 letters of the English alphabet at least once.

✅ Example

"The quick brown fox jumps over the lazy dog" → ✅ Pangram

"Hello world" → ❌ Not a pangram

🧠 Idea

Ignore case (A = a)

Consider only alphabets (a–z)

If count of unique letters = 26 → pangram'''

'''🧠 Pangram Logic (Code-Level Explanation with Example)
Example Input
"The quick brown fox"

Step 1: Take an empty dictionary
d = {}


This dictionary will store alphabets as keys.

Step 2: Traverse each character of the string
for ch in s:


Character-by-character traversal:

T  h  e     q  u  i  c  k

Step 3: Convert uppercase to lowercase
if 'A' <= ch <= 'Z':
    ch = chr(ord(ch) + 32)


Example:

'T' → 't'

Step 4: Check if character is an alphabet
if 'a' <= ch <= 'z':


Letters → allowed

Space / number / symbol → ignored

Step 5: Store alphabet in dictionary
d[ch] = 1


Dictionary after few steps:

{'t':1}
{'t':1, 'h':1}
{'t':1, 'h':1, 'e':1}
...


👉 Duplicate letters overwrite, but dictionary keeps only unique keys.

Step 6: After loop, count dictionary keys
if len(d) == 26:


26 keys → pangram

<26 keys → not pangram

✅ Code (Using Dictionary, No Inbuilt Functions)'''
def pangram(s):
    d = {}

    for ch in s:
        # convert uppercase to lowercase
        if 'A' <= ch <= 'Z':
            ch = chr(ord(ch) + 32)

        # consider only alphabets
        if 'a' <= ch <= 'z':
            d[ch] = 1

    if len(d) == 26:
        return True
    else:
        return False


s = input("enter a string: ")

if pangram(s):
    print("pangram")
else:
    print("not pangram")

#✍️ Short Comment Version (Exam-Friendly)
# store each alphabet as key in dictionary
# ignore spaces and symbols
# if dictionary size becomes 26 → pangram