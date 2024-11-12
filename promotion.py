from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """Applies a percentage discount on total price"""
        total_price = product.price * quantity
        print("pp", total_price)
        discount = total_price * (self.percent / 100)
        print("dd", discount)
        return total_price - discount


class SecondHalfPrice(Promotion):
    """Promotion gives second one half price"""

    def apply_promotion(self, product, quantity):
        """Applies discount: second item at half price for even quantities."""
        pairs = quantity // 2
        single_items = quantity % 2
        # Half price for half of the pairs; full price for others
        return (pairs * 1.5 + single_items) * product.price


class ThirdOneFree(Promotion):
    """Promotion that gives third one free"""

    def apply_promotion(self, product, quantity):
        """Applies discount: third item free."""
        full_price_groups = quantity // 3 * 2  # 3 items but pay for only 2
        remainder = quantity % 3
        return (full_price_groups + remainder) * product.price
