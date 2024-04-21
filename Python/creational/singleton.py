from abc import ABC, abstractmethod
from typing import Dict, Optional, Type, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from structural.composite import Item

## Singleton Pattern
class Inventory:
    _instance = None
    items: Dict["Item", int] = {}
    name: str = ""

    @staticmethod
    def get_instance() -> "Inventory":
        """
        This method returns the singleton instance of the Inventory class.
        """

        if Inventory._instance is None:
            return Inventory()
        return Inventory._instance

    @staticmethod
    def add_item(item: "Item", quantity: int) -> None:
        """
        This method adds an item to the inventory. It takes an item and a quantity as arguments.
        """

        Inventory.items[item] = quantity

    @staticmethod
    def set_name(name: str) -> str:
        """
        This method sets the name of the inventory. It takes a name as an argument.
        """

        Inventory.name = name
        return Inventory.name

    @staticmethod
    def __str__() -> str:
        """
        This method returns a string representation of the inventory.
        """

        return f"Inventory {Inventory.name} has: {Inventory.items}"
