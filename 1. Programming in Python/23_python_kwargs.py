def sum_of(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return sum

print(round(sum_of( coffee=2.99, cake=4.55, juice=2.99),2))

