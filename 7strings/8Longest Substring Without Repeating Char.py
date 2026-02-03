#Longest Substring Without Repeating Characters
'''✅ Using Array / String only (NO dictionary)
💡 Logic (very short – write as comments)

Maintain a current substring (temp)

Traverse characters one by one

If character not in temp → add it

If character already in temp → remove characters from left until duplicate is gone

Track maximum length

✅ Code (Array / String Method)'''
def lengthOfLongestSubstring(s):
    temp = ""     # current substring without duplicates
    maxlen = 0

    for i in range(len(s)):
        if s[i] not in temp:
            temp = temp + s[i]
        else:
            # remove characters until duplicate is removed
            idx = temp.index(s[i])
            temp = temp[idx+1:] + s[i]

        maxlen = max(maxlen, len(temp))

    return maxlen


# -------- MAIN PART --------
s = input("Enter string: ")
print("Length of longest substring:", lengthOfLongestSubstring(s))

'''🧠 Example (important for understanding)
Input: "abba"

temp = "a"
temp = "ab"
'b' repeated → remove up to first 'b'
temp = "b"
temp = "ba"

Output = 2'''