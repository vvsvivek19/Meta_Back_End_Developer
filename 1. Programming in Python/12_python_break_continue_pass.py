favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisu', 'Chocolate Cake']
item = input("Please enter the item you wanna order: ")
count = 0
while count < len(favorites):
    if (favorites[count] == item):
        print("Item added to order list")
        break
    else:
        count += 1