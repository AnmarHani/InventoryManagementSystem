from abc import ABC, abstractmethod

## Composite Pattern
class Item(ABC):
    @abstractmethod
    def get_price(self):
        pass


class Box(Item):
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def set_name(self, name):
        self.name = name
        return self

    def get_name(self):
        return self.name

    def get_price(self):
        return sum(item.get_price() for item in self.items)

    def __str__(self) -> str:
        return (
            "\n########\nItems in this box are:\n---------\n"
            + "\n".join("* " + str(item) for item in self.items)
            + "\n########\n"
        )


class SingleItem(Item):
    def __init__(self, pricing_strategy):
        self.pricing_strategy = pricing_strategy

    def set_name(self, name):
        self.name = name
        return self

    def get_name(self):
        return self.name

    def set_price(self, price):
        self.price = price
        return self

    def get_price(self):
        return self.pricing_strategy.get_price(self.price)

    def __str__(self) -> str:
        return "Item " + self.name + f" has price of {self.get_price()}"
