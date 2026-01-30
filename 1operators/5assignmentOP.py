#assignment Operators
#=
#variables- memory where we store the address 
a=10
b=(2*5)
c=(8+2)
d=b
print(a)#!0
print(b)#10
print(c)#10
print(d)#10
print(id(a))#140716814386376
print(id(b))#140716814386376
print(id(c))#140716814386376
print(id(d))#140716814386376
d=(15+5)
print(d)#20
print(id(d))#140716993365512
print(a==d)#false
d=25
print(d)#25
print(id(d))#140716993365672
d=45
print(d)#45
print(id(d))#140716993366312
e=100
print(e)#100
e=200
print(e)#200
e=300
print(e)#300
print(type(e))#<class 'int'>
g=55,65,75
print(g)#(55, 65, 75)
print(type(g))#<class 'tuple'>
k=2500
print(k)
#print(z)#error
#a=b+y#error
print(a) #10
