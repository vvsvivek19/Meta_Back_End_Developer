class MyClass:
    a = 5
    print("Hello")

    #class method
    def greetings(self):
        print("Hi There User!!")

#creating a instance or object of class and initialising that instance
myc = MyClass()

#attribute reference with class object
print(MyClass.a)

#attribute reference with instance object 
print(myc.a)

#calling class method with instance object
print(myc.greetings())