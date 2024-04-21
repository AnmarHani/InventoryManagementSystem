from abc import ABC, abstractmethod
from typing import Dict, Optional, Type, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from structural.composite import Item
    from creational.singleton import Inventory
    from behavioural.observer import Observable

## Adapter Pattern
class InventoryAdapter:
    def __init__(self, inventory: "Inventory", observable: "Observable") -> None:
        """
        This method initializes the InventoryAdapter class. It takes an inventory and an observable as arguments.
        """

        self.inventory = inventory
        self.observable = observable

    def add_item(self, item: "Item", quantity: int) -> None:
        """
        This method adds an item to the inventory and notifies all observers. It takes an item and a quantity as arguments.
        """

        self.inventory.add_item(item, quantity)
        self.observable.notify(f"Added Item: {item.get_name()} to Inventory")

    def remove_item(self, item: "Item", quantity: int) -> None:
        """
        This method removes an item from the inventory and notifies all observers. It takes an item and a quantity as arguments.
        """

        if item in self.inventory.items and self.inventory.items[item] >= quantity:
            self.inventory.items[item] -= quantity
            self.observable.notify(
                f"Removed Item: {item.get_name()} with Quanitity: {quantity} from Inventory"
            )

            if self.inventory.items[item] == 0:
                del self.inventory.items[item]
        else:
            raise ValueError("Not enough quantity in inventory")

    def check_item(self, item: "Item") -> Optional[int]:
        """
        This method checks the quantity of an item in the inventory. It takes an item as an argument.
        """

        return self.inventory.items.get(item)
