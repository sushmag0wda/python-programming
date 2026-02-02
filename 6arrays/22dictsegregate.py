'''You are given an integer array and you want to segregate elements into categories based on how many times they appear.

Definitions (very important for exams 👇)

Duplicate elements
👉 Elements that are repeated more than once
Example: [2, 3, 2] → 2

Unique elements
👉 Elements that appear exactly once
Example: [2, 3, 2] → 3

Non-duplicate elements
👉 Elements that are not repeated (appear once)
⚠️ This is actually the same as unique elements

So:

Unique elements == Non-duplicate elements

🔹 Concept 1: Dynamic Array Creation'''
def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number"))
            l1.append(n)
        except Exception as e:
            return l1

'''What’s happening?

Keeps taking input until the user enters a non-integer

Uses exception handling to stop input

Returns a list of integers

Concepts used:

while True → infinite loop

try-except → handles invalid input

Dynamic list creation

📌 Why this is useful:
We don’t need to know array size in advance.

🔹 Concept 2: Frequency Counting using Dictionary
dict={}
for i in range(0,len(arr)):
    if arr[i] in dict:
        dict[arr[i]]=dict[arr[i]]+1
    else:
        dict[arr[i]]=1

What is a dictionary?

Stores data as key : value

Here:

Key → array element

Value → number of times it appears

Example:

For input:

arr = [1, 2, 2, 3, 1]


Dictionary becomes:

{1:2, 2:2, 3:1}


📌 This technique is called frequency mapping
📌 Time complexity: O(n) (very efficient)

🔹 Concept 3: Segregating Elements
dup,nondup,uniq=[],[],[]'''

'''for key,value in dict.items():
    if value>1:
        dup.append(key)
    if value>=1:
        nondup.append(key)
    if value==1:
        uniq.append(key)

Meaning of each condition:
1️⃣ Duplicate elements
if value > 1:
    dup.append(key)


✔ Appears more than once

2️⃣ Unique elements
if value == 1:
    uniq.append(key)


✔ Appears exactly once

3️⃣ Non-duplicate elements ❌ (logical issue)
if value >= 1:
    nondup.append(key)


⚠️ This condition adds all elements, because every element appears at least once.

🔹 Important Correction (For Proper Notes)
According to definitions:
Non-duplicate elements = elements repeated only once


So nondup and uniq are the same.

Correct condition should be:
if value == 1:
    nondup.append(key)

🔹 Corrected Logic (Recommended)
for key,value in dict.items():
    if value > 1:
        dup.append(key)
    if value == 1:
        uniq.append(key)
        nondup.append(key)

🔹 Output Explanation
print(f"the given array is :{arr}")
print(f"the duplicates elements are :{dup}")
print(f"the nonduplicates elements are :{nondup}")
print(f"the unique elements are :{uniq}")


Displays original array

Shows segregated results clearly

🔹 Key Notes for Exams / Interviews 📝

Use dictionary for counting frequency

Avoid nested loops → improves performance

dict.items() gives both key and value

Unique = Non-duplicate

Time Complexity: O(n)

Space Complexity: O(n)'''
#WAP to segregate bwteen duplicated on duplicates and unique elements present in an integer array 
'''
duplicates-elements that are repeated more than once
unique elements-elements that are not repeated
nonduplicates-elements that are repeated only once
'''
def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number"))
            l1.append(n)
        except Exception as e:
            return l1
def segregate(arr):
    dict={}
    dup,nondup,uniq=[],[],[]
    for i in range(0,len(arr)):
        if arr[i] in dict:
            dict[arr[i]]=dict[arr[i]]+1
        else:
            dict[arr[i]]=1
    for key,value in dict.items():
        if value>1:
            dup.append(key)
        if value>=1:
            nondup.append(key)
        if value==1:
            uniq.append(key)
    return dup,nondup,uniq
    
print("enetr val into the array: ")
arr=createarray()
dup,nondup,uniq=segregate(arr)
print(f"the given array is :{arr}")
print(f"the duplicates elements are :{dup}")
print(f"the nonduplicates elements are :{nondup}")
print(f"the unique elements are :{uniq}")
