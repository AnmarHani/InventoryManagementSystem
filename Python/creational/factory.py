from abc import ABC, abstractmethod
from typing import Dict, Optional, Type, Union, TYPE_CHECKING

from typing import TYPE_CHECKING

from structural.composite import Box, SingleItem

if TYPE_CHECKING:
    from structural.composite import Item
    from behavioural.strategy import PricingStrategy

## Factory Pattern
class ItemFactory(ABC):
    @abstractmethod
    def create_item(self, item_type: str, pricing_strategy: Optional["PricingStrategy"] = None) -> "Item":
        """
        This method creates an item based on the item type. It takes the item type as an argument.
        """

        pass


class ConcreteItemFactory(ItemFactory):
    def create_item(
        self, item_type: str, pricing_strategy: Optional["PricingStrategy"] = None
    ) -> "Item":
        """
        This method creates an item based on the item type. It takes the item type and an optional pricing strategy as arguments.
        """

        if item_type == "Box":
            return Box()
        elif item_type == "SingleItem":
            return SingleItem(pricing_strategy)
        else:
            raise ValueError("Invalid item type")
