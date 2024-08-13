class test:

    def sum(self, a, b):
        result = a + b
        print(result)


class demo(test):
    def __init__(self, a):
        print(a)

        def sum(self, a, b, c):
            result = a + b + c
            print(result)


d = demo()
d.sum(10, 20, 30)
t = test()
t.sum(10, 20)
