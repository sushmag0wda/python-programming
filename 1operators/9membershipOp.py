#membership Operators
#in, not in     
s1="Aabbc12"
print('A' in s1) #True because 'A' is present in the string
print('abb' not in s1) #True because 'a' is not present in the string
print("123"not in s1) #false because '123' is not present in the string
print(1 in [11,22,33]) #False because 1 is not present in the list
print(3 in 33) #False because 3 is not present in the integer
print("3" in "33") #True because '3' is present in the string "33"-
print(10 in [10,20,30]) #True because 10 is present in the list
print(10 not in [20,30,40]) #True because 10 is not present in the list
