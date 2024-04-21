from abc import ABC, abstractmethod

## Strategy Pattern
class PricingStrategy(ABC):
    @abstractmethod
    def get_price(self, base_price):
        pass


class RegularPrice(PricingStrategy):
    def get_price(self, base_price):
        return base_price


class DiscountPrice(PricingStrategy):
    def __init__(self, discount):
        self.discount = discount

    def get_price(self, base_price):
        return base_price * (1 - self.discount)


class SpecialOfferPrice(PricingStrategy):
    def __init__(self, special_offer):
        self.special_offer = special_offer

    def get_price(self, base_price):
        return base_price - self.special_offer
