#__del__ method is invoked when an object is being destroyed.
#Lets see this behavior at work by making the following class that deletes noisily
class Xon:
    def __del__(self):
        print('AUUUUUUGGGGGGHH!')

class Xon2:
    def __init__(self):
        print('I Have born here!')

    def __del__(self):
        print('UUUUUUOOOGGGGGGHH! Dead...')

if __name__ == '__main__':
    y = Xon2()
#What happened here? First, an Xon object was created (but not assigned to a
#variable, so there is no real reason for the Python interpreter to keep it around).

