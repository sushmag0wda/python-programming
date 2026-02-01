#✅ Python Arrays (Lists)
'''
✅ 1. What is an Array (List)?

An array is a data structure.


A data structure is a way of storing data in an organized manner.

Examples of data structures:

*String
*Array (List)
*Linked List
*Queue
*Stack

✅ Algorithm

An algorithm is a set of steps or logic used to solve a problem or store/process data.

✅ 2. Properties of Arrays (Lists in Python)

*Collection of data (can be homogeneous or heterogeneous)

*Indexed data structure

*Iterable object

*Dynamic size (can grow or shrink based on need)

*Represented using square brackets [ ]

#Syntax'''
arr_name = [data1, data2, data3, ...]
#Examples
arr1 = []            # Empty array
print(arr1)          # []


arr2 = [1, "ab", 2]
print(arr2)          # [1, 'ab', 2]


arr3 = [1, 1, 1]


s2 = (1, 2, 3, 4)    # tuple
s3 = {1, 2, 3, 3}    # set (duplicates removed)
dict1 = {1: 2, 2: 3, 4: 5}  # dictionary

arr4 = [1, "ab", 2, arr3, s2, s3, dict1]
print(arr4) #op = [1, 'ab', 2, [1, 1, 1], (1, 2, 3, 4), {1, 2, 3}, {1: 2, 2: 3, 4: 5}]

'''
✅ 3. len() Function

*len() is an inbuilt function

*Returns the number of elements in an iterable object

*Always returns a whole number

✅ Syntax
len(iterable_object)'''
#Example
arr1 = []
arr2 = [1, "ab", 2]
arr3 = [1, 1, 1]
s2 = (1, 2, 3, 4)
s3 = {1, 2, 3, 3}
dict1 = {1: 2, 2: 3, 4: 5}
arr4 = [1, "ab", 2, arr3, s2, s3, dict1]


print(len(arr1))   # 0
print(len(arr2))   # 3
print(len(arr3))   # 3
print(len(s2))     # 4
print(len(s3))     # 3
print(len(dict1))  # 3
print(len(arr4))   # 7

'''
✅ 4. Index

*Index is a whole number assigned automatically by Python
*Index starts from 0
*Programmers can use an index but cannot change it

Syntax
arr_name[index]

⚠️ Accessing an index that does not exist will cause an IndexError.

✅ 5. append() Method

append() is a predefined method

Adds an element as it is to the end of the array

✅ Syntax
array_name.append(value)
Example'''
arr1 = [1, 2, 3]
arr2 = [100, 200]
arr1.append(arr2)
print(arr1)        # [1, 2, 3, [100, 200]]
print(arr1[3])     # [100, 200]
print(arr1[3][0])  # 100
arr1[3][0] = 999
print(arr2)        # [999, 200]

'''
✅ 6. insert() Method

Used to add an element at a specific index

Syntax
array_name.insert(index, value)
Example'''
arr = [1, 2, 4]
arr.insert(2, 3)
print(arr)   # [1, 2, 3, 4]

'''
✅7. extend() Method

Adds elements of another iterable one by one to the array

Syntax
array_name.extend(iterable)
Example'''
arr1 = [1, 2, 3]
arr2 = [4, 5]
arr1.extend(arr2)
print(arr1)   # [1, 2, 3, 4, 5]

'''
✅8. Difference: append() vs extend()
------------------------------------------------------------
append()	                 |   extend()
Adds as a single element	 |  Adds elements individually
Creates nested list	         |  No nesting
Accepts one value	         |  Accepts iterable
------------------------------------------------------------
✨ These notes are exam‑ready, interview‑friendly, and beginner‑clear.'''