from behavioural.observer import Supplier, Manager, Observable
from behavioural.strategy import DiscountPrice, RegularPrice, SpecialOfferPrice

from structural.adapter import InventoryAdapter

from creational.singleton import Inventory
from creational.factory import ConcreteItemFactory

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from structural.adapter import InventoryAdapter
    from structural.composite import Item, SingleItem, Box


# Customer Class
class Customer:
    def __init__(self, inventory_adapter: "InventoryAdapter") -> None:
        """
        This method initializes the Customer class. It takes an inventory adapter as an argument.
        """

        self.inventory_adapter = inventory_adapter

    def purchase_item(self, item: "Item", quantity: int) -> str:
        """
        This method purchases an item from the inventory. It takes an item and a quantity as arguments.
        """

        try:
            self.inventory_adapter.remove_item(item, quantity)
            return f"Purchased {quantity} of {item.get_name()}"
        except ValueError as e:
            return e.__str__()

    def check_availability(self, item: "Item") -> int:
        """
        This method checks the availability of an item in the inventory. It takes an item as an argument.
        """

        quantity = self.inventory_adapter.check_item(item)
        return quantity


# Main Function
def main() -> None:
    inventory: Inventory = Inventory.get_instance()
    inventory.set_name("First Inventory")

    item_factory: ConcreteItemFactory = ConcreteItemFactory()

    box: "Box" = item_factory.create_item("Box")
    box.set_name("Food Box")

    pizza: "SingleItem" = item_factory.create_item("SingleItem", RegularPrice())
    pizza.set_price(100).set_name("Pizza")
    print(pizza)

    bottle: "SingleItem" = item_factory.create_item(
        "SingleItem", DiscountPrice(0.1)
    )  # 10% discount
    bottle.set_price(100).set_name("Bottle of Water")
    print(bottle)

    box.add_item(pizza)
    box.add_item(bottle)
    print(box)

    # Add observers
    supplier: Supplier = Supplier()
    manager: Manager = Manager()

    observable: Observable = Observable()

    observable.attach(supplier)
    observable.attach(manager)

    inventory_adapter: InventoryAdapter = InventoryAdapter(inventory, observable)
    customer: Customer = Customer(inventory_adapter)

    # Add items to inventory
    inventory_adapter.add_item(box, 10)

    # Buy all the boxes in the inventory
    box_quantity: int = customer.check_availability(box)
    print(customer.purchase_item(box, box_quantity))

    # Check if all are sold
    print(
        f"Availability of {box.get_name()}: {customer.check_availability(box)} in the Inventory {Inventory.get_instance()}"
    )


if __name__ == "__main__":
    main()
