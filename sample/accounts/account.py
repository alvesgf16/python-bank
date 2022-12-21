from abc import ABCMeta, abstractmethod
from transaction import Transaction


class Account(metaclass=ABCMeta):
    def __init__(self, password, holder, initial_deposit, bank):
        self.__id = bank.generate_new_account_number()
        self.__password = password
        self.__holder = holder
        self.__transactions = []

        self.__add_transaction(initial_deposit, "Initial deposit")
        print(f"Account number {self.__id} created!")

    @property
    def id(self):
        return self.__id

    @property
    def password(self):
        return self.__password

    @property
    def holder_cpf(self):
        return self.__holder.cpf

    def __str__(self):
        return f"{self.__id} : BRL {self.return_balance():.2f}"

    def deposit(self, amount):
        self.__add_transaction(amount, "Deposit received")

    def withdraw(self, amount):
        self.__add_transaction(-amount, "Withdrawal made")

    def return_balance(self):
        return sum(transaction.amount for transaction in self.__transactions)

    def return_statement(self):
        print(f"Statement from account {self.__id}")
        print("")
        for transaction in self.__transactions:
            print(transaction)

    @abstractmethod
    def transfer_funds(self, amount, destination_account):
        pass

    @abstractmethod
    def simulate_investment(self, initial_value, final_value):
        pass

    def __add_transaction(self, amount, description):
        self.__transactions.append(Transaction(amount, description))
