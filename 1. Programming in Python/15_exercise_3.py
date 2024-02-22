num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

# for item in num_list:
#     if item > 45:
#         print("Over 45:", item)
#     else:
#         print("Under 45:", item)


# for idx, item in enumerate(num_list):
#     if item == 36:
#         print("Number found at position:", idx)

count = 0
for idx, item in enumerate(num_list):
    count += 1
    if item == 36:
        print("Number found at position:", idx+1)
        break
print("Count:", count)

a = isinstance("aa", str)

print(a)  