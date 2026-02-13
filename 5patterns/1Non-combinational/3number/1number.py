#number patterns 
# at every updated row if the complete row displays the same value then it is printing the value present in the variable i
#at every updated row if it starts from the same point and moves till certain point or viseversa then it is printing the value present in the value present in the variable j
#if the pattern is of continueous series then it is a third variable 
#1)
'''
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''
'''n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()'''

#2)
'''
1 
1 2
1 2 3
1 2 3 4
'''
'''n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
#3)
'''
1 2 3 4 
1 2 3
1 2
1
'''
'''n=int(input("enter a number"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

#4)

'''
4 
4 3
4 3 2
4 3 2 1
'''
'''n=int(input("enter a number"))
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print()'''

#5)
'''
1 
2 1
3 2 1
4 3 2 1
'''
'''n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(i,1-1,-1):
        print(j,end=" ")
    print()'''

#6)
'''
4 3 2 1 
3 2 1
2 1
1
'''
'''n=int(input("enter a number"))
for i in range(n,0,-1):
    for j in range(i,1-1,-1):
        print(j,end=" ")
    print()'''

#7)
'''
1 2 3 4 
1     4
1     4
1 2 3 4
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()'''
#8)
'''
1 
0 1
1 0 1
0 1 0 1
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()'''
#9)
'''
1 0 0 0 
0 2 0 0
0 0 3 0
0 0 0 4
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print(i,end=" ")
        else:
            print("0",end=" ")
    print()'''
#10)
'''
1 0 0 1 
0 2 2 0
0 3 3 0
4 0 0 4
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or (i+j)==(n+1):
            print(i,end=" ")
        else:
            print("0",end=" ")
    print()'''

#11)
'''
1 0 0 4 
0 2 3 0
0 2 3 0
1 0 0 4
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or (i+j)==(n+1):
            print(j,end=" ")
        else:
            print("0",end=" ")
    print()'''


#12)
'''
1 1 1 1 
1 2 2 2 
1 2 3 3 
1 2 3 4
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()'''
#13)
'''
4 3 2 1 
3 3 2 1
2 2 2 1
1 1 1 1
'''
'''n=int(input("enter the value"))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if i>j:
            print(j,end=" ")
        else:
            print(i,end=" ")
    print()'''
#14)
'''
1 2 3 4 
2 2 3 4
3 3 3 4
4 4 4 4
'''
'''n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<=j:
            print(j,end=" ")
        else:
            print(i,end=" ")
    print()'''

#15)
'''
4 4 4 4 
4 3 3 3
4 3 2 2
4 3 2 1
'''
'''n=int(input("enter the value"))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if i>j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()'''
#16)
'''
1 2 3 4 
5 6 7 8
9 10 11 12
13 14 15 16
'''
'''n=int(input("enter the value"))
count=1
for i in range(1,n+1):
    for j in range(1,n+1):
            print(count,end=" ")
            count+=1
    print()'''

#17
'''
1 2 3 4 
8 7 6 5
9 10 11 12
16 15 14 13
'''
'''n=int(input("enter the value"))
count1=1
count2=0
for i in range(1,n+1):
    for j in range(1,n+1):
            if i%2!=0:
                  print(count1,end=" ")
                  count2=count1
            else:
                  print(count2,end=" ")
                  count2-=1  
            count1+=1            
    print()
    count2=count2+n'''

#18
'''
1
3 2
4 5 6
10 9 8 7

'''
'''n=int(input("enter the value"))
count1=1
count2=0
for i in range(1,n+1):
    for j in range(1,i+1):
            if i%2!=0:
                  print(count1,end=" ")
                  count2=count1
            else:
                  print(count2,end=" ")
                  count2-=1  
            count1+=1            
    print()
    count2=(count2+i)+1'''