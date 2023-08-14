class Fracional:
    def __init__(self, numerador, denominador) -> None:
        self.numerador = numerador
        self.denominador = denominador
        
    def __str__(self):
        return f'{self.numerador}/{self.denominador}'
    
    def soma(self, other):
        numerador = self.numerador*other.denominador + self.denominador*other.numerador
        denominador = self.denominador*other.denominador
        
        return Fracional(numerador, denominador)
    
    def sub(self, other):
        numerador = self.numerador*other.denominador - self.denominador*other.numerador
        denominador = self.denominador*other.denominador
        
        return Fracional(numerador, denominador)
    
    def mul(self, other):
        numerador = self.numerador*other.numerador
        denominador = self.denominador*other.denominador
        
        return Fracional(numerador, denominador)
    
    def div(self, other):
        
        return self.mul(Fracional(other.denominador, other.numerador))
    
print('---- Testes ----\n')

meio = Fracional(1,2)
terco = Fracional(1,3)

print('soma:            1/2 + 1/3 = ', meio.soma(terco))
print('subtração:       1/3 - 1/2 = ', terco.sub(meio))
print('multiplicação:   1/3 * 1/2 = ', terco.mul(meio))
print('divisão:         1/2 / 1/3 = ', meio.div(terco))