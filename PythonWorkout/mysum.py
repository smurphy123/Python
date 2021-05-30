def mysum(numbers, base = 0):
    output = 0

    for num in numbers:
        output += num
    
    return output + base

print(mysum([1,2,3], 4))