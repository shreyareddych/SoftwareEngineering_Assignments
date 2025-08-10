# bank/base_skeleton.py
"""Base account class (skeleton) for Question 2."""

from __future__ import annotations

class BankAccount:
    # TODO: class attribute for bank title
    # bank_title = "Your Bank"

    def __init__(self, customer_name: str, opening_balance: float, account_number: str, routing_number: str):
        """Store core state.
        TODO:
        - public: customer_name
        - public: balance (float)
        - private: __account_number
        - protected: _routing_number
        """
        pass

    # TODO: read-only properties that mask numbers (e.g., ****1234)
    # @property
    # def account_number(self) -> str: ...

    # @property
    # def routing_number(self) -> str: ...

    def deposit(self, amount: float) -> float:
        """TODO: validate and add to balance. Return new balance."""
        pass

    def withdraw(self, amount: float) -> float:
        """TODO: validate and subtract from balance if sufficient."""
        pass

    def transfer(self, other: "BankAccount", amount: float) -> None:
        """TODO: withdraw here and deposit to 'other'."""
        pass

    def print_customer_information(self) -> None:
        """TODO: print masked account info and current balance."""
        pass
