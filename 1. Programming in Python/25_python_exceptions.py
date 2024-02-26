def divide_by(a,b):
    return a / b

# try:
#     ans = divide_by(40,0)
# except Exception as e:
#     print("Something went wrong!", e)
#     print(e.__class__)
try:
    ans = divide_by(40,0)
except ZeroDivisionError as e:
   print(e, "We cannot divide by zero")
#It is possible to handle more than one exception without knowing what they are ahead oftime by chaining except statements together. 
except Exception as e:
    print("Something went wrong!",e)

