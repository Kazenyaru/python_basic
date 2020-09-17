def countdown():
    i = 5
    while (i < 5):
        yield i
        i -= 1


for i in countdown():
    print(i)
