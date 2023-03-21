# There is a program (see listing below). It is necessary to add a command in the func2 function body that would
# change the value of the already existing msg variable declared in the func1 function.


def func1():
    msg = input("message: ")

    def func2():
        nonlocal msg
        msg = input("message: ")
        print(msg)

    func2()
    print(msg)


func1()
