str = input()
lenght = len(str)
last_index = lenght - 1
rev_str = ''
def reverse_string (last_index):
    if last_index < 0:
        return
    else:
        rev_str.append(str[last_index])
        last_index -= 1
        reverse_string(last_index)
reverse_string(lenght)
print(rev_str)