def multiply(arr, num):
    for index in range(len(arr)):
        arr[index] = arr[index] * num
    return arr
a = [2,4,10,16]
x = multiply(a,5)
print x
