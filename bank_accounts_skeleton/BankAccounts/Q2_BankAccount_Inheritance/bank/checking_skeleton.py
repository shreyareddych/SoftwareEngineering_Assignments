# bank/checking_skeleton.py
"""Checking account subclass with daily transfer limit (skeleton)."""

from .base_skeleton import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name: str, opening_balance: float, account_number: str, routing_number: str, daily_transfer_limit: float = 500.0):
        super().__init__(customer_name, opening_balance, account_number, routing_number)
        # TODO: store daily_transfer_limit and initialize a protected daily tracker

    def reset_daily_limit(self) -> None:
        """TODO: reset daily transfer tracker."""
        pass

    def transfer(self, other: BankAccount, amount: float) -> None:
        """TODO: enforce daily limit then call base transfer."""
        pass
