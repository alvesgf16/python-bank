class Customer:
    def __init__(self, name, cpf):
        self.__name = name
        self.__cpf = cpf
        self.__accounts = []

        print(
            f"New customer {self.__name} with CPF {self.__cpf} created!"
        )

    @property
    def name(self):
        return self.__name

    @property
    def cpf(self):
        return self.__cpf

    def add_account(self, account):
        self.__accounts.append(account)

    def does_customer_have_an_account_of_type(self, account_type):
        return account_type in [account.type for account in self.__accounts]
