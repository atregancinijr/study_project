class Adder:
    def __init__(self):
        self.sum = 0

    def add(self, value):
        self.sum += value

if __name__ == '__main__':
    acc = Adder()
    for i in range(99):
        acc.add(i)
        print(acc.sum)