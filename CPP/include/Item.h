#pragma once
#include <string>
#include <vector>

// Decorator Pattern for Item
class Item {
public:
    virtual std::string getDescription() = 0;
    virtual double getPrice() = 0;
};

class Book : public Item {
public:
    std::string getDescription();
    double getPrice();
};

class Electronics : public Item {
public:
    std::string getDescription();
    double getPrice();
};

// Composite Pattern for Box
class Box : public Item {
private:
    std::vector<Item*> items;
public:
    void addItem(Item* item);
    std::string getDescription();
    double getPrice();
};

