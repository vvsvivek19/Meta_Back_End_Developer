# Define class MyFirstClass
class MyFirstClass:
    print("Who wrote this?")
    # Define string variable called index
    index = "Author-Book"
    # Define function hand_list()
    def hand_lst(self, philosopher, book, year):
        print(MyFirstClass.index)
        print(self.index)
        # variable + “ wrote the book: ” + variable
        print(str(philosopher) + " wrote the book: " + str(book) + " in the year " + str(year))
        
whodunnit = MyFirstClass()
whodunnit.index = "Sun Tzu"
whodunnit.hand_lst("Sun Tzu","The Art of War","5th Century BC")

# Call function handlist()