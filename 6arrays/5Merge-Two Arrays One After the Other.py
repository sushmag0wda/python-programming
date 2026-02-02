#Merge Two Arrays One After the Other
'''
a1 = [2, 1, 3]
a2 = [10, 11, 12]
Output = [2, 1, 3, 10, 11, 12]
'''
def createarray():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number: "))
            l1.append(n)
        except:
            return l1

def merge_one_after_other(arr1, arr2):
    res = []
    # add elements of first array
    for i in arr1:
        res.append(i)
    # add elements of second array
    for j in arr2:
        res.append(j)
    return res

# main program
print("Enter values for Array 1:")
arr1 = createarray()
print("Enter values for Array 2:")
arr2 = createarray()

merged_array = merge_one_after_other(arr1, arr2)
print("Merged array:", merged_array)

'''
Example Run
Enter values for Array 1:
2
1
3
a
Enter values for Array 2:
10
11
12
a
Merged array: [2, 1, 3, 10, 11, 12]

'''