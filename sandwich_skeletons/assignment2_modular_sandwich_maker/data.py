"""Shared data structures and constants for the Modular Sandwich Maker - Skeleton."""
from typing import Dict

MENU: Dict[str, Dict[str, object]] = {
    "small": {"cost": 2.5, "ingredients": {"bread": 2, "ham": 50, "cheese": 20, "mayo": 10}},
    "medium": {"cost": 3.5, "ingredients": {"bread": 3, "ham": 75, "cheese": 30, "mayo": 15}},
    "large": {"cost": 4.5, "ingredients": {"bread": 4, "ham": 100, "cheese": 40, "mayo": 20}},
}

INITIAL_RESOURCES: Dict[str, int] = {
    "bread": 20,
    "ham": 500,
    "cheese": 200,
    "mayo": 150,
    "money": 0,
}

COIN_VALUES = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}