#pragma once
#include <string>

// Observer Pattern for Supplier and Manager
class Observer {
public:
    virtual void update(std::string availability) = 0;
};

class Supplier : public Observer {
public:
    void update(std::string availability);
};

class Manager : public Observer {
public:
    void update(std::string availability);
};

