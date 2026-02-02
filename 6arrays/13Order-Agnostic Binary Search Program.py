#Order-Agnostic Binary Search Program
# Order-Agnostic Binary Search:
# Works on sorted arrays in ascending or descending order
# Time Complexity: O(log n)

def createarray():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number: "))
            l1.append(n)
        except:
            return l1

def orbinary_search(arr, tar):
    start = 0
    end = len(arr) - 1

    # Determine the order of the array
    if arr[start] <= arr[end]:
        flag = "asc"
    else:
        flag = "desc"

    # Binary search
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == tar:
            return mid  # Target found

        if flag == "asc":
            if tar < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:  # descending
            if tar < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1

    return -1  # Target not found

# Main program
print("Enter values into the array in sorted order (ascending or descending):")
arr = createarray()
tar = int(input("Enter the target element: "))

print(f"Given array is: {arr}")
index = orbinary_search(arr, tar)

if index != -1:
    print(f"The target element {tar} is at index {index}")
else:
    print(f"The target element {tar} is not found")

'''Example Runs

Ascending array:

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


Descending array:

Enter values into the array in sorted order:
9
7
5
3
1
a
Enter the target element: 5
Given array is: [9, 7, 5, 3, 1]
The target element 5 is at index 2


✅ Notes:

Order-Agnostic: Works for both ascending and descending sorted arrays.

Logic:

First, check the first and last element to determine the order.

Then apply binary search accordingly.

Time Complexity: O(log n)

Space Complexity: O(1)'''