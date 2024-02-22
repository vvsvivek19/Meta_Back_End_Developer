import time
start_time = time.time()

#printing table from 1 to 10
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,2,3,4,5,6,7,8,9,10]
count = 0

for x in list1:
    print("Table of ", x)
    for y in list2:
        print (x ,"*",y,"=",x*y)

print("Total time taken:",round((time.time() - start_time),2))

