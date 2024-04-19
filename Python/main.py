from abc import ABC, abstractmethod
from typing import List, Dict

# Creational Patterns

## Singleton Pattern
class Inventory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Inventory, cls).__new__(cls)
            cls._instance.items = {}
        return cls._instance

    def add_item(self, item, quantity):
        self.items[item] = quantity

## Factory Pattern
class ItemFactory(ABC):
    @abstractmethod
    def create_item(self, item_type):
        pass

class ConcreteItemFactory(ItemFactory):
    def create_item(self, item_type):
        if item_type == 'Box':
            return Box()
        elif item_type == 'SingleItem':
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

    def get_price(self):
        return sum(item.get_price() for item in self.items)
    
    def __str__(self) -> str:
        return "Items in this box are " + self.items.__str__()

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
        return "Item " + self.name + " has price of " + self.price
    
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
    def update(self, subject):
        print(f"Supplier: Received update from {subject}. Replenishing stock.")

class Manager(Observer):
    def update(self, subject):
        print(f"Manager: Received update from {subject}. Checking inventory.")

class Observable:
    def __init__(self):
        self.observers: List[Observer] = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

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

class SpecialOfferItem(ItemDecorator):
    def __init__(self, item: Item, special_offer: float):
        super().__init__(item)
        self.special_offer = special_offer

    def get_price(self):
        return super().get_price() - self.special_offer
    
# Client Class
class Client:
    def __init__(self, inventory_adapter):
        self.inventory_adapter = inventory_adapter

    def purchase_item(self, item, quantity):
        try:
            self.inventory_adapter.remove_item(item, quantity)
            print(f"Purchased {quantity} of {item}")
        except ValueError as e:
            print(e)

    def check_availability(self, item):
        quantity = self.inventory_adapter.check_item(item)
        print(f"Availability of {item}: {quantity}")

# Main Function
def main():
    inventory = Inventory()
    item_factory = ConcreteItemFactory()
    box = item_factory.create_item('Box')
    pizza = item_factory.create_item('SingleItem')
    pizza.set_price(100).set_name("Pizza")

    bottle = item_factory.create_item('SingleItem')
    bottle.set_price(100).set_name("Bottle of Water")

    box.add_item(pizza)
    box.add_item(bottle)


    inventory_adapter = InventoryAdapter(inventory)
    client = Client(inventory_adapter)

    inventory_adapter.add_item(box, 10)
    inventory_adapter.add_item(bottle, 20)

    client.check_availability(box)
    client.purchase_item(box, 5)
    client.check_availability(box)

if __name__ == "__main__":
    main()
