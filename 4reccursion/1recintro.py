#WAP to print 1-4(n) without using any loops or no repetative code allowed within the same block
#op=1 2 3 4 5
def num(n):
    print(n,end=" ")

num(1)
num(2)
num(3)
num(4)

#the recursive-style version

def num1(n):   # 1 is given
    print(n,end=" ")
    num2(n+1)

def num2(n):   # 2 is given
    print(n,end=" ")
    num3(n+1)

def num3(n):   # 3 is given
    print(n,end=" ")
    num4(n+1)

def num4(n):   # 4 is given
    print(n,end=" ")

num1(1)
'''
📌 Output Produced
1 2 3 4  '''

''''
Complete Call Flow Diagram
num1(1)
   ↓
num2(2)
   ↓
num3(3)
   ↓
num4(4)
'''
#when function is called in the stack memory there will be a activation record is created
#once the function is executed the activation record will be removed from the stack memory
#this memory deallocation is done by the pvm 
#the pvm will deallocate the memory when it comes to the return statement
#in every function there will be a return statement by default
#the default return is given by the compile
