from abc import ABC, abstractmethod
from typing import List, Dict

# Creational Patterns


## Singleton Pattern
class Inventory:
    _instance = None
    items: dict[object, int] = {}
    name: str = ""

    @staticmethod
    def get_instance() -> object | None:
        if Inventory._instance is None:
            return Inventory()
        return Inventory._instance

    @staticmethod
    def add_item(item, quantity):
        Inventory.items[item] = quantity

    @staticmethod
    def set_name(name: str) -> str:
        Inventory.name = name
        return Inventory.name

    @staticmethod
    def __str__():
        return f"Inventory {Inventory.name} has: {Inventory.items}"


## Factory Pattern
class ItemFactory(ABC):
    @abstractmethod
    def create_item(self, item_type):
        pass


class ConcreteItemFactory(ItemFactory):
    def create_item(self, item_type):
        if item_type == "Box":
            return Box()
        elif item_type == "SingleItem":
            return SingleItem()
        else:
            raise ValueError("Invalid item type")


# Structural Patterns


## Composite Pattern
class Item(ABC):
    @abstractmethod
    def get_price(self):
        pass


class Box(Item):
    def __init__(self):
        self.items: List[Item] = []

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

    def set_name(self, name):
        self.name = name
        return self

    def get_name(self):
        return self.name

    def set_price(self, price):
        self.price = price
        return self

    def get_price(self):
        return self.price

    def __str__(self) -> str:
        return "Item " + self.name + f" has price of {self.price}"


## Adapter Pattern
class InventoryAdapter:
    def __init__(self, inventory):
        self.inventory = inventory

    def add_item(self, item, quantity):
        self.inventory.add_item(item, quantity)

    def remove_item(self, item, quantity):
        if item in self.inventory.items and self.inventory.items[item] >= quantity:
            self.inventory.items[item] -= quantity
            if self.inventory.items[item] == 0:
                del self.inventory.items[item]
        else:
            raise ValueError("Not enough quantity in inventory")

    def check_item(self, item):
        return self.inventory.items.get(item, 0)


# Behavioural Patterns


## Observer Pattern
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


class Supplier(Observer):
    items_to_suply: Dict[str, Item] = {}

    def __init__(self, items_to_suply):
        self.items_to_suply = items_to_suply

    def supply(self, items):
        for item, obj in items.items():
            del self.items_to_suply[item]
        

    def add_item(self, item):
        self.items_to_suply[item.get_name()] = item
        return self.items_to_suply

    def update(self, message):
        print(f"Supplier: Notified with {message}. Checking Items Left: {str(self.items_to_suply)}.")


class Manager(Observer):
    cash: int = 0

    def __init__(self, budget) -> None:
        self.cash = budget

    def sell(self, amount) -> int:
        return self.cash + amount
    
    def buy(self, amount) -> int:
        return self.cash - amount

    def update(self, message):
        print(f"Manager: Notified with {message}. Checking Cash: {self.cash}.")


class Observable:
    def __init__(self):
        self.observers: List[Observer] = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


## Decorator Pattern
class ItemDecorator(Item):
    def __init__(self, item: Item):
        self.item = item

    def get_price(self):
        return self.item.get_price()


class DiscountedItem(ItemDecorator):
    def __init__(self, item: Item, discount: float):
        super().__init__(item)
        self.discount = discount

    def get_price(self):
        return super().get_price() * (1 - self.discount)

    def __str__(self) -> str:
        return self.item.__str__()


class SpecialOfferItem(ItemDecorator):
    def __init__(self, item: Item, special_offer: float):
        super().__init__(item)
        self.special_offer = special_offer

    def get_price(self):
        return super().get_price() - self.special_offer

    def __str__(self) -> str:
        return self.item.__str__()


# Customer Class
class Customer:
    def __init__(self, inventory_adapter):
        self.inventory_adapter = inventory_adapter

    def purchase_item(self, item, quantity) -> str:
        try:
            self.inventory_adapter.remove_item(item, quantity)
            return f"Purchased {quantity} of {item.get_name()}"
        except ValueError as e:
            return e.__str__()

    def check_availability(self, item) -> int:
        quantity = self.inventory_adapter.check_item(item)
        return quantity


# Main Function
def main():
    inventory = Inventory.get_instance()
    inventory.set_name("First Inventory")

    item_factory = ConcreteItemFactory()

    box = item_factory.create_item("Box")
    box.set_name("Food Box")

    pizza = item_factory.create_item("SingleItem")
    pizza.set_price(100).set_name("Pizza")
    print(pizza)

    bottle = item_factory.create_item("SingleItem")
    bottle.set_price(100).set_name("Bottle of Water")
    print(bottle)

    # Apply a discount to the bottle
    discounted_bottle = DiscountedItem(bottle, 0.1)  # 10% discount
    print(
        f"Discounted {discounted_bottle.item.get_name()} has price of {discounted_bottle.get_price()}"
    )

    box.add_item(pizza)
    box.add_item(discounted_bottle)

    print(box)

    inventory_adapter = InventoryAdapter(inventory)
    customer = Customer(inventory_adapter)

    ######### Supplier and Manager Section is not yet done. #########

    # Buy all the boxes in the inventory
    box_quantity: int = customer.check_availability(box)
    print(customer.purchase_item(box, box_quantity))

    # Check if all are sold
    print(
        f"Availability of {box.get_name()}: {customer.check_availability(box)} in the Inventory {Inventory.get_instance()}"
    )


if __name__ == "__main__":
    main()
