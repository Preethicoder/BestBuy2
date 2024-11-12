class Product:

    def __init__(self, name, price, quantity):

        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be less than zero ")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True
        self._promotion = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Name cannot be empty.")
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be less than zero")
        self._price = value

    # Getter and Setter for quantity
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = self._quantity - value
        if value == 0:
            self.deactivate()

    # Getter and Setter for promotion
    @property
    def promotion(self):
        return self._promotion

    @promotion.setter
    def promotion(self, value):
        self._promotion = value

    # Active status
    @property
    def is_active(self):
        return self._active







    def activate(self):
        """Activates the product."""
        self._active = True

    def deactivate(self):
        """Deactivates the product."""
        self._active = False

    def __str__(self):
        """MacBook Air M2, Price: 1450, Quantity: 100"""
        detail = f"{self.name}, Price={self.price}, Quantity={self.quantity}"
        if self.promotion:
            detail += f", Promotion={self.promotion.name}"
        return detail

    def buy(self,quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be zero")
        if quantity > self.quantity:
            raise ValueError("More quantity than available")
        if self.promotion:
            total_price = self.promotion.apply_promotion(self,quantity)
        else :
            total_price = quantity * self.price
        self.quantity = quantity

        return total_price

class NonStockedProduct(Product):


    def __init__(self, name, price):
         super().__init__(name,price,quantity = 0)


    def __str__(self):

        detail = f"{self.name}, Price={self.price}"
        if self.promotion:
            detail += f", Promotion={self.promotion.name}"
        return detail



class LimitedProduct(Product):


    def __init__(self, name, price, quantity,maximum):
          super().__init__(name,price,quantity)
          if maximum < 0:
              raise ValueError ("Maximum quantity cannot be zero")
          self.maximum = maximum

    def __str__(self):
        """MacBook Air M2, Price: 1450, Quantity: 100"""
        detail =f"{self.name}, Price={self.price}, Quantity={self.quantity}, Maximum={self.maximum}"
        if self.promotion:
            detail += f", Promotion={self.promotion.name}"
        return detail

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac._active)

    print(str(bose))
    str(mac)

    bose.quantity =1000
    str(bose)

if __name__ == "__main__":
    main()
