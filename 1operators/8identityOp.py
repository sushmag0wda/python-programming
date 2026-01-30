#identity Operators
#is, is not
s1="pentagon"
s2="pentagon"
l1=[1,2,3]
l2=[1,2,3]
print(s1 is s2) #True because both refer to same object in memory
print(l1 is l2) #False because both refer to different object in memory
print(id(s1)) #2704485091440
print(id(s2)) #2704485091440
print(id(l1)) #2704482853056
print(id(l2)) #2704483001664

print(10 is 10) #True because both are same
print(10 is not 20) #True because 10 is not equal to 20
print("hello" is "hello") #True because both are same
print("hello" is not "world") #True because "hello" is not equal to "world"'''
