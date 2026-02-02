#Program to Find 2nd Maximum Element (using 2³¹ & index)
def createarray():
    l1 = []
    while True:
        try:
            n = int(input("enter a number: "))
            l1.append(n)
        except:
            return l1


def secondmax(arr):
    max = -2**31
    maxind = -1
    secmax = -2**31
    secmaxind = -1

    for i in range(len(arr)):
        if arr[i] > max:
            secmax = max
            secmaxind = maxind

            max = arr[i]
            maxind = i

        elif arr[i] > secmax and arr[i] != max:
            secmax = arr[i]
            secmaxind = i

    return secmax, secmaxind


# main program
print("Enter values into the array:")
arr = createarray()

res, ind = secondmax(arr)
print("Second max element is", res, "at index", ind)
'''
Example Run
Enter values into the array:
10
45
23
45
9
a
Second max element is 45 at index 3
'''