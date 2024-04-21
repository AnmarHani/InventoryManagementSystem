from abc import ABC, abstractmethod

## Singleton Pattern
class Inventory:
    _instance = None
    items = {}
    name = ""

    @staticmethod
    def get_instance():
        if Inventory._instance is None:
            return Inventory()
        return Inventory._instance

    @staticmethod
    def add_item(item, quantity):
        Inventory.items[item] = quantity

    @staticmethod
    def set_name(name):
        Inventory.name = name
        return Inventory.name

    @staticmethod
    def __str__():
        return f"Inventory {Inventory.name} has: {Inventory.items}"
