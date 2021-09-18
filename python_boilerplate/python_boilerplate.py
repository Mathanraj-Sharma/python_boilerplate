"""Main module."""


def print_package_description():
    print(
        "Python Boilerplate contains all the boilerplate you need to create a Python package."
    )


# sample class for pytest fixture example
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        temp_balance = self.balance - amount

        if temp_balance > 0:
            self.balance = temp_balance
            return self.balance
        else:
            return None

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def peek_balance(self):
        return self.balance
