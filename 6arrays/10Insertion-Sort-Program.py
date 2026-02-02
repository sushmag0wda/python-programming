#Insertion Sort Program
def createarray():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number: "))
            l1.append(n)
        except:
            return l1

def insertion_sort(arr):
    n = len(arr)
    # Traverse from 1 to n
    for i in range(1, n):
        key = arr[i]        # element to be inserted
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# main program
print("Enter values for the array:")
arr = createarray()

print("Array before sorting:", arr)
insertion_sort(arr)
print("Array after sorting:", arr)

'''Example Run
Enter values for the array:
8
3
5
1
6
a
Array before sorting: [8, 3, 5, 1, 6]
Array after sorting: [1, 3, 5, 6, 8]


✅ Notes:

Insertion Sort Logic:

Take each element from the unsorted part

Insert it into its correct position in the sorted part

Time Complexity: O(n²)

Space Complexity: O(1) (in-place sorting)

Good for small arrays and almost sorted arrays'''