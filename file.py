file = open("test.txt", "r")
print(file.read())
print(file.read())
file.close()

fileWrite = open("test.txt", "w")
fileWrite.write("line baru")
fileWrite.close()

with open("test.txt", "r") as f:
    print(f.read())
