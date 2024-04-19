#pragma once
#include <string>

// Singleton Pattern for Inventory
class Inventory {
private:
    static Inventory* instance;
    Inventory() {}
public:
    static Inventory* getInstance();
    // Other methods for inventory management
};

