#Bubble Sort Program
def createarray():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number: "))
            l1.append(n)
        except:
            return l1

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]

# main program
print("Enter values for the array:")
arr = createarray()

print("Array before sorting:", arr)
bubble_sort(arr)
print("Array after sorting:", arr)

'''Example Run
Enter values for the array:
5
2
9
1
3
a
Array before sorting: [5, 2, 9, 1, 3]
Array after sorting: [1, 2, 3, 5, 9]


✅ Notes:

Bubble Sort Logic: Compare each element with the next and swap if it’s greater.

Passes: After each pass, the largest element “bubbles” to the end.

Time Complexity: O(n²)

Space Complexity: O(1) (in-place sorting)

Works for any size array.'''