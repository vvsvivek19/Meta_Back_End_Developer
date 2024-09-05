
#basic for loop
for i in range (10):
    print("Looping .. ", i)

#using for loop to iterate through items of an array
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisu', 'Chocolate Cake']
for item in favorites:
   print("I like", item)

#using while loop to iterate through items of an array
count = 0
while count < len(favorites):
     print("I like", favorites[count])
     count+=1

#using for loop to print indexes of an array along side its items
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisu', 'Chocolate Cake']
for idx, item in enumerate(favorites):
     print(idx, item)
