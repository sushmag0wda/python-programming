#Two Sum – Dictionary Approach
'''Idea:

Use a dictionary to store number → index

For each element:

Calculate remaining = target - nums[i]

If remaining exists in dictionary → answer found

Else store current element in dictionary

✅ Code (Dictionary Approach)'''
class Solution:
    def twoSum(self, nums, target):
        d = {}

        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in d:
                return [d[rem], i]

            d[nums[i]] = i

        return [-1, -1]


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

obj = Solution()                  # create object
result = obj.twoSum(nums, target) # call method using object

if result != [-1, -1]:
    print("Indices are:", result)
else:
    print("No two elements found with given target")


'''🔹 Example
nums = [2, 7, 11, 15]
target = 9


Step-by-step:

i=0 → rem=7 → not in dict → store {2:0}

i=1 → rem=2 → found in dict → return [0,1]

✔ Output → [0, 1]

🔹 Time & Space Complexity

Time: O(n)

Space: O(n)

🔹 Why Dictionary is Better?

Avoids nested loops

Faster for large inputs

Most interview-preferred solution'''