my_d = {1:'Test',"Name": 'Jim'}
print(my_d[1])
print(my_d["Name"])
my_d[2] = 'Test 2'
print(my_d)
my_d[1] = 'Not a Test'
print(my_d)
for key, value in my_d.items():
    print(str(key) + ":" + value)
del my_d[1]
print(my_d)

