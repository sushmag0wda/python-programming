#Array Left Rotation

'''Left rotation means shifting elements to the left, and the removed elements come to the end.

Example
Array = [1, 2, 3, 4, 5]
Rotate by 2

After rotation = [3, 4, 5, 1, 2]

Program: Left Rotate an Array'''
def createarray():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number: "))
            l1.append(n)
        except:
            return l1

def left_rotate(arr, k):
    n = len(arr)
    k = k % n   # handle rotations > length

    for _ in range(k):
        first = arr[0]
        for i in range(0, n-1):
            arr[i] = arr[i+1]
        arr[n-1] = first

# Main program
print("Enter values for the array:")
arr = createarray()

k = int(input("Enter number of left rotations: "))

print("Array before rotation:", arr)
left_rotate(arr, k)
print("Array after left rotation:", arr)

#using recursion

def createarray():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number: "))
            l1.append(n)
        except:
            return l1

def left_rotate_one(arr, n):
    first = arr[0]
    for i in range(0, n-1):
        arr[i] = arr[i+1]
    arr[n-1] = first

def left_rotate_rec(arr, k, n):
    if k == 0:
        return
    left_rotate_one(arr, n)
    left_rotate_rec(arr, k-1, n)

# Main program
print("Enter values for the array:")
arr = createarray()

k = int(input("Enter number of left rotations: "))
k = k % len(arr)

print("Array before rotation:", arr)
left_rotate_rec(arr, k, len(arr))
print("Array after left rotation:", arr)

'''Example Run
Enter values for the array:
1
2
3
4
5
a
Enter number of left rotations: 2
Array before rotation: [1, 2, 3, 4, 5]
Array after left rotation: [3, 4, 5, 1, 2]

Notes (Exam-Friendly)

Each rotation shifts elements one position left

First element moves to the end

k % n avoids extra rotations

Time Complexity: O(n × k)

Space Complexity: O(1)'''