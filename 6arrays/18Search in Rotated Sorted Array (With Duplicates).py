#Search in Rotated Sorted Array (With Duplicate Values)
'''Example
Array  = [2, 5, 6, 0, 0, 1, 2]
Target = 0
Output = Found (index may vary)

Program: Rotated Binary Search with Duplicates'''
def createarray():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number: "))
            l1.append(n)
        except:
            return l1

def search_rotated_dup(arr, tar):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == tar:
            return mid

        # If duplicates block the decision
        if arr[start] == arr[mid] == arr[end]:
            start += 1
            end -= 1

        # Left half is sorted
        elif arr[start] <= arr[mid]:
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
print("Enter values for the rotated sorted array (with duplicates):")
arr = createarray()
tar = int(input("Enter the target element: "))

print("Given array:", arr)
index = search_rotated_dup(arr, tar)

if index != -1:
    print(f"Target element {tar} found at index {index}")
else:
    print(f"Target element {tar} not found")

'''Example Run
Enter values for the rotated sorted array:
2
5
6
0
0
1
2
a
Enter the target element: 0
Given array: [2, 5, 6, 0, 0, 1, 2]
Target element 0 found at index 3

Explanation (Very Important for Exams)

Normally, binary search checks which half is sorted.

Problem with duplicates:

arr[start] == arr[mid] == arr[end]


→ cannot determine sorted half.

Solution:

Shrink search space

start += 1

end -= 1

Continue binary search logic.

Notes 📝

Works even when duplicate values exist

Index returned can be any valid index

Worst Case Time Complexity: O(n) (all duplicates)

Average Case: O(log n)

Space Complexity: O(1)'''