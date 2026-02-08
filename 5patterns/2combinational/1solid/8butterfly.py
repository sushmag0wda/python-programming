#8)
'''
*     *
**   **
*** ***
*******
*** ***
**   **
*     *
'''
#note : if there is spaces in between the patterns we should take a if-else block in the j loop 
#any changes made on if block should also be done on else block
n=int(input("enter the number : "))
noc=1
nor=(n*2)-1
for i in range(1,n*2):
    for j in range(1,n*2):
        if j<=noc or j>=nor:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i < n:
        noc+=1
        nor-=1
    else:
        noc-=1
        nor+=1
