class BombaCombustivel:
    def __init__(self, valor, quantidade):  
        self.__valor_litro = valor
        self.__quantidade = quantidade

    def get_preco(self):
        return self.__valor_litro
    
    def set_quantidade(self, novo_valor):
        self.__quantidade = novo_valor

    def get_quantidade(self):
        return self.__quantidade
    
    def set_valor(self, valor):
        self.__valor_litro = valor
    
    def abastecer_por_litros(self, litros):
        if litros > self.__quantidade:
            return -1
        else:
            total = litros * self.__valor_litro
            self.__quantidade -= litros
            return total
    
    def abastecer_por_valor(self, valor):
        litros = valor / self.__valor_litro
        if litros > self.__quantidade:
            return -1
        else:
            self.__quantidade -= litros
            return litros
