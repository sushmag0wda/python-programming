#subarray concept

# Subarray:
# Continuous part of an array (elements must be adjacent)
# Example: arr = [1,2,3]
# Subarrays = [1], [2], [3], [1,2], [2,3], [1,2,3]

# Subsequence:
# Derived by deleting some elements without changing order
# Elements need NOT be continuous
# Example: arr = [1,2,3]
# Subsequences = [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3], []

# Subset:
# Any selection of elements (order does not matter)
# Total subsets = 2^n
# Example: arr = [1,2]
# Subsets = [], [1], [2], [1,2]

# Substring (for strings):
# Continuous part of a string
# Example: s = "abc"
# Substrings = "a", "b", "c", "ab", "bc", "abc"

# Maximum Subarray Problem:
# Find the contiguous subarray with maximum sum
# Example: arr = [-2,1,-3,4,-1,2,1,-5,4]
# Maximum subarray = [4,-1,2,1], Sum = 6
# Maximum Subarray Problem (Kadane's Algorithm)
def maxSubArray(arr):
    max_sum = -2**31   # initialize to very small number
    current_sum = 0

    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0

    return max_sum


# -------- main part --------
arr = []
print("Enter array elements (enter non-number to stop):")
while True:
    try:
        n = int(input())
        arr.append(n)
    except:
        break

print("Maximum subarray sum is:", maxSubArray(arr))
'''🔹 Example Run
Input:  -2 1 -3 4 -1 2 1 -5 4 x
Output: Maximum subarray sum is: 6
Explanation: [4, -1, 2, 1] → sum = 6

🔹 Notes
max_sum initialized to very small number to handle all negative arrays.

current_sum reset to 0 whenever sum becomes negative.

Time Complexity: O(n)

Space Complexity: O(1)'''