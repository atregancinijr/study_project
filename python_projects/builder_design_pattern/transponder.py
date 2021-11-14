
class Transponder:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Transponder features: {', '.join(self.parts)}", end="")
