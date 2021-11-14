from target import Target
from adaptee import Adaptee

class Adapter(Target, Adaptee):
    """
    O Adapter torna a interface de Adaptee compatível
    com a interface do Target por meio de herança múltipla
    """

    def request(self) -> str:
        return f"Adapter: (TRADUÇÃO) {self.specific_request()[::-1]}"
