#Dictionary (dict) in Python

'''What is a Dictionary?

A dictionary is a data structure

It stores data in key : value pairs

It is an iterable object

A dictionary is mutable in nature

Syntax
dict_name = {key1: value1, key2: value2}


Example:'''

d = {1: "apple", 2: "banana"}

'''Keys in Dictionary

Keys act as identifiers

Keys are immutable

Keys must be unique

Keys can be of any immutable type

int, float, str, tuple

Mutable data structures cannot be keys

❌ list, set, dict

Duplicate keys are not allowed

If duplicated, latest value is taken

To get the count of keys, use:

len(dict_name)


Example:'''

d = {1: "a", 1: "b"}
print(d)   # {1: 'b'}

'''Values in Dictionary

Values store the actual data

Values are mutable

Values can be heterogeneous

Values can be duplicated

To get the count of values, use:

len(dict_name)


Example:'''

d = {1: "a", 2: "a", 3: [1,2,3]}

'''Dictionary Length

len(dict_name) gives the number of key–value pairs

Example:'''

d = {1: 10, 2: 20, 3: 30}
print(len(d))  # 3

'''Dictionary Representation

{} is used to represent a dictionary

Empty dictionary:'''

d = {}

'''When Do We Use Dictionary?

When we want to store data in key–value format

When we want to track frequency of elements

When fast search, update, insert is required

Example (frequency count):'''

arr = [1,2,1,3,2,1]
freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

'''Traversing a Dictionary

Use for loop with items()

Syntax
for key, value in dict_name.items():
    print(key, value)


Example:'''

d = {1: "a", 2: "b"}
for k, v in d.items():
    print(k, v)

'''Accessing a Value

Use the key

Syntax
dict_name[key]


Example:
'''
d = {1: "apple", 2: "banana"}
print(d[1])  # apple

'''Updating a Value

Assign a new value to an existing key

Syntax
dict_name[key] = new_value'''


#Example:

d = {1: "apple"}
d[1] = "orange"

'''Adding a New Key–Value Pair

Assign value to a new key

Syntax
dict_name[new_key] = new_value


Example:'''

d = {}
d[1] = "python"

'''One-Line Summary (Exam Ready 📝)

Dictionary is a mutable data structure that stores data in key–value pairs where keys are immutable and unique, and values can be duplicated and heterogeneous.
'''