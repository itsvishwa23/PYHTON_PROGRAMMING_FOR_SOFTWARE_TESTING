try:
    a = 10
    # b = 20
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot Divide by Zero")
except SystemError:
    print("Cannot Divide by Zero")
else:
    print("In else block")
finally:
    print("In finally")

a = 10
b = 0


def div(): raise ZeroDivisionError


print(a / b)

