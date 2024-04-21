from abc import ABC, abstractmethod
from structural.composite import Box, SingleItem

## Factory Pattern
class ItemFactory(ABC):
    @abstractmethod
    def create_item(self, item_type):
        pass


class ConcreteItemFactory(ItemFactory):
    def create_item(self, item_type, pricing_strategy=None):
        if item_type == "Box":
            return Box()
        elif item_type == "SingleItem":
            return SingleItem(pricing_strategy)
        else:
            raise ValueError("Invalid item type")
