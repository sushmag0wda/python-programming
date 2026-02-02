#Reverse an Array
def createarray():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number: "))
            l1.append(n)
        except:
            return l1

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        # Swap the elements
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# main program
print("Enter values for the array:")
arr = createarray()

print("Original array:", arr)
reverse_array(arr)
print("Reversed array:", arr)

'''Example Run
Enter values for the array:
1
2
3
4
5
a
Original array: [1, 2, 3, 4, 5]
Reversed array: [5, 4, 3, 2, 1]


✅ Notes:

Swaps elements from start and end moving toward the middle.

In-place reversal (no extra array used).

Works for arrays of any size.'''

#Reverse an Array Using Recursion
def createarray():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number: "))
            l1.append(n)
        except:
            return l1

def reverse_rec(arr, start, end):
    if start >= end:
        return
    # Swap first and last
    arr[start], arr[end] = arr[end], arr[start]
    # Recurse for the remaining subarray
    reverse_rec(arr, start + 1, end - 1)

# main program
print("Enter values for the array:")
arr = createarray()

print("Original array:", arr)
reverse_rec(arr, 0, len(arr) - 1)
print("Reversed array:", arr)

'''Example Run
Enter values for the array:
1
2
3
4
5
a
Original array: [1, 2, 3, 4, 5]
Reversed array: [5, 4, 3, 2, 1]'''