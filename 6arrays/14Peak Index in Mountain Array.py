#Peak Index in Mountain Array
'''
A mountain array is an array where elements first strictly increase to a peak and then strictly decrease.
If there are multiple equal peaks, we can return the first peak index.'''

def createarray():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number: "))
            l1.append(n)
        except:
            return l1

def peak_index_binary(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < arr[mid + 1]:
            start = mid + 1
        else:
            end = mid
    return start  # peak index

# Main program
print("Enter values for the mountain array:")
arr = createarray()

print(f"Given array: {arr}")
index = peak_index_binary(arr)
print(f"Peak element is {arr[index]} at index {index}")
'''Example
Enter values for the mountain array:
1
3
5
5
4
2
a
Given array: [1, 3, 5, 5, 4, 2]
Peak element is 5 at index 2


✅ Notes:

Works even if more than one peak exists, returns the first peak in the mountain.

Time Complexity: O(log n)

Space Complexity: O(1)'''