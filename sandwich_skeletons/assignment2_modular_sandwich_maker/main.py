"""Entry point for the Modular Sandwich Maker - Skeleton.

Structure:
  - data.py: shared constants (MENU, INITIAL_RESOURCES, COIN_VALUES)
  - inventory.py: resource checks & deduction
  - payments.py: coin collection & settlement
  - machine.py: SandwichMachine orchestration
  - ui.py: simple CLI layer
"""
from typing import Dict
# If using a flat module layout (same folder), these imports are fine:
import data, inventory, payments, machine, ui

def run(resources: Dict[str, int]) -> None:
    sm = machine.SandwichMachine(resources)
    while True:
        choice = ui.prompt_choice()
        if choice == "off":
            break
        if choice == "report":
            ui.show_message(sm.report())
            continue
        if choice in data.MENU:
            ok, missing = sm.can_make(choice)
            if not ok:
                ui.show_message(f"Sorry, not enough {missing}." )
                continue
            payment = payments.collect_coins(data.COIN_VALUES)
            accepted, change = payments.settle(payment, float(data.MENU[choice]["cost"]))  # type: ignore[index]
            if not accepted:
                ui.show_message("Sorry, that's not enough money. Money refunded.")
                continue
            if change > 0:
                ui.show_message(f"Here is ${change:.2f} in change.")
            sm.make(choice)
            ui.show_message(f"Here is your {choice} ham sandwich. Enjoy!")
        else:
            ui.show_message("Invalid selection, try again.")

if __name__ == "__main__":
    run(dict(data.INITIAL_RESOURCES))