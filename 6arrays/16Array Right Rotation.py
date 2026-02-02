#Array Right Rotation
'''
Right rotation means shifting elements to the right, and the last element comes to the front.

Example
Array = [1, 2, 3, 4, 5]
Rotate by 2

After rotation = [4, 5, 1, 2, 3]

1️⃣ Right Rotation (Normal – Loop Based)'''
def createarray():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number: "))
            l1.append(n)
        except:
            return l1

def right_rotate(arr, k):
    n = len(arr)
    k = k % n

    for _ in range(k):
        last = arr[n-1]
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = last

# Main program
print("Enter values for the array:")
arr = createarray()

k = int(input("Enter number of right rotations: "))

print("Array before rotation:", arr)
right_rotate(arr, k)
print("Array after right rotation:", arr)

#2️⃣ Right Rotation Using Recursion
def createarray():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number: "))
            l1.append(n)
        except:
            return l1

def right_rotate(arr, k):
    n = len(arr)
    k = k % n

    for _ in range(k):
        last = arr[n-1]
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = last

# Main program
print("Enter values for the array:")
arr = createarray()

k = int(input("Enter number of right rotations: "))

print("Array before rotation:", arr)
right_rotate(arr, k)
print("Array after right rotation:", arr)
'''Example Run
Enter values for the array:
1
2
3
4
5
a
Enter number of right rotations: 2
Array before rotation: [1, 2, 3, 4, 5]
Array after right rotation: [4, 5, 1, 2, 3]

Exam Notes 📝

Right rotation shifts elements towards higher index

Last element moves to index 0

k % n avoids unnecessary rotations

Time Complexity: O(n × k)

Space Complexity:

Loop: O(1)

Recursion: O(k)'''