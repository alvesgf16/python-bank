from datetime import date
from accounts.account import Account


class Savings_Account(Account):
    def __init__(self, password, holder, initial_deposit, bank):
        super(Savings_Account, self).__init__(
            password, holder, initial_deposit, bank
        )
        self.__type = 'savings'
        self.__bank = bank

    @property
    def type(self):
        return self.__type

    def transfer_funds(self, amount, destination_account):
        print("It is not possible make transfers on a savings account.")

    def simulate_investment(self, initial_value, final_value):
        investment_return = initial_value
        year = date.today().year

        while investment_return < final_value:
            investment_return *= self.__bank.annualization
            year += 1

        print(
            f"With an initial value of {initial_value} you'll reach the "
            + f"final value of {final_value} in {year}."
        )
