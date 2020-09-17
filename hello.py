print("hello world")

msg = "Numbers: {0}, {1}".format(20, 21)
msgVar = "Numbers: {a}, {b}".format(a=20, b=21)
print(msg)
print(msgVar)

print(5**2, 20 // 6)
var = input("hei namamu? \n")
if var.isalpha():
    print(var + " adalah string")
    print("ini namamu " + var)
elif var.isnumeric():
    print(var + " adalah bilangan")
elif var.isdigit() or var.isalnum():
    print(var + " adalah string dengan bilangan")
else:
    print("err")
