#include "Inventory.h"
#include "ItemFactory.h"
#include "Item.h"
#include "Observer.h"
#include <iostream>

int main() {
    // Create inventory
    Inventory* inventory = Inventory::getInstance();

    // Create items
    Item* book = ItemFactory::createItem("Book");
    Item* electronics = ItemFactory::createItem("Electronics");

    // Create box and add items
    Box* box = new Box();
    box->addItem(book);
    box->addItem(electronics);

    // Print box description and price
    std::cout << box->getDescription() << std::endl;
    std::cout << "Total price: " << box->getPrice() << std::endl;

    // Create observers
    Supplier* supplier = new Supplier();
    Manager* manager = new Manager();

    // Update observers
    supplier->update("available");
    manager->update("out of stock");

    return 0;
}

