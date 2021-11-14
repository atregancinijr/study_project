class A:
    def a1(self):
        print("a1")

class B:
    def b(self):
        print("b")
        A().a1()
if __name__== '__main__':
    objectB = B()
    objectB.b()