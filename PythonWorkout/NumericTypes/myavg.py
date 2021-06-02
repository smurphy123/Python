def myavg(numbers):
    sum = 0
    length = len(numbers)

    for num in numbers:
        sum += num
    
    return sum / length

print(myavg([1,2,3,4]))