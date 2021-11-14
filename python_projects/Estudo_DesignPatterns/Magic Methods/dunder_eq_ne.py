# All instances of MyClass are equivalent to one another, and they
# are not equivalent to instances of other classes.
class MyClass:
    def __eq__(self, other):  #"=="
        if type(self) == type(other):
            return f'The objects are iqual'
        else:
            return f'The objects aren`t iqual'

    def __ne__(self, other):  #"!="
        if type(self) != type(other):
            return f'The objects are different'
        else:
            return f'The objects aren`t different'

if __name__ == '__main__':
    my_obj= MyClass()
    my_obj2= MyClass()
    print(MyClass() == MyClass())
    print(MyClass() == 42)
    print(MyClass() == my_obj)
    print('\n')
    print(my_obj2 != MyClass())
    print(MyClass() != 42)
    print(my_obj != my_obj2)


#__eq__ method runs when Python is asked to make an equivalence check with the == operator, "other" will be set to the
# object on the other side of ==.
