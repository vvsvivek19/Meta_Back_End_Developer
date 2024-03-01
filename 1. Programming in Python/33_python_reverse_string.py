user_string = input()
lenght = len(user_string)
last_index = lenght - 1
rev_str = ''
def reverse_string (last_index):
    global rev_str
    if last_index < 0:
        return
    else:
        rev_str = rev_str + user_string[last_index]
        last_index -= 1
        reverse_string(last_index)

reverse_string(last_index)
print(rev_str)