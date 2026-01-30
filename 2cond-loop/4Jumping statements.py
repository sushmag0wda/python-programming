#jumping statements
'''1)break
    -it is used to exit the current loop
    -it will not execute the remaining iterations of the loop
    -it can be used with for and while loops
2)continue
    -it is used to skip the current iteration of the loop
    -it will not execute the remaining logic of the current iteration
    -it can be used with for and while loops
    -it will continue with the next iteration of the loop
    -it is used to skip the current iteration and continue with the next    
3)return
    -it is used to exit the current function and return a value
    -it can be used with functions only
    -it will not execute the remaining logic of the function
    -it will return the value to the caller of the function
'''
#write a logic keep accepting numbers from the user until and unless 
#he is not entering the number 0. once he enters 0,exit the repeatetive 
#logic also ignore even num
'''i/p:
enter val:1
number entered is 1
enter val:100
number entered is 100
enter val:-3
number entered is -3 
enter val:0
program exited!!!'''

while True:
    n=int(input("enter val: "))
    if n == 0:
        print("program exited!!!")
        break # break is used to exit the current loop
    elif n % 2 == 0:
        continue # continue is used to skip the current iteration and continue with the next
    else:
        print("number entered is", n)
#-----------------------------------------------------------------------------------------------------------------