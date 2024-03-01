class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
    def content(self):
        print("The " + self.dish + " has " + str(self.items) + \
              " and takes " + str(self.time) + " min to preprare.")
        
pizza = Recipe("Pizza", ["Cheese","Bread","Tomato"], 45)
pasta = Recipe("Pasta", ["penne","Sauce"], 55)

print(pizza.items)
print(pasta.items)
pizza.content()