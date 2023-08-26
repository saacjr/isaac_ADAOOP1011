class Veiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
    
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    def __str__(self):
        return f'Marca: {self.__marca}, Modelo: {self.__modelo}'
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas
    
    def __str__(self):
        return super().__str__() + ', ' + f'Número de Portas: {self.__portas}'

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.__cilindradas = cilindradas
    
    def __str__(self):
        return super().__str__() + ', ' + f'Cilindradas: {self.__cilindradas}'