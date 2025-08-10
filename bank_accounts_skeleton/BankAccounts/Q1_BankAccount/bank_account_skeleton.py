# bank_account_skeleton.py
"""Skeleton for BankAccount assignment (Q1).
Implement according to rubric:
- Class attribute: bank title
- Instance attrs: customer_name, current_balance, minimum_balance
- Methods: deposit, withdraw (with validation), print_customer_information
"""

class BankAccount:
    # TODO: add class attribute for bank title, e.g., bank_title = "Your Bank"
    # bank_title = "Your Bank"
    
    def __init__(self, customer_name: str, current_balance: float, minimum_balance: float):
        """Initialize attributes.
        TODO:
        - store customer_name
        - store current_balance
        - store minimum_balance
        """
        pass

    def deposit(self, amount: float) -> None:
        """TODO: increase balance by amount if amount > 0."""
        pass

    def withdraw(self, amount: float) -> None:
        """TODO: decrease balance if amount > 0 and does not break minimum balance."""
        pass

    def print_customer_information(self) -> None:
        """TODO: print bank title, customer name, current balance, minimum balance."""
        pass
