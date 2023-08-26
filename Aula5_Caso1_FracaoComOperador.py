class Fracional:
    def __init__(self, numerador, denominador) -> None:
        if denominador == 0:
            raise ZeroDivisionError('Denominador não pode ser nulo')
        self.__numerador = numerador
        self.__denominador = denominador
        
    def __str__(self):
        return f'{self.numerador}/{self.denominador}'
    
    def __add__(self, other):
        numerador = self.__numerador*other.__denominador + self.__denominador*other.__numerador
        denominador = self.__denominador*other.__denominador
        
        return Fracional(numerador, denominador)
    
    def __sub__(self, other):
        numerador = self.__numerador*other.__denominador - self.__denominador*other.__numerador
        denominador = self.__denominador*other.__denominador
        
        return Fracional(numerador, denominador)
    
    def __mul__(self, other):
        numerador = self.__numerador*other.__numerador
        denominador = self.__denominador*other.__denominador
        
        return Fracional(numerador, denominador)
    
    def __truediv__(self, other):
        numerador = self.__numerador*other.__denominador
        denominador = self.__denominador*other.__numerador
        
        return Fracional(numerador, denominador)
    
    def __gt__(self, other):
        
        return self.__numerador*other.__denominador > self.__denominador*other.__numerador
    
    def __ge__(self, other):
        
        return self.__numerador*other.__denominador >= self.__denominador*other.__numerador
    
    def __lt__(self, other):
        
        return self.__numerador*other.__denominador < self.__denominador*other.__numerador
    
    def __le__(self, other):
        
        return self.__numerador*other.__denominador <= self.__denominador*other.__numerador
    
    def __eq__(self, other):
        
        return self.__numerador*other.__denominador == self.__denominador*other.__numerador
    
    def __neq__(self, other):
        
        return self.__numerador*other.__denominador != self.__denominador*other.__numerador
    
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

print('---- Operações ----\n')

meio = Fracional(1,2)
terco = Fracional(1,3)

print('soma:            1/2 + 1/3 = ', meio + terco)
print('subtração:       1/3 - 1/2 = ', terco - meio)
print('multiplicação:   1/3 * 1/2 = ', terco * meio)
print('divisão:         1/2 / 1/3 = ', meio / terco)

print('---- Comparações ----')
print('>    1/2 > 1/3:', meio > terco)
print('<    1/2 > 1/3:', meio < terco)
print('>=   1/2 > 1/3:', meio >= terco)
print('<=   1/2 > 1/3:', meio <= terco)
print('!=   1/2 > 1/3:', meio != terco)
print('==   1/2 > 1/3:', meio == terco)
