#Alphabetical patterns
#!)
'''
A
BB
CCC
DDDD
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end="")
    print()'''

#2)
'''
abcd
abc
ab
a
'''
'''n=int(input("enter the value"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(96+j),end="")
    print()'''

#3
'''
D
CC
BBB
AAAA
'''
'''n=int(input("enter the value"))
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(chr(64+i),end="")
    print()'''

#4
'''
ABCD
abcd
ABCD
abcd
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2!=0:
            print(chr(64+j),end="")
        else:
            print(chr(96+j),end="")
    print()'''
#5
'''
A
aB
AbC
aBcD
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print(chr(64+j),end="")
        else:
            print(chr(96+j),end="")  
    print()'''
#6
'''
DcBa
dCbA
DcBa
dCbA
'''

'''n=int(input("enter the value"))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if (i+j)%2==0:
            print(chr(64+j),end="")
        else:
            print(chr(96+j),end="")  
    print()
'''
#7
'''
abcd
abc
ab
a
ab
abc
abcd
'''
'''n=int(input("enter the number : "))
noc=n
for i in range(1,n*2):
    for j in range(1,noc+1):
        print(chr(96+j),end="")
    print()
    if i < n:
        noc-=1
    else:
        noc+=1'''
#8
'''
a b c d 
e f g h
i j k l
m n o p
'''
'''n=int(input("enter the value"))
count=97
for i in range(1,n+1):
    for j in range(1,n+1):
            print(chr(count),end=" ")
            count+=1
    print()'''