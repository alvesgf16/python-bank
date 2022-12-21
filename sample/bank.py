from random import randint
from accounts.current_account import Current_Account
from accounts.savings_account import Savings_Account
from helpers.cpf_validator import CPF_Validator
from customer import Customer


class Bank:
    def __init__(self):
        self.__annualization = 1.35
        self.__customers = []
        self.__accounts = []

    @property
    def accounts(self):
        return self.__accounts

    @property
    def annualization(self):
        return self.__annualization

    def add_account(self, account_type, holder, password, initial_deposit):
        if holder.does_customer_have_an_account_of_type(account_type):
            print(
                f"Customer with CPF {holder.cpf} already has a "
                + f"{account_type} account."
            )
        else:
            new_account = self.__create_account(
                account_type, holder, password, initial_deposit
            )

            holder.add_account(new_account)
            self.__accounts.append(new_account)

    def add_customer(self, name, cpf):
        if CPF_Validator.validate_cpf(cpf):
            new_customer = Customer(name, cpf)

            self.__customers.append(new_customer)

            return new_customer

    def generate_new_account_number(self):
        new_account_number = "".join(str(randint(0, 9)) for _ in range(6))

        return (
            self.generate_new_account_number()
            if new_account_number
            in [account.id for account in self.__accounts]
            else new_account_number
        )

    def login(self, account_number, password):
        return next(
            (
                account
                for account in self.__accounts
                if account.id == account_number
                and account.password == password
            ),
            None,
        )

    def __create_account(
        self, account_type, holder, password, initial_deposit
    ):
        if account_type == "savings":
            return Savings_Account(password, holder, initial_deposit, self)
        if account_type == "current":
            return Current_Account(password, holder, initial_deposit, self)
