from abc import ABC, abstractmethod
from typing import Dict, Optional, Type, Union, List, TYPE_CHECKING

if TYPE_CHECKING:
    from behavioural.strategy import PricingStrategy

## Composite Pattern
class Item(ABC):
    name: str
    price: float
    
    @abstractmethod
    def get_price(self) -> float:
        """
        This method calculates the price of the item.
        """

        pass


class Box(Item):

    def __init__(self) -> None:
        """
        This method initializes the Box class and creates an empty list of items.
        """

        self.items: List[Item] = []

    def add_item(self, item: Item) -> None:
        """
        This method adds an item to the box. It takes an item as an argument.
        """

        self.items.append(item)

    def set_name(self, name: str) -> "Box":
        """
        This method sets the name of the box. It takes a name as an argument.
        """

        self.name = name
        return self

    def get_name(self) -> str:
        """
        This method returns the name of the box.
        """

        return self.name

    def get_price(self) -> float:
        """
        This method calculates the total price of all items in the box.
        """

        return sum(item.get_price() for item in self.items)

    def __str__(self) -> str:
        """
        This method returns a string representation of the box and its items.
        """

        return (
            "\n########\nItems in this box are:\n---------\n"
            + "\n".join("* " + str(item) for item in self.items)
            + "\n########\n"
        )


class SingleItem(Item):
    def __init__(self, pricing_strategy: "PricingStrategy") -> None:
        """
        This method initializes the SingleItem class and sets the pricing strategy. It takes a pricing strategy as an argument.
        """

        self.pricing_strategy = pricing_strategy

    def set_name(self, name: str) -> "SingleItem":
        """
        This method sets the name of the item. It takes a name as an argument.
        """

        self.name = name
        return self

    def get_name(self) -> str:
        """
        This method returns the name of the item.
        """

        return self.name

    def set_price(self, price: float) -> "SingleItem":
        """
        This method sets the price of the item. It takes a price as an argument.
        """

        self.price = price
        return self

    def get_price(self) -> float:
        """
        This method calculates the price of the item based on the pricing strategy.
        """

        return self.pricing_strategy.get_price(self.price)

    def __str__(self) -> str:
        """
        This method returns a string representation of the item and its price.
        """

        return "Item " + self.name + f" has price of {self.get_price()}"
