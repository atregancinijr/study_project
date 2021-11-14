from target import Target
from adaptee import Adaptee
from adapter import Adapter


def client_code(target):
    """
    O código do cliente suporta todas as classes que seguem a interface Target.
    """
    print(target.request(), end="")

print("Cliente: Eu posso trabalhar muito bem com os objetos da classe Target :")
target = Target()
client_code(target)
print("\n")

adaptee = Adaptee()
print("Cliente: A classe Adaptee tem uma interface estranha. Veja, eu não entendo isso :")
print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

print("Cliente: Mas posso trabalhar com isso por meio do Adapter :")
adapter = Adapter()
client_code(adapter)