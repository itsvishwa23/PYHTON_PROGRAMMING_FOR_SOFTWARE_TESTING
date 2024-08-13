def print_fun():
    print("This is print function wihthout any parameter")


print_fun()


def add_fun(a, b):
    c = int(a)
    d = int(b)
    return c + d


a = input("Enter the number 1")
b = input("Enter the number 2")

print(add_fun(a, b))
print(add_fun(a=10, b=30))
