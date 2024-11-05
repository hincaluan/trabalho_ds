from bomba_combustivel import BombaCombustivel

class BombaEtanol(BombaCombustivel):
    def __init__(self, quantidade, valor):
        super().__init__(quantidade, valor)


# testing
bomba = BombaEtanol(1000, 4)
resultado = bomba.abastecer_por_litros(20)
print(resultado)  # Deve imprimir 80
print(bomba.get_quantidade())  # Deve imprimir 980

bomba = BombaEtanol(1000, 4)
resultado = bomba.abastecer_por_valor(100)
print(resultado)  # Deve imprimir 25
print(bomba.get_quantidade())  # Deve imprimir 975