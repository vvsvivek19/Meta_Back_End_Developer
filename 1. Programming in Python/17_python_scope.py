#global scope
my_global = 10

def fn1():
    #enclosed scope
    ennclosed_v = 8
    def fn2():
        #local scope
        local_v = 5
        print("Access to Global", my_global)
        print("Access to Enclosed", ennclosed_v)
    fn2()

fn1()
