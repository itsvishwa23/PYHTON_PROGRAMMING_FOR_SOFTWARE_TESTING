t = 5  # global varible


class Employee:
    def emp_disp(self, name, age, salary):
        print("The details of employee are")
        print(name, age, salary)


class Salary:
    def disp(self):
        print("This is salary class")


class demo:
    @staticmethod
    def demo_print():
        print("This is demo")


class vishwa:
    name = "Vishwa"  # class varible

    def vishwa_print(self):
        x = 10
        t = 15555  # local varible
        print(x)
        print(t)
        print(globals()['t'])
        print(self.name)


# Create instances of the classes
e1 = Employee()
e1.emp_disp("Vishwanath", 30, 50000)

s1 = Salary()
s1.disp()

demo().demo_print()
v1 = vishwa()
v1.vishwa_print()


class cst:
    def __init__(self):
        print("Constructor Invoked")


c1 = cst()


class tst:
    def __init__(self, a, b):
        print(a)
        print(b)


t1 = tst(10, 20)
