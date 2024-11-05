class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

# Demonstration
account = BankAccount()
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Should output the current balance
