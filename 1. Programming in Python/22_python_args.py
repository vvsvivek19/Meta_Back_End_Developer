def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
print(sum_of(3,4,6,7,8,9,10))