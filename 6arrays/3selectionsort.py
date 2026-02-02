#🔹 Selection Sort – Concept
'''
Selection sort idea:

Divide the array into sorted and unsorted parts

In each pass:

Find largest (or smallest) element from the unsorted part

Place it in its correct position

Repeat until the array is sorted



Explanation

i → number of passes

actind = n-1-i → position where the largest element should go

Inner loop finds the maximum element in unsorted part

Swap it with the element at actind
'''
def createarray():
    l1 = []
    while True:
        try:
            n = int(input("enter a number: "))
            l1.append(n)
        except:
            return l1


def selectionsort(arr):
    n = len(arr)

    # number of passes
    for i in range(0, n-1):

        actind = n - 1 - i          # correct position for maximum element
        currmax = -2**31
        currmaxind = -1

        # find maximum element in unsorted part
        for j in range(0, n - i):
            if currmax < arr[j]:
                currmax = arr[j]
                currmaxind = j

        # swap max element to its correct position
        arr[actind], arr[currmaxind] = arr[currmaxind], arr[actind]


# main program
print("Enter values into the array:")
arr = createarray()

print("Array before sorting:", arr)
selectionsort(arr)
print("Array after sorting:", arr)
'''
Example
Before: [64, 25, 12, 22, 11]
Pass 1 → max = 64 → placed at end
Pass 2 → max = 25 → placed at 2nd last
...
After:  [11, 12, 22, 25, 64]


✔ Sorts in ascending order
'''

#Selection Sort (ASCENDING & DESCENDING in ONE program)
def createarray():
    l1 = []
    while True:
        try:
            n = int(input("enter a number: "))
            l1.append(n)
        except:
            return l1


def selectionsort(arr, order):
    n = len(arr)

    for i in range(0, n-1):
        ind = i

        for j in range(i+1, n):
            if order == "asc":
                if arr[j] < arr[ind]:
                    ind = j
            elif order == "desc":
                if arr[j] > arr[ind]:
                    ind = j

        arr[i], arr[ind] = arr[ind], arr[i]


# main program
print("Enter values into the array:")
arr = createarray()

print("Original array:", arr)

selectionsort(arr, "asc")
print("Ascending order:", arr)

selectionsort(arr, "desc")
print("Descending order:", arr)
'''
🔍 Example Run
Enter values into the array:
10
45
23
9
34
a
Original array: [10, 45, 23, 9, 34]
Ascending order: [9, 10, 23, 34, 45]
Descending order: [45, 34, 23, 10, 9]
'''
