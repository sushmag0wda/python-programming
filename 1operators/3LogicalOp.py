# Logical Operators
#and 
print((23>(10**1))and True and 55) #True because all conditions are True
print((True**False)and -10 and ((5+5<=(2**2)))) #False because True**False is 0 and 0 is False
#or
print((5 and 0)or (25>12)or (True**5)) #True because 25>12 is True
print(0 or (10%2) or (True**5)) #True because 10%2 is 0 and True**5 is True
#not
print(not((5 and 0)or (25>12)or (True**5))) #False because the expression inside the not is True
print(not(not((35<=45)and (26>12)and (not(True))))) #True because the expression inside the not is False
