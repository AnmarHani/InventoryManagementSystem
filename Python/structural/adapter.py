from abc import ABC, abstractmethod

## Adapter Pattern
class InventoryAdapter:
    def __init__(self, inventory, observable):
        self.inventory = inventory
        self.observable = observable

    def add_item(self, item, quantity):
        self.inventory.add_item(item, quantity)
        self.observable.update(f"Added Item: {item.get_name()} to Inventory")

    def remove_item(self, item, quantity):
        if item in self.inventory.items and self.inventory.items[item] >= quantity:
            self.inventory.items[item] -= quantity
            self.observable.update(f"Removed Item: {item.get_name()} with Quanitity: {quantity} from Inventory")

            if self.inventory.items[item] == 0:
                del self.inventory.items[item]
        else:
            raise ValueError("Not enough quantity in inventory")

    def check_item(self, item):
        return self.inventory.items.get(item)
