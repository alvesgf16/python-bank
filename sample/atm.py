from bank import Bank
from helpers.clear import clear_screen


class ATM:
    @classmethod
    def main(cls):
        bank = cls.__setup()

        while True:
            authed_account = cls.__auth(bank)
            clear_screen()

            while True:
                cls.__display_menu(authed_account)
                op = int(input("Enter your option: "))
                clear_screen()

                if op < 1 or op > 6:
                    print("Invalid option, choose a valid option.")
                elif op == 6:
                    print("Logout successful!")
                    break
                else:
                    cls.__perform_operation(op, authed_account, bank)

    @staticmethod
    def __setup():
        bank = Bank()

        customers_data = [
            (
                "Alexiania Pereira",
                "842.074.410-77",
                (("savings", 12700), ("current", 7300)),
            ),
            (
                "Abadiania Silva",
                "848.725.510-87",
                (("savings", 5600), ("savings", 300)),
            ),
            (
                "Camaragibe Oliveira",
                "433.892.200-11",
                (("current", 53000), ("current", 12200)),
            ),
        ]

        for name, cpf, accounts_data in customers_data:
            customer = bank.add_customer(name, cpf)

            for account_type, initial_deposit in accounts_data:
                bank.add_account(
                    account_type, customer, "1234", initial_deposit
                )

        return bank

    @staticmethod
    def __auth(bank):
        authed_account = None

        while True:
            print("\n\nWelcome to Python Bank!\n\n")
            account_number = input("Enter an account number: ")
            password = input("Enter the account password: ")

            authed_account = bank.login(account_number, password)

            if authed_account is None:
                print(
                    "Incorrect account number and password combination. "
                    + "Try again."
                )
            else:
                return authed_account

    @staticmethod
    def __display_menu(authed_account):
        print(authed_account)
        print()
        print("What would you like to do?")
        print("  1) Show statement")
        print("  2) Withdraw")
        print("  3) Deposit")
        print("  4) Transfer")
        print("  5) Simulate an investment")
        print("  6) Exit")
        print()

    @classmethod
    def __perform_operation(cls, option, authed_account, bank):
        if option == 1:
            cls.__return_statement(authed_account)

        elif option == 2:
            cls.__withdraw(authed_account)

        elif option == 3:
            cls.__deposit(authed_account)

        elif option == 4:
            cls.__transfer_funds(authed_account, bank)

        elif option == 5:
            cls.__simulate_investment(authed_account)

    @staticmethod
    def __return_statement(account):
        account.return_statement()

    @classmethod
    def __withdraw(cls, account):
        account_balance = account.return_balance()
        amount = cls.__get_outbound_amount("withdrawn", account_balance)

        account.withdraw(amount)

    @classmethod
    def __deposit(cls, account):
        amount = cls.__get_inbound_amount("deposit amount")

        account.deposit(amount)

    @classmethod
    def __transfer_funds(cls, account, bank):
        amount = 0
        destination_account = None

        if account.type == ("current"):
            account_balance = account.return_balance()
            amount = cls.__get_outbound_amount("transferred", account_balance)
            destination_account = cls.__get_destination_account(bank)

        account.transfer_funds(amount, destination_account)

    @classmethod
    def __simulate_investment(cls, account):
        initial_value, final_value = 0, 0

        if account.type == ("savings"):
            initial_value = cls.__get_inbound_amount(
                "initial value of the simulation"
            )

            final_value = cls.__get_inbound_amount(
                "desired final value", initial_value, "the initial value"
            )

        account.simulate_investment(initial_value, final_value)

    @classmethod
    def __get_destination_account(cls, bank):
        destination_account = None
        destination_account_number = input(
            "Enter the number of the account that will receive the "
            + "transfer: "
        )

        for account in bank.accounts:
            if account.id == destination_account_number:
                destination_account = account

        if not destination_account or destination_account == cls:
            print("Invalid account number, please try again.")

        return destination_account or cls.__get_destination_account(bank)

    @classmethod
    def __get_inbound_amount(
        cls, type, lower_limit=0.0, limit_description="zero"
    ):
        amount = float(input(f"Enter the {type}: BRL"))

        if amount <= lower_limit:
            print(f"Amount must be greater than {limit_description}.")

        return (
            amount
            if amount > lower_limit
            else cls.__get_inbound_amount(type, lower_limit, limit_description)
        )

    @classmethod
    def __get_outbound_amount(cls, type, account_balance):
        amount = float(
            input(
                f"Enter the amount to be {type} (max.: BRL "
                + f"{account_balance:.2f}): BRL "
            )
        )

        if amount < 0:
            print("Amount must be greater than zero.")
        elif amount > account_balance:
            print(
                "Amount cannot be greater than the balance of BRL "
                + f"{account_balance:.2f}."
            )

        return (
            amount
            if 0 < amount <= account_balance
            else cls.__get_outbound_amount(type, account_balance)
        )


if __name__ == "__main__":
    ATM.main()
