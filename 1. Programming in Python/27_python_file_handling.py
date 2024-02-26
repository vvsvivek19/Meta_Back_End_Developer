file = open("D:/Web Development/Practice Code/Meta_Back_End_Developer/1. Programming in Python/test.txt", mode = 'r')
data = file.readline()
print(data)
file.close()

with open("D:/Web Development/Practice Code/Meta_Back_End_Developer/1. Programming in Python/test.txt", mode='r') as file:
    data = file.readline()
print(data)