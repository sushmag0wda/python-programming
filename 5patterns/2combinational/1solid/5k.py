#5)
'''
****
***
**
*
**
***
****
'''
n=int(input("enter the number : "))
noc=n
for i in range(1,n*2):
    for j in range(1,noc+1):
        print("*",end="")
    print()
    if i < n:
        noc-=1
    else:
        noc+=1