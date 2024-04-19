#include "../include/Item.h"
#include <iostream>
#include <vector>

std::string Book::getDescription() {
    return "Book";
}

double Book::getPrice() {
    return 10.0;
}

std::string Electronics::getDescription() {
    return "Electronics";
}

double Electronics::getPrice() {
    return 100.0;
}

void Box::addItem(Item* item) {
    items.push_back(item);
}

std::string Box::getDescription() {
    std::string description = "Box contains: ";
    for (auto& item : items) {
        description += item->getDescription() + ", ";
    }
    return description;
}

double Box::getPrice() {
    double total = 0.0;
    for (auto& item : items) {
        total += item->getPrice();
    }
    return total;
}

