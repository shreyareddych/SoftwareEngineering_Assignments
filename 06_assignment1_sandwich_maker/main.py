# main.py

# Recipes (sizes -> ingredients + cost)
RECIPES = {
    "small":  {"ingredients": {"bread": 2, "ham": 4, "cheese": 4},  "cost": 1.75},
    "medium": {"ingredients": {"bread": 4, "ham": 6, "cheese": 8},  "cost": 3.25},
    "large":  {"ingredients": {"bread": 6, "ham": 8, "cheese": 12}, "cost": 5.50},
}

# Machine starting resources chosen to match your sample run
RESOURCES = {"bread": 12, "ham": 18, "cheese": 24}


def check_resources(ingredients: dict) -> bool:
    """
    Input: ingredients (dict) -> {'bread': int, 'ham': int, 'cheese': int}
    Output: bool (True if enough resources, else False and print which is lacking)
    """
    for item, req in ingredients.items():
        if RESOURCES.get(item, 0) < req:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins() -> float:
    """
    Ask for coins and return total inserted as float.
    Accepts: large dollar ($1), half dollar ($0.5), quarter ($0.25), nickel ($0.05)
    """
    print("Please insert coins.")
    def ask(prompt):
        try:
            return int(input(prompt).strip() or "0")
        except ValueError:
            return 0

    dollars  = ask("how many large dollars?: ")
    halves   = ask("how many half dollars?: ")
    quarters = ask("how many quarters?: ")
    nickels  = ask("how many nickels?: ")

    total = dollars * 1.00 + halves * 0.50 + quarters * 0.25 + nickels * 0.05
    return round(total + 1e-9, 2)


def transaction_result(coins: float, cost: float) -> bool:
    """
    Input: coins (float), cost (float)
    Output: bool (True if enough; prints change. False if not; prints refund msg)
    """
    if coins + 1e-9 < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    change = round(coins - cost, 2)
    print(f"Here is ${change} in change.")
    return True


def make_sandwich(sandwich_size: str, ingredients: dict) -> None:
    """
    Input: sandwich_size (str), ingredients (dict)
    Output: None (side effect: deduct resources and print ready message)
    """
    for item, qty in ingredients.items():
        RESOURCES[item] -= qty
    print(f"{sandwich_size} sandwich is ready. Bon appetit!")


def print_report() -> None:
    print(f"Bread: {RESOURCES['bread']} slice(s)")
    print(f"Ham: {RESOURCES['ham']} slice(s)")
    print(f"Cheese: {RESOURCES['cheese']} pound(s)")


def main():
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").strip().lower()

        if choice == "off":
            break
        elif choice == "report":
            print_report()
        elif choice in RECIPES:
            order = RECIPES[choice]
            ingredients = order["ingredients"]
            cost = order["cost"]

            if not check_resources(ingredients):
                continue

            coins = process_coins()
            if not transaction_result(coins, cost):
                continue

            make_sandwich(choice, ingredients)
        else:
            print("Please choose from: small / medium / large / report / off")

if __name__ == "__main__":
    main()
