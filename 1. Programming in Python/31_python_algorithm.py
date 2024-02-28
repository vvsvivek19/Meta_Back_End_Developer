#Algorith for palindrome
str = input("Enter the word for checking Palindrom: ")
# def isPalindrome(str):
#     startIndex = 0
#     lastIndex = len(str) - 1

#     for x in str:
#         if str[startIndex] != str[lastIndex]:
#             return False
#     return True

def isPalindrome(str):
    length = len(str)
    last_index = length - 1
    count = 0
    revstr =''
    while count < length:
        revstr = revstr + str[last_index]
        count += 1
        last_index -= 1
    return revstr

revstr = isPalindrome(str)

if (str == revstr):
    print("String is a palindrome")
else:
    print("String is not a palindrome")


