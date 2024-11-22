from bomba_combustivel import BombaCombustivel

class BombaEtanol(BombaCombustivel):
    def __init__(self, quantidade, valor):
        super().__init__(quantidade, valor)
