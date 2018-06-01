def multiply(arr,num):
    print arr, num
    for x in arr:
        print x
        x *= num
    return arr
a = [2,3,10,16]
b = multiply(a,5)
print b
