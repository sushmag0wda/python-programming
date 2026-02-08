def square(n):
    print("square")
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("*",end="")
        print()
def lhs(n):
    print("left hand side triangle")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
def lhsinv(n):
    print("left hand side triangle inverted")
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()
def rhs(n):
    print("right hand side triangle")
    for i in range(1,n+1):
        for k in range(n,i,-1):
            print(" ",end="")
        for j in range(1,i+1):
            print("*",end="")
        print()
def rhsinv(n):
    print("right hand side triangle inverted")
    for i in range(n,0,-1):
        for k in range(n,i,-1):
            print(" ",end="")
        for j in range(1,i+1):
            print("*",end="")
        print()
def py(n):
    print("pyramid")
    for i in range(1,n+1):
        for k in range(n,i,-1):
            print(" ",end="")
        for j in range(1,i+1):
            print("*",end=" ")
        print()
def pyinv(n):
    print("pyramid inverted")
    for i in range(n,0,-1):
        for k in range(n,i,-1):
            print(" ",end="")
        for j in range(1,i+1):
            print("*",end=" ")
        print()
def oddpy(n):
    odd=1
    print("odd pyramid")
    for i in range(1,n+1):
        for k in range(n,i,-1):
            print(" ",end="")
        for j in range(1,odd+1):
            print("*",end="")
        odd+=2
        print()
def oddpyinv(n):
    odd=(n*2)-1
    print("odd pyramid inverted")
    for i in range(n,0,-1):
        for k in range(n,i,-1):
            print(" ",end="")
        for j in range(1,odd+1):
            print("*",end="")
        odd-=2
        print()
def para(n):
    print("parallelogram")
    for i in range(1,n+1):
        for k in range(1,i):
            print(" ",end="")
        for j in range(1,n+1):
            print("*",end="")
        print()
def parainv(n):
    print("parallelogram inverted")
    for i in range(n,0,-1):
        for k in range(1,i):
            print(" ",end="")
        for j in range(n,0,-1):
            print("*",end="")
        print()

n=int(input("enter the number"))
square(n)
print("-----------------------------------------------------------------------------------------")
lhs(n)
print("-----------------------------------------------------------------------------------------")
lhsinv(n)
print("-----------------------------------------------------------------------------------------")
rhs(n)
print("-----------------------------------------------------------------------------------------")
rhsinv(n)
print("-----------------------------------------------------------------------------------------")
py(n)
print("-----------------------------------------------------------------------------------------")
pyinv(n)
print("-----------------------------------------------------------------------------------------")
oddpy(n)
print("-----------------------------------------------------------------------------------------")
oddpyinv(n)
print("-----------------------------------------------------------------------------------------")
para(n)
print("-----------------------------------------------------------------------------------------")
parainv(n)
print("-----------------------------------------------------------------------------------------")