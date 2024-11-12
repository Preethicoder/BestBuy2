class Product:

    def __init__(self, name, price, quantity):

        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be less than zero ")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def set_promotion(self,promotion):
        self.promotion = promotion

    def get_quantity(self):
        """Getter function for quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Sets the quantity and deactivates the product if quantity reaches 0."""
        if quantity < 0:
            raise  ValueError("Quantity should not  be zero")

        self.quantity = self.quantity - quantity

        if quantity == 0:
           self.deactivate()

    def is_active(self):
        """Getter function for active."""
        if self.active:
            return True
        return False

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """MacBook Air M2, Price: 1450, Quantity: 100"""
        detail = f"{self.name}, Price={self.price}, Quantity={self.quantity}"
        if self.promotion:
            detail += f", Promotion={self.promotion.name}"
        print(detail)

    def buy(self,quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be zero")
        if quantity > self.quantity:
            raise ValueError("More quantity than available")
        if self.promotion:
            total_price = self.promotion.apply_promotion(self,quantity)
        else :
            total_price = quantity * self.price
        self.set_quantity(quantity)

        return total_price

class NonStockedProduct(Product):


    def __init__(self, name, price):
         super().__init__(name,price,quantity = 0)


    def show(self):

        detail = f"{self.name}, Price={self.price}"
        if self.promotion:
            detail += f", Promotion={self.promotion.name}"
        print(detail)



class LimitedProduct(Product):


    def __init__(self, name, price, quantity,maximum):
          super().__init__(name,price,quantity)
          if maximum < 0:
              raise ValueError ("Maximum quantity cannot be zero")
          self.maximum = maximum

    def show(self):
        """MacBook Air M2, Price: 1450, Quantity: 100"""
        detail =f"{self.name}, Price={self.price}, Quantity={self.quantity}, Maximum={self.maximum}"
        if self.promotion:
            detail += f", Promotion={self.promotion.name}"
        print(detail)

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

if __name__ == "__main__":
    main()
