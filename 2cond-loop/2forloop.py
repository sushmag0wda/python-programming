#looping statements:
'''
1)for loop
    a)with range()
        syn:
        for variable in range(start,stop,step):
           #logic
        #remaining statements
-----------------------------------------------------------------------------
        range()
        syntax:range(start,stop,step)
        -predefined function
        -it helps to setup a range of values internally
        -only integer arguments are allowed
-----------------------------------------------------------------------------
        i)start:starting value
        -from where pvm should begin the range of values
        -if not provided, it will start from 0
-----------------------------------------------------------------------------
        ii)stop:stopping value
        -it is the value where pvm should stop the range of values
        -compulsory argument
        -it is exclusive, means it will not include the stop value
-------------------------------------------------------------------------------
       iii)step:increment value
        -it is the value by which pvm should increment the range of values
        -if not provided, it will increment by 1
        -if step is negative, then start should be greater than stop
        -if step is positive, then start should be less than stop
---------------------------------------------------------------------------'''
for i in range(1,5):
    print(i,end=" ") #prints 1,2,3,4
print("----------------------------------------------------------------------------------------------")
for i in range(0,10,2):
    print(i,end=" ") #prints 0,2,4,6,8
print("----------------------------------------------------------------------------------------------")
for i in range(10,0,-2):
    print(i,end=" ") #prints 10,8,6,4,2
print("----------------------------------------------------------------------------------------------")
for i in range(5): #start is not provided, so it will start from 0
    print(i,end=" ") #prints 0,1,2,3,4
print("----------------------------------------------------------------------------------------------")
for i in range(1,10,-2): #invalid range
    print(i,end=" ") #no output
print("----------------------------------------------------------------------------------------------")

#for i in range() #error

#pvm will not accept the range without any arguments
'''pvm cannot return multiple sequencesof values at 
the same time until and unless it is not stored in a 
data structure therefore for is used with range()'''
# types of for loop
''' 
i)incrementing
        for variable in range(start,actual stop +1,+ve step):
            #logic
        #remaining statements
three rules of incrementing for loop
1)step should be +ve
2)start should be less than stop
3)stop should be inclusive of the value +1

decrementing
         for variable in range(start,actual stop -1,-ve step):
            #logic
        #remaining statements
        #note:the inputs given for a program is caled constraints
three rules of decrementing for loop
1)step should be -ve
2)start should be greater than stop
3)stop should be exclusive of the value -1
'''
'''
b)without range
    -it can be used with any iterable data structure or on group of elements
    -there is no increment or decrement
    -it moves only in forward direction
    -here, the looping variable will directly holds each individual element
        syntax:
            for variable in iterable obj or group of elements:
                #logic
            #remaining statements'''

    
#example:
for i in 10,20,30:#group of elements
    #it will print each element in the group
    print(i, end=" ") #op 10 20 30
print("\n==================================")

for j in 20,10,-30:#group of elements
    print(j, end=" ") #op 20 10 -30
print("\n==================================")

for k in "abc",100,23,-100:#group of elements
    #it will print each element in the group
    print(k, end=" ") #op a b c 100 23 -100
print("\n==================================")

for x in "abc":#string is iterable
    print(x, end=" ") # op a b c
print("\n==================================") 

for y in [1,2,3]:#list is iterable
    #it will print each element in the list
    print(y, end=" ") #op 1 2 3
print("\n==================================")

for z in "":#empty string is iterable but has no elements
    #it will not print anything
    #it will not throw error
    print(z, end=", ") #no output
print("\n==================================")

#for a in 100:#error, int is not iterable
 #   print(a, end=" ") #no output
#print("\n==================================")

for b in "100":# 100 is a string, string is iterable
    print(b, end=" ") #op 1 0 0
print("\n==================================")

for c in (1,2,3):#tuple is iterable
    #it will print each element in the tuple
    print(c, end=" ")
print("\n==================================")

#difference in for loop with range and without range

'''without range
-moves only in forward direction
-looping variable will directly holds each individual element
-to access the index we have to use inbuilt functions to get the index
-inputs should be iterable'''

l1=[3,5,-9]
for i in l1:
    print(i) #op 3 5 -9
print("\n==================================")
#-------------------------------------------------------------------------------------------'''
'''with range
-supports incrementing and decrementing
-looping variable will hold the index of the element not the element
-inputs are only integers'''
l1=[3,5,-9]
for i in range(0, len(l1)):
    print(i,"=", l1[i]) #op 0=3 1=5 2=-9
print("\n==================================")

#-------------------------------------------------------------------------------------------
#example to print element with index using for loop with and without range
l1=[1,2,3,4,5]
for i in l1:#for loop without range
    print("element:", i, "index:", l1.index(i))
print("\n==================================")

for i in range(0, len(l1)): #for loop with range
    print("element:", l1[i],"index:", i)
print("\n==================================")
#---------------------------------------------------------------------------