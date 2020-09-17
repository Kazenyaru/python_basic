numsTuple = (20, 21, 22)
numsDict = {
    "number": [20, 21, 22]
}
numsList = [20, 21, 22]

print(len(numsList))
print(22 in numsList)

print(numsList + [23, 24, 25])
print(numsList * 2)

print(numsList[::-1])

ints = numsList
print(ints)

print(list(range(5)))
print(list(range(3, 5)))

if all([i > 20 for i in numsList]):
    print("all value larger than 20")

if any([i > 22 for i in numsList]):
    print("at least one value larger than 22")

listFromNumsTimesFive = list(map(lambda x: x * 5, numsList))
print(listFromNumsTimesFive)

listFromNumsFiltered = list(filter(lambda x: x % 2 == 0, numsList))
print(listFromNumsFiltered)
