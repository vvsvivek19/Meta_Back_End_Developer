#List with all integer items
list1 = [1,2,3,4,5]
print(list1[2])

#list with all character type item
list2 = ['A', 'B', 'C']

#list with various other datatypes together
list3 = ['Hello', 1,True, 40.22]

#nested lists
list4 = [1, [2,3,4], 5, 6]

print(*list1)
#list1.insert(len(list1),6)
#list1.append(6)
#list1.extend([7,8,9,10])
#list1.pop(4)
#del list1[2]
print(list1, sep=",")

for x in list1:
    print(x)