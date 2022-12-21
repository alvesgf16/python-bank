from accounts.account import Account


class Current_Account(Account):
    def __init__(self, password, holder, initial_deposit, bank):
        super(Current_Account, self).__init__(
            password, holder, initial_deposit, bank
        )
        self.__type = 'current'

    @property
    def type(self):
        return self.__type

    def transfer_funds(self, amount, destination_account):
        self.__add_transaction(-amount, "Transfer sent")
        destination_account.add_transaction(amount, "Transfer received")

    def simulate_investment(self, initial_value, final_value):
        print("A current account does not bear interest.")
