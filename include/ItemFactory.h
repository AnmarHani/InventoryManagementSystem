#pragma once
#include <string>
#include <Item.h>

// Factory Pattern for Item Creation
class ItemFactory {
public:
    static Item* createItem(std::string type);
};

