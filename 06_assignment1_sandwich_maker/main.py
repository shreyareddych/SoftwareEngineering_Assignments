# main.py

MENU = {
    "bread": {"white": 2.00, "wheat": 2.25, "sourdough": 2.50},
    "protein": {"turkey": 3.00, "chicken": 3.00, "tofu": 2.50},
    "cheese": {"cheddar": 1.00, "swiss": 1.20, "none": 0.00},
    "toppings": {"lettuce": 0.30, "tomato": 0.40, "onion": 0.25, "pickles": 0.25, "none": 0.00},
}

def choose_one(category: str) -> tuple[str, float]:
    items = list(MENU[category].items())
    print(f"\nChoose {category}:")
    for i, (name, price) in enumerate(items, 1):
        print(f"{i}) {name} (${price:.2f})")
    while True:
        try:
            idx = int(input("Enter choice #: ").strip())
            if 1 <= idx <= len(items):
                return items[idx - 1]  # (name, price)
        except ValueError:
            pass
        print("Invalid choice, try again.")

def choose_multi(category: str) -> list[tuple[str, float]]:
    items = list(MENU[category].items())
    print(f"\nChoose {category} (comma-separated numbers, or 0 for none):")
    for i, (name, price) in enumerate(items, 1):
        print(f"{i}) {name} (${price:.2f})")
    while True:
        picks = input("Enter choice(s): ").strip()
        if picks == "0":
            return [("none", 0.00)]
        try:
            idxs = [int(x) for x in picks.split(",") if x.strip()]
            if all(1 <= i <= len(items) for i in idxs):
                # dedupe while preserving order
                seen, res = set(), []
                for i in idxs:
                    pair = items[i - 1]
                    if pair[0] not in seen:
                        seen.add(pair[0])
                        res.append(pair)
                return res or [("none", 0.00)]
        except ValueError:
            pass
        print("Invalid choice(s), try again.")

def price_line(label: str, value: str | list[str], price: float) -> str:
    if isinstance(value, list):
        value = ", ".join(value)
    return f"{label:<10} {value:<25} ${price:>5.2f}"

def make_sandwich():
    print("=== Sandwich Maker ===")
    bread_name, bread_price = choose_one("bread")
    protein_name, protein_price = choose_one("protein")
    cheese_name, cheese_price = choose_one("cheese")
    toppings = choose_multi("toppings")

    # sum prices
    toppings_names = [n for (n, _) in toppings if n != "none"]
    toppings_price = sum(p for (_, p) in toppings)

    total = bread_price + protein_price + cheese_price + toppings_price

    # receipt
    print("\n--- Receipt ---")
    print(price_line("Bread:", bread_name, bread_price))
    print(price_line("Protein:", protein_name, protein_price))
    print(price_line("Cheese:", cheese_name, cheese_price))
    print(price_line("Toppings:", toppings_names or ["none"], toppings_price))
    print("-" * 42)
    print(f"{'Total:':<36} ${total:>5.2f}")
    print("\nEnjoy your sandwich! 🥪")

if __name__ == "__main__":
    make_sandwich()
