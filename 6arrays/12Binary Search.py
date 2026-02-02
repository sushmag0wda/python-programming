#Binary Search Program (Iterative)
def createarray():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number: "))
            l1.append(n)
        except:
            return l1

def binary_search(arr, tar):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == tar:
            return mid   # target found
        elif tar < arr[mid]:
            end = mid - 1  # search in left half
        else:
            start = mid + 1  # search in right half

    return -1  # target not found

# Main program
print("Enter values into the array in sorted order:")
arr = createarray()
tar = int(input("Enter the target element: "))

print(f"Given array is: {arr}")
index = binary_search(arr, tar)

if index != -1:
    print(f"The target element {tar} is at index {index}")
else:
    print(f"The target element {tar} is not found")

'''Example Run
Enter values into the array in sorted order:
1
3
5
7
9
a
Enter the target element: 5
Given array is: [1, 3, 5, 7, 9]
The target element 5 is at index 2


✅ Notes:

Binary search only works on a sorted array.

Logic:

Check middle element.

If target < middle → search left half.

If target > middle → search right half.

Time Complexity: O(log n)

Space Complexity: O(1) for iterative version'''