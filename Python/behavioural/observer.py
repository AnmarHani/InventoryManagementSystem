from abc import ABC, abstractmethod
from typing import Dict, Optional, Type, Union, List, TYPE_CHECKING


## Observer Pattern
class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        """
        This method is called when the subject's state changes. It takes a message as an argument.
        """
        pass


class Supplier(Observer):
    def update(self, message: str) -> None:
        """
        This method is called when the subject's state changes. It takes a message as an argument and prints a notification message.
        """

        print(f"Supplier: Notified with {message}.")


class Manager(Observer):
    def update(self, message: str) -> None:
        """
        This method is called when the subject's state changes. It takes a message as an argument and prints a notification message.
        """

        print(f"Manager: Notified with {message}.")


class Observable:
    def __init__(self) -> None:
        """
        This method initializes the Observable class and creates an empty list of observers.
        """

        self.observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        """
        This method attaches an observer to the subject. It takes an observer as an argument.
        """

        self.observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        This method detaches an observer from the subject. It takes an observer as an argument.
        """

        self.observers.remove(observer)

    def notify(self, message: str) -> None:
        """
        This method notifies all observers when the subject's state changes. It takes a message as an argument.
        """

        for observer in self.observers:
            observer.update(message)
