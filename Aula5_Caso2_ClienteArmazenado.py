class Cliente:
    __clientes = []
    
    def __init__(self, nome, cpf):
        if not valida_cpf(cpf):
            raise ValueError('CPF inválido!') 
        self.__nome = nome
        self.__cpf = cpf
        self.__conta = None
        Cliente.__clientes.append(self)
        
    @staticmethod
    def valida_cpf(cpf):
        cont = 0
        fixa = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        n_cpf = []
        for x in cpf:
            if x.isnumeric():
                if cont < 9:
                    cont += 1
                    n_cpf.append(int(x))
        validador_n1 = list(zip(n_cpf, fixa))
        validador_n1 = [a * b for (a, b) in validador_n1]
        validador_n1 = (sum(validador_n1) * 10) % 11
        if validador_n1 == 10:
            validador_n1 = 0
        if str(validador_n1) != cpf[-2]:
            return False
        else:
            fixa = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
            n_cpf.append(validador_n1)
            validador_n2 = list(zip(n_cpf, fixa))
            validador_n2 = [a * b for (a, b) in validador_n2]
            validador_n2 = (sum(validador_n2) * 10) % 11
            if validador_n2 == 10:
                validador_n2 = 0
            if str(validador_n1) == cpf[0] or str(validador_n1) == cpf[1] or str(validador_n1) == cpf[2]:
                return False
            else:
                if str(validador_n1) + str(validador_n2) == cpf[-2:]:
                    return True
                else:
                    return False
                
    @classmethod
    def mostrar_clientes(cls):
        for cliente in cls.__clientes:
            print(cliente)
    
    @classmethod
    def buscar_cliente(cls, termo):
        for cliente in cls.__clientes:
            if termo in cliente.__nome or termo in cliente.__cpf:
                print(cliente)

    def vincular_conta(self, conta):
        if conta in [cliente.__conta for cliente in Cliente.__clientes]:
            raise ValueError('Conta já vinculada a cliente')
        self.__conta = conta

    def __str__(self):
        return f"Cliente: {self.__nome} (CPF: {self.__cpf})"