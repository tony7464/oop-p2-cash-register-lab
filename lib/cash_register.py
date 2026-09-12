#!/usr/bin/env python3


class CashRegister:
    """Tracks a cart total, line items, optional percent discount, and sale history."""

    def __init__(self, discount=0):
        # discount is a percent off the cart (20 means 20% off). Defaults to 0.
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Only whole-number percentages from 0 through 100 are accepted.
        if isinstance(value, int) and not isinstance(value, bool) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            # Keep a usable default if initialization received a bad value.
            if not hasattr(self, "_discount"):
                self._discount = 0

    def add_item(self, item, price, quantity=1):
        """Add one or more of the same item, update the total, and log the sale."""
        self.total += price * quantity
        # Repeat the title so `items` includes every unit purchased.
        self.items.extend([item] * quantity)
        self.previous_transactions.append(
            {"item": item, "price": price, "quantity": quantity}
        )

    def apply_discount(self):
        """Take the configured percent off the current total, if a discount exists."""
        if not self.discount or not self.previous_transactions:
            print("There is no discount to apply.")
            return

        self.total = int(self.total * ((100 - self.discount) / 100))
        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        """Undo the most recent add_item call, including its quantity."""
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()
        quantity = last_transaction["quantity"]
        self.total -= last_transaction["price"] * quantity
        # Drop the same number of item titles that this transaction added.
        del self.items[-quantity:]
