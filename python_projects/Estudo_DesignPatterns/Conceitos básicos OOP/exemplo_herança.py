class A:
    def function_a(self):
        return 'teste_A'

class B(A):
    def function_b(self):
        return 'teste_B'

if __name__ == '__main__':
    b = B()
    res =  b.function_a()
    print(res)