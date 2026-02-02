#Kth Missing Positive Number 👍
'''(LeetCode 1539 concept)

🔹 Problem

Given a sorted array of positive integers and an integer k, find the kth missing positive number.

Example
arr = [2, 3, 4, 7, 11]
k = 5

Missing numbers: 1, 5, 6, 8, 9, 10 ...
5th missing = 9

✅ Method 1: Simple Linear Scan (Easy to understand)
Logic

Start from num = 1

Traverse the array

If num is missing → decrease k

When k == 0, that number is the answer

Code (No inbuilt tricks)'''
def kthMissing(arr, k):
    i = 0
    num = 1

    while True:
        if i < len(arr) and arr[i] == num:
            i += 1
        else:
            k -= 1
            if k == 0:
                return num
        num += 1


arr = []
print("Enter array elements (sorted):")
while True:
    try:
        n = int(input())
        arr.append(n)
    except:
        break

k = int(input("Enter k value: "))

ans = kthMissing(arr, k)
print("Kth missing positive number is:", ans)

'''⏱ Time & Space

Time: O(n + k)

Space: O(1)

✅ Method 2: Binary Search (Optimized – Interview level)
Key Idea

Missing numbers till index i:

missing = arr[i] - (i + 1)'''

#Code (Binary Search)
def kthMissing(arr, k):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        missing = arr[mid] - (mid + 1)

        if missing < k:
            start = mid + 1
        else:
            end = mid - 1

    return start + k


arr = []
print("Enter array elements (sorted):")
while True:
    try:
        n = int(input())
        arr.append(n)
    except:
        break

k = int(input("Enter k value: "))

print("Kth missing positive number is:", kthMissing(arr, k))

'''⏱ Time & Space

Time: O(log n)

Space: O(1)

🔑 Exam Tip

If basics asked → Linear method

If optimized / LeetCode → Binary Search method'''