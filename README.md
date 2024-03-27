## The Inventory Management System with Software Best Practices in C++

MEMBERS:
- Anmar Hani (2140004)
- Raef Shah (241165)
- Ziyad Alghamdi (2142017) 
- Samer Awaji (2140332)

It allows Suppliers and Managers to be on track with the inventory, also allows the client to manage items in the Inventory.

### Interfaces:
- Inventory
- ItemFactory
- Item
- Observer

### Class Diagram
![image](https://github.com/AnmarHani/InventoryManagementSystem/assets/76432762/cfb66f8d-add9-466f-a922-66a201bdf4a0)

### Usage of Design Patterns:
#### Creational
- Singleton Pattern (Inventory.h): We use the Singleton pattern for the Inventory class to ensure that there is only one instance of the inventory in the system. This is important because having multiple instances of the inventory can lead to inconsistencies in the inventory data.
- Factory Pattern (ItemFactory.h): The Factory pattern is used to create different types of Item objects. This provides a way to encapsulate the instantiation of Item objects and makes the code more flexible and extensible. For example, if we want to add a new type of item in the future, we just need to modify the ItemFactory class without affecting the client code.
  
#### Structural
- Composite Pattern (Item.h): The Composite pattern is used to represent the box items. A box is an Item that can contain other items (including other boxes). This allows us to treat individual items and compositions of items uniformly.

#### Behavoural
- Decorator Pattern (Item.h): The Decorator pattern is used to add additional features (like discounts or special offers) to the Item objects dynamically. This is more flexible than static inheritance because the features can be added and removed at runtime.
- Observer Pattern (Observer.h): The Observer pattern is used to notify the Supplier and Manager when the availability of an item changes. This is useful because the Supplier and Manager don’t need to check the item availability manually and they will be notified automatically when the availability changes.
