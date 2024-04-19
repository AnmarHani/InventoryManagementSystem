#include "../include/Inventory.h"

Inventory* Inventory::instance = NULL;

Inventory* Inventory::getInstance() {
    if (instance == NULL) {
        instance = new Inventory();
    }
    return instance;
}

