'''#Anagram
🔹 What is an Anagram?

Two strings are called anagrams if:

They contain the same characters

With the same frequency

But order can be different

🔹 Examples
"listen"  ↔  "silent"     ✅ anagram
"race"    ↔  "care"       ✅ anagram
"heart"   ↔  "earth"      ✅ anagram


❌ Not anagrams:

"hello" ↔ "helo"   (missing one 'l')
"aab"   ↔ "abb"    (different frequency)

🔹 Important Rules

Length of both strings must be same

Character count must be same

Case sensitivity depends on problem (usually convert to lowercase)

🔹 Ways to Check Anagram
1️⃣ Sorting Method

Sort both strings

If equal → anagram

Example:

"listen" → eilnst
"silent" → eilnst

2️⃣ Frequency Count Method (Best)

Count characters using dictionary / array

Compare counts

Example:

"anagram"
a → 3
n → 1
g → 1
r → 1
m → 1

🔹 Real-Life Use Cases

Word games

Spell checkers

Search optimization

String comparison problems (LeetCode)

🔹 One-line Definition (Exam-friendly)
# Anagram: Two strings having same characters with same frequency but different order'''


#WAP to find if 2 strings are anagram without sorting
'''🧠 Idea (Without Sorting)

If lengths are different → not anagram

Count frequency of each character in first string

Reduce frequency using second string

If all counts become zero → anagram

✅ Python Code (WITHOUT sorting)'''
def isAnagram(s1, s2):
    # Step 1: Length check
    if len(s1) != len(s2):
        return False

    count = {}

    # Step 2: Count characters of first string
    for ch in s1:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    # Step 3: Reduce count using second string
    for ch in s2:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False

    return True


# Main part
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if isAnagram(s1, s2):
    print("Strings are Anagrams")
else:
    print("Strings are NOT Anagrams")

'''🧪 Example Run
Enter first string: listen
Enter second string: silent
Strings are Anagrams
'''