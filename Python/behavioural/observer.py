from abc import ABC, abstractmethod



## Observer Pattern
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


class Supplier(Observer):
    def update(self, message):
        print(f"Supplier: Notified with {message}.")


class Manager(Observer):

    def update(self, message):
        print(f"Manager: Notified with {message}.")


class Observable:
    def __init__(self):
        self.observers = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

