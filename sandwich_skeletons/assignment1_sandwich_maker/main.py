"""
Ham Sandwich Maker Machine (Interactive CLI) - Skeleton
Part 1 requirements summary:
  - Prompt user to choose sandwich size or commands: 'report', 'off'.
  - Check resources per order; reject if insufficient and show which resource.
  - Handle coin input (quarters, dimes, nickels, pennies) and pricing per size.
  - Complete transaction: accept/reject payment, return change.
  - Update resources after making a sandwich.
  - Print resource report on demand.

Replace all 'pass' / TODOs with working code.
DO NOT rename functions or constants; graders may import these by name.
"""

from typing import Dict, Tuple

# ---------------------- Constants (example placeholders) ----------------------
MENU: Dict[str, Dict[str, object]] = {
    # price in dollars; ingredients in 'ml' or 'g' as appropriate
    "small": {"cost": 2.5, "ingredients": {"bread": 2, "ham": 50, "cheese": 20, "mayo": 10}},
    "medium": {"cost": 3.5, "ingredients": {"bread": 3, "ham": 75, "cheese": 30, "mayo": 15}},
    "large": {"cost": 4.5, "ingredients": {"bread": 4, "ham": 100, "cheese": 40, "mayo": 20}},
}

RESOURCES: Dict[str, int] = {
    # starting inventory (example values)
    "bread": 20,   # slices
    "ham": 500,    # grams
    "cheese": 200, # grams
    "mayo": 150,   # ml
    "money": 0,    # cents or dollars depending on implementation
}

COIN_VALUES: Dict[str, float] = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

# ---------------------- Core helpers (implement these) ----------------------

def print_report(resources: Dict[str, int]) -> None:
    """Print remaining resources and money collected in a human-friendly format."""
    # TODO: pretty-print each resource and the money total
    pass

def is_resource_sufficient(needed: Dict[str, int], resources: Dict[str, int]) -> Tuple[bool, str]:
    """
    Return (ok, missing_name). If any resource is insufficient, ok=False and missing_name names it.
    Excludes 'money' from checks.
    """
    # TODO: iterate over needed ingredients and compare with resources
    pass

def process_coins() -> float:
    """Prompt user for coin counts and return the total inserted as a float dollars."""
    # TODO: input() quarters/dimes/nickels/pennies and compute total
    pass

def complete_transaction(payment: float, cost: float) -> Tuple[bool, float]:
    """Return (accepted, change). Accept if payment>=cost; change is payment-cost if accepted else 0."""
    # TODO
    pass

def make_sandwich(size: str, resources: Dict[str, int]) -> None:
    """Deduct ingredients for the given size from resources; increment money collected."""
    # TODO
    pass

def get_user_choice() -> str:
    """Read a user command/size: one of {'small','medium','large','report','off'}."""
    # TODO: return sanitized input
    pass

# ---------------------- Main loop ----------------------

def main() -> None:
    """Interactive loop. Implement the machine workflow described in the doc."""
    # Pseudocode guideline (you can adjust):
    # while True:
    #   choice = get_user_choice()
    #   if choice == 'off': break
    #   if choice == 'report': print_report(RESOURCES); continue
    #   if choice in MENU:
    #       ok, missing = is_resource_sufficient(MENU[choice]['ingredients'], RESOURCES)
    #       if not ok: print(f"Sorry, not enough {missing}."); continue
    #       payment = process_coins()
    #       accepted, change = complete_transaction(payment, float(MENU[choice]['cost']))
    #       if not accepted: print("Sorry, that's not enough money. Money refunded."); continue
    #       if change > 0: print(f"Here is ${change:.2f} in change.")
    #       make_sandwich(choice, RESOURCES)
    #       print(f"Here is your {choice} ham sandwich. Enjoy!")
    #   else:
    #       print("Invalid selection, try again.")
    pass

if __name__ == "__main__":
    main()