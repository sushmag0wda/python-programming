#digsum
#WAP to sum of all the individual character digits present in a given string

'''I/P:a12d34c4

o/p: (1+2+3+4+4)
    =14'''

#i/p : "a12d34c4"
#OP:adc(12+34+4)=adc50
def digsum(str):
    sum=0# to collect the sum of the digits present in the string
    res=""#to collect left over character
    for i in range(0,len(str)):
        if "0"<=str[i]<="9":
            sum=sum+(ord(str[i])-48)  #to convert char '1' to int 1
        else:
            res=res+str[i]   #to add the leftover characters from the string from a2b4cs to abcs

    nstr=''
    while sum>0:
        rem=sum%10
        nstr=chr(rem+48)+nstr  
        sum=sum//10
        #this logic can be replaced with newstr=string(sum)

    return res+nstr

str=input("enter a string : ")
res=digsum(str)
print(res)