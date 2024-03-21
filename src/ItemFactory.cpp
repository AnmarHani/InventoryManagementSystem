#include "../include/ItemFactory.h"
#include "../include/Item.h"

Item* ItemFactory::createItem(std::string type) {
    if (type == "Book") {
        return new Book();
    } else if (type == "Electronics") {
        return new Electronics();
    }
    // Other item types
    return nullptr;
}

