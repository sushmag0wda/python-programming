'''Maximum Product Subarray problem (LeetCode #152) 😄
This is like Kadane’s algorithm but a bit trickier because of negative numbers. Let me explain clearly.

🔹 Problem

Given an integer array, find the contiguous subarray with the maximum product.

Example:

arr = [2, 3, -2, 4]
Output = 6
Explanation: [2,3] → product = 6

🔹 Key Points

Product can become very small or very large.

Negative numbers can flip max ↔ min, so we track both max and min product at each step.

Initialize:

max_prod = arr[0]
min_prod = arr[0]
result = arr[0]'''

#✅ Code – Maximum Product Subarray
def maxProductSubarray(arr):
    max_prod = arr[0]
    min_prod = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):
        num = arr[i]
        if num < 0:
            # Swap max_prod and min_prod when negative
            max_prod, min_prod = min_prod, max_prod

        # Extend the subarray or start new
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)

        # Update result
        result = max(result, max_prod)

    return result


# -------- main part --------
arr = []
print("Enter array elements (enter non-number to stop):")
while True:
    try:
        n = int(input())
        arr.append(n)
    except:
        break

print("Maximum product subarray is:", maxProductSubarray(arr))

'''🔹 Example Run
Input:  2 3 -2 4 x
Output: Maximum product subarray is: 6


Explanation: [2,3] → 6

Input:  -2 0 -1 x
Output: 0

🔹 Complexity

Time: O(n)

Space: O(1)'''