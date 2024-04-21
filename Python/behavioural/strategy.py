from abc import ABC, abstractmethod
from typing import Dict, Optional, Type, Union


## Strategy Pattern
class PricingStrategy(ABC):
    @abstractmethod
    def get_price(self, base_price: float) -> float:
        """
        This method notifies all observers when the subject's state changes. It takes a message as an argument.
        """

        pass


class RegularPrice(PricingStrategy):
    def get_price(self, base_price: float) -> float:
        """
        This method returns the base price as the price. It takes the base price as an argument.
        """

        return base_price


class DiscountPrice(PricingStrategy):
    def __init__(self, discount: float) -> None:
        """
        This method initializes the DiscountPrice class and sets the discount rate. It takes a discount rate as an argument.
        """

        self.discount = discount

    def get_price(self, base_price: float) -> float:
        """
        This method calculates the price after applying the discount. It takes the base price as an argument.
        """

        return base_price * (1 - self.discount)


class SpecialOfferPrice(PricingStrategy):
    def __init__(self, special_offer: float) -> None:
        """
        This method initializes the SpecialOfferPrice class and sets the special offer amount. It takes a special offer amount as an argument.
        """

        self.special_offer = special_offer

    def get_price(self, base_price: float) -> float:
        """
        This method calculates the price after applying the special offer. It takes the base price as an argument.
        """

        return base_price - self.special_offer
