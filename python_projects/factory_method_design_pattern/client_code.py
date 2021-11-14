from concrete_creators import ConcreteCreatorA, ConcreteCreatorB, ConcreteCreatorC


def client_code(creator):
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreatorA.")
    client_code(ConcreteCreatorA())
    print("\n")

    print("App: Launched with the ConcreteCreatorB.")
    client_code(ConcreteCreatorB())
    print("\n")

    print("App: Launched with the ConcreteCreatorC.")
    client_code(ConcreteCreatorC())