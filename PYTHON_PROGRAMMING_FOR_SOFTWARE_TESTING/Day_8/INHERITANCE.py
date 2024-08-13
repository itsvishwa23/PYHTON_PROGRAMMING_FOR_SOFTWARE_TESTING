class parent:

    def parent_disp(self):
        print("Parent Class Method")


class parent_two:

    def parent_disp_two(self):
        print("Parent 2 Class Method")


class child(parent, parent_two):

    def child_disp(self):
        print("Child Class Method")
        super().parent_disp()


class sister(child):

    def sister_disp(self):
        print("In sister class")
        super().child_disp()


p = parent()
p.parent_disp()
c = child()
c.parent_disp()
c.child_disp()
c.parent_disp_two()
s = sister()
s.parent_disp()
