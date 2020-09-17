def decor(func):
    def wrap():
        print("==============")
        func()
        print("==============")
    return wrap


@decor
def printText():
    print("Hello wordl")


printText()
