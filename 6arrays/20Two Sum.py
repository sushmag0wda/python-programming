#Two Sum

'''Given an array nums and an integer target,
return the indices of the two numbers such that they add up to target.

✔ You may assume exactly one solution exists
✔ You cannot use the same element twice

🔹 Example
nums = [2, 7, 11, 15]
target = 9
Output = [0, 1]


Because:

nums[0] + nums[1] = 2 + 7 = 9

Two Sum – Array Approach (Full Program)'''
def twoSum(nums, target):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

    return [-1, -1]   # if no pair found


# -------- main part --------
nums = []
print("Enter array elements (enter non-number to stop):")

while True:
    try:
        n = int(input())
        nums.append(n)
    except:
        break

target = int(input("Enter target value: "))

result = twoSum(nums, target)

if result != [-1, -1]:
    print("Indices are:", result)
else:
    print("No two elements found with given target")

'''🔹 Example Run
Enter array elements (enter non-number to stop):
2
7
11
15
x
Enter target value: 9
Indices are: [0, 1]

🔹 Key Points (exam-friendly)

Uses nested loops

Checks all pairs

Time Complexity: O(n²)

Space Complexity: O(1)'''