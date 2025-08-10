# bank/savings_skeleton.py
"""Savings account subclass with interest (skeleton)."""

from .base_skeleton import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name: str, opening_balance: float, account_number: str, routing_number: str, interest_rate: float = 0.02):
        super().__init__(customer_name, opening_balance, account_number, routing_number)
        # TODO: store interest_rate

    def apply_interest(self) -> float:
        """TODO: apply one period of interest and return new balance."""
        pass
