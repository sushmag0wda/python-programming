#Search in a Rotated Sorted Array
'''Example
Array = [4, 5, 6, 7, 0, 1, 2]
Target = 0
Output = Index 4


The array was originally sorted, then rotated.

Program: Search in Rotated Sorted Array (Binary Search Based)'''

def createarray():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number: "))
            l1.append(n)
        except:
            return l1

def search_rotated(arr, tar):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == tar:
            return mid

        # Left half is sorted
        if arr[start] <= arr[mid]:
            if arr[start] <= tar < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        # Right half is sorted
        else:
            if arr[mid] < tar <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1

# Main program
print("Enter values for the rotated sorted array:")
arr = createarray()
tar = int(input("Enter the target element: "))

print("Given array:", arr)
index = search_rotated(arr, tar)

if index != -1:
    print(f"Target element {tar} found at index {index}")
else:
    print(f"Target element {tar} not found")

'''Example Run
Enter values for the rotated sorted array:
4
5
6
7
0
1
2
a
Enter the target element: 0
Given array: [4, 5, 6, 7, 0, 1, 2]
Target element 0 found at index 4

Explanation (Exam-Friendly)

This is a modified binary search.

At every step:

One half of the array is always sorted.

Steps:

Find mid

Check if target == arr[mid]

Identify which half is sorted

Decide whether target lies in the sorted half

Move start or end accordingly

Repeat until found or search space ends.

Notes 📝

Works on rotated sorted arrays

No extra space used

Time Complexity: O(log n)

Space Complexity: O(1)'''