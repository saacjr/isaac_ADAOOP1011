class Fracional:
    def __init__(self, numerador, denominador) -> None:
        if denominador == 0:
            raise ZeroDivisionError('Denominador não pode ser nulo')
        self.__numerador = numerador
        self.__denominador = denominador
        
    def __str__(self):
        return f'{self.numerador}/{self.denominador}'
    
    def soma(self, other):
        numerador = self.__numerador*other.__denominador + self.__denominador*other.__numerador
        denominador = self.__denominador*other.__denominador
        
        return Fracional(numerador, denominador)
    
    def sub(self, other):
        numerador = self.__numerador*other.__denominador - self.__denominador*other.__numerador
        denominador = self.__denominador*other.__denominador
        
        return Fracional(numerador, denominador)
    
    def mul(self, other):
        numerador = self.__numerador*other.__numerador
        denominador = self.__denominador*other.__denominador
        
        return Fracional(numerador, denominador)
    
    def div(self, other):
        numerador = self.__numerador*other.__denominador
        denominador = self.__denominador*other.__numerador
        
        return Fracional(numerador, denominador)
    
    @property
    def numerador(self):
        return self.__numerador
    
    @numerador.setter
    def numerador(self, num):
        self.__numerador = num
    
    @property
    def denominador(self):
        return self.__denominador
    
    @denominador.setter
    def denominador(self, den):
        if den == 0:
            raise ZeroDivisionError('Denominador não pode ser nulo')
        self.__denominador = den
    