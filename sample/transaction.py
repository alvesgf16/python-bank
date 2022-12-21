from datetime import datetime


class Transaction:
    def __init__(self, amount, description):
        self.__amount = amount
        self.__time = self.return_time()
        self.__description = description

    @property
    def amount(self):
        return self.__amount

    def __str__(self):
        return (
            f"{self.__time} -------- {self.__description}: "
            + f"BRL {self.__format_displayed_amount()}"
        )

    def __format_displayed_amount(self):
        return (
            f"{self.__amount:.2f} +"
            if self.__amount > 0
            else f"{abs(self.__amount):.2f} -"
        )

    def return_time(self):
        return datetime.now()
