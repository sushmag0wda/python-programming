#1️⃣ createarray() function
def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number"))
            l1.append(n)
        except Exception as e:
            return l1

'''What this does:

Creates an empty list l1

Runs an infinite loop (while True)

Keeps asking the user to enter numbers

Adds each number to the list using append()

Why try–except?

If the user enters anything that is not a number (like a letter),

int(input()) causes an error

Control goes to except

The function stops input and returns the list

📌 Example input:

10
25
7
a   ← stops here


📌 Returned list:

[10, 25, 7]'''
#Check target element in an array

def checktarget(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # target found at index i
    return -1          # target not found

# main program
print("Enter elements into the array:")
arr = createarray()
target = int(input("Enter target element: "))
index = checktarget(arr, target)
if index!=-1:
    print(f"Target element {target} found at index {index}")
else:
    print(f"Target element {target} not found in the array")


'''🔹 How it works (short explanation)
1️⃣ createarray()

Keeps taking numbers from the user

Stops when a non-number is entered

Returns the list (array)

2️⃣ checktarget(arr, target)

Traverses the array using a loop

Compares each element with target

Returns:

index → if found

-1 → if not found

🔹 Sample Run
Enter elements into the array:
10
20
30
40
a
Enter target element: 30
Target element 30 found at index 2

🔹 Logic in one line (exam tip 📝)

Traverse the array and compare each element with the target.
If matched, return its index; otherwise, report not found.'''

#2️⃣ findlargest(arr) function
def findlargest(arr):
    max,maxind=-2147483648,-1         #note      2147483648 this can be written as 2^31
    for i in range(0,len(arr)):
        if max<arr[i]:
            max=arr[i]
            maxind=i
    return max,maxind


'''What’s happening here:

max is initialized to a very small number

maxind stores the index of the largest value

Loop goes through every element in the array

If current element is greater than max:

Update max

Store its index in maxind

📌 Example:

arr = [10, 25, 7]

Result:

max = 25
index = 1'''

#3️⃣ findsmallest(arr) function
def findsmallest(arr):
    min,minind=+2147483648,-1
    for i in range(0,len(arr)):
        if min>arr[i]:
            min=arr[i]
            minind=i
    return min,minind

'''What this does:
min starts with a very large number
Compares each element in the array
If current element is smaller than min:
Update min
Save its index

📌 Example:

arr = [10, 25, 7]

Result:

min = 7
index = 2'''

#4️⃣ Main execution part
print("enetr val into the array: ")
arr=createarray()
res,resind=findlargest(arr)
res1,res1ind=findsmallest(arr)
print(f"the max element is {res} stored in {resind}")
print(f"the min element is {res1} stored in {res1ind}")

#the max element is 25 stored in 1
#the min element is 7 stored in 2

'''🔑 Key concepts used

Functions

Lists (arrays)

Looping

Indexing

Exception handling (try-except)

Returning multiple values'''

'''
🔢 Let’s break it down
2147483648=2^31
Why this number shows up so often

2³¹ − 1 = 2147483647 → maximum value of a 32-bit signed integer

−2³¹ = −2147483648 → minimum value

So in your code:

max = -2147483648   # -2^31
min =  2147483648   #  2^31


You used them as:

a very small number for finding max

a very large number for finding min

That guarantees any real input will replace them.

🧠 Python tip (cleaner way)

In Python, you don’t need these magic numbers:

max_val = float('-inf')
min_val = float('inf')


Or even simpler:

max_val = arr[0]
min_val = arr[0]

Quick power-of-2 reference
Power	Value
2¹⁰	1024
2²⁰	1,048,576
2³⁰	1,073,741,824
2³¹	2,147,483,648 ✅
'''