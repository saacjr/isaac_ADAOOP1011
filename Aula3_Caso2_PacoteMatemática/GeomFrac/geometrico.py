class Retangulo:
    def __init__(self, altura, largura):
        if (altura < 0) or (largura <0):
            raise ValueError("Retângulos não podem ter dimensões negativas")
        self.__altura = altura
        self.__largura = largura
    
    @property
    def largura(self):
        return self.__largura
    
    @property
    def altura(self):
        return self.__altura
    
    @property
    def area(self):
        return self.__altura*self.__largura

class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
    
    @property
    def lado(self):
        return self.__altura
    
    @lado.setter
    def lado(self, newside):
        if newside < 0:
            raise ValueError("Quadrados não podem ter lado negativo")
        self.__altura = newside
        self.__largura = newside

class Triangulo:
    def __init__(self, l1, l2, l3):
        if (l1+l2 < l3) or (l2+l3<l1) or (l3+l1<l2):
            raise ValueError("Impossível existir um triângulo com tais medidas")
        self.__lado1 = l1
        self.__lado2 = l2
        self.__lado3 = l3
    
    @property
    def area(self):
        semiper = (self.__lado1 + self.__lado2 + self.__lado3)/2
        return (semiper*(semiper-self.__lado1)*(semiper-self.__lado2)*(semiper-self.__lado3))**(1/2)

class Circulo:
    def __init__(self,raio):
        self.__raio = raio
    
    @property
    def area(self):
        return 3.141592*self.__raio**2