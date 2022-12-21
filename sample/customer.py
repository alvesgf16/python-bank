class Customer:
    def __init__(self, name, cpf):
        self.__name = name
        self.__cpf = cpf

        print(
            f"New customer {self.__name} with CPF {self.__cpf} created!"
        )

    @property
    def name(self):
        return self.__name

    @property
    def cpf(self):
        return self.__cpf
