from bomba_combustivel import BombaCombustivel

class BombaGasolina(BombaCombustivel):
    def __init__(self, valor, quantidade):
        super().__init__(valor, quantidade)

    def abastecer_por_valor_com_aditivo(self, valor):
        litros = valor / super().get_preco() * 1.05

        if litros > super().get_quantidade():
            return -1
        else:
            sobra = super().get_quantidade() - litros
            super().set_quantidade(sobra)
            return litros
    
    def abastecer_por_litros_com_adtivo(self, litros):
        valor = litros * (super().get_preco() * 1.05)

        if litros > super().get_quantidade():
            return -1
        else:
            sobra = super().get_quantidade() - litros
            super().set_quantidade(sobra)
            return valor

class Bomba_gasolina_C(BombaCombustivel):
    def __init__(self, valor, quantidade):
        super().__init__(valor, quantidade)