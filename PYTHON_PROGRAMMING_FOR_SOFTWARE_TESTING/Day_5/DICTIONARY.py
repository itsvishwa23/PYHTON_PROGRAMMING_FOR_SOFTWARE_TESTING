dict = {
    "Biscuit": 101,
    "Grocerry": 102
}
dict2 = {
    "Rice": 1001,
    "Wheat": 1002
}
print(dict["Biscuit"])

for i in dict:
    print(i)
    print(dict[i])

print(dict)

del dict
print(dict)
dict3 = dict | dict2
print(dict3)
