class MyObject:
    def __str__(self):
        return 'My Awesome Object!'

if __name__ == '__main__':
    print(MyObject)

    print(MyObject())

    myobj= str(MyObject())
    print(myobj)

    myobj2= MyObject()
    print(myobj2)