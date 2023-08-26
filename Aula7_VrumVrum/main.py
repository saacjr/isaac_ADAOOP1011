from veiculos import *

corolla = Carro('Toyota', 'Corolla', 4)
cbr = Moto('Honda', 'CBR500R', 500)
kicks = Carro('Nissan', 'Kicks', 4)
pg208 = Carro('Peugeot', '208', 2)
forza = Moto('Honda', 'Forza', 350)

listagem = [forza, pg208, kicks, cbr, corolla]

for veic in listagem:
    print(veic)
