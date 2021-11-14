'''O "Target" define a interface específica do
domínio usada pelo código do cliente. '''

class Target:
    def request(self):
        return "Target: Este é o comportamento padrão esperado."