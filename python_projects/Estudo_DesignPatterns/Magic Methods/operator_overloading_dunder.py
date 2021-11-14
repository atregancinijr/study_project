''' |  Operator |     Method        |     Reverse       |     In-place        |
    |     +     |     __add__       |     __radd__      |     __iadd__        |
    |     -     |      __sub__      |     __rsub__      |     __isub__        |
    |     *     |     __mul__       |     __rmul__      |     __imul__        |
    |     /     |     __truediv__   |     __rtruediv__  |     __itruediv__    |
    |     //    |     __floordiv__  |     __rfloordiv__ |     __ifloordiv__   |
    |     %     |     __mod__       |     __rmod__      |     __imod__        |
    |     **    |     __pow__       |      __rpow__     |     __ipow__        |
    |     &     |     __and__       |     __rand__      |     __iand__        |
    |     |     |     __or__        |     __ror__       |     __ior__         |
    |     ˆ     |      __xor__      |     __rxor__      |     __ixor__        |
    |     <<    |     __lshift__    |     __rlshift__   |     __ilshift__     |
    |     >>    |     __rshift__    |     __rrshift__   |     __irshift__     |'''

#The first of these is a vanilla method, in which an expression x + y maps to x.__add__(y), and the method simply returns the result.
#The second is a reverse method.  The reverse methods are called if the first operand does not supply the traditional method. Therefore, the expression x + y, where x does not define an __add__ method, would call y.__radd__(x).
#The third and final magic method is the in-place method.In-place methods are called when the operators that modify the former variable in place (such as +=, -=) are used. The expression x += y would call x.__iadd__(y).
class Book:
    def __init__(self, title='', pages=0):
        self.title = title
        self.pages = pages

    def __str__(self):
        return self.title

    def __radd__(self, other):      #https://blog.teamtreehouse.com/operator-overloading-python
        return self.pages + other

    def __add__(self, other): #most of the time, __add__ and __radd__ are very similar, often just inverses of each other!
        return self.pages + other.pages

#https://www.geeksforgeeks.org/customize-your-python-class-with-magic-or-dunder-methods/

class Count:
    def __init__(self, count):
        self._count = count

    def __add__(self, other):
        total_count = self._count + other._count
        return Count(total_count)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __str__(self):
        return 'Count:% i' % self._count

class inPlace(object):
    def __init__(self, value):
        self._value = value
    def __iadd__(self, other):
        self._value = self._value + other._value
        return self._value
    def __str__(self):
        return str(self._value)

if __name__=='__main__':
    book1 = Book('Fluency', 350)
    book2 = Book('The Martian', 300)
    book3 = Book('Ready Player One', 300)
    print(sum([book1, book2, book3]))   #__radd__
    print(book1 + book2)  #__add__

    c1 = Count(2) #Vanila
    c2 = Count(5)
    c3 = c1 + c2
    print(c3)

    c2 = Count(2)
    c3 = 0 + c2 #Reverse
    print(c3)

    inP1 = inPlace(5)
    inP2 = inPlace(3)
    inP1 += inP2
    print(inP1)