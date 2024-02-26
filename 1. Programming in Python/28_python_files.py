#always use exception handling when working with files to handle exception like file not found.
try:
    with open('newfile.txt', 'a') as file:
        file.writelines(["\nThis is a new file created!","\nThis is another line to be added."])
except FileNotFoundError as e:
    print("Error", e)