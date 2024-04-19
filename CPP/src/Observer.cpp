#include "../include/Observer.h"
#include <iostream>

void Supplier::update(std::string availability) {
    std::cout << "Supplier notified. Item is now " << availability << std::endl;
}

void Manager::update(std::string availability) {
    std::cout << "Manager notified. Item is now " << availability << std::endl;
}

