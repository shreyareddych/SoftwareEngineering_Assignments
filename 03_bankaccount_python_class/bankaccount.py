class BankAccount:
    bank_title = "Global Trust Bank"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"Deposited ${amount} successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self.current_balance - amount < self.minimum_balance:
            print(f"Cannot withdraw ${amount}. Minimum balance requirement not met.")
        else:
            self.current_balance -= amount
            print(f"Withdrew ${amount} successfully.")

    def print_customer_information(self):
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: ${self.current_balance}")
        print(f"Minimum Balance: ${self.minimum_balance}")


account1 = BankAccount("Alice Johnson", 1000, 200)
account2 = BankAccount("Bob Smith", 500, 100)

account1.deposit(300)
account1.withdraw(950)
account1.print_customer_information()

print("----------------------------")

account2.deposit(200)
account2.withdraw(550)
account2.print_customer_information()
