menu = { 1: {"name": 'espresso', "price": 1.99},
         2: {"name": 'coffee', "price": 2.50},
         3: {"name": 'cake', "price": 2.79}, 
         4: {"name": 'soup', "price": 4.50},
         5: {"name": 'sandwich', "price": 4.99}
    }

#function to display menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

#function to take order
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    print(order)
    return order

#function to print order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

new_order = take_order()
print_order(new_order)

def calculate_subtotal(order):
    ### WRITE SOLUTION HERE
    sum = 0.00
    prices = []
    prices = [item["price"] for item in order]
    for i in prices:
        sum = sum + i
    return round(float(sum), 2)

total = calculate_subtotal(new_order)
print("Sub Total", total)

def calculate_tax(subtotal):
    print('Calculating tax from subtotal...')
    return round((subtotal * 0.15), 2)
    ### WRITE SOLUTION HERE
tax = calculate_tax(total)
print("Tax for the order is: " + str(tax))

def summarize_order(order):
    prices = []
    prices = [item["price"] for item in order]
    subtotal = 0.00
    for i in prices:
        subtotal = subtotal + i
    tax = round((subtotal * 0.15), 2)
    total = round((tax + subtotal),2)
    names = []
    names = [item["name"] for item in order]
    return names, total
    print_order(order)
    ### WRITE SOLUTION HERE
summarize_order(new_order)



