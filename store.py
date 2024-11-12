import products
class Store:

    def __init__(self, product_list = None):
        # Initialize store with an optional list of products
        if product_list is None:
            product_list = []
        self.product = product_list

    def add_product(self, product):
        """Adds a new product to the store."""
        self.product.append(product)

    def __contains__(self, item):
        return item in self.product

    def remove_product(self, product):
        """Removes a product from store."""
        self.product.remove(product)

    def get_total_quantity(self):
        """Returns how many items are in the store in total."""
        return sum(product.quantity  for product in self.product)

    def get_all_products(self):
        """Returns all products in the store that are active."""
        return [product_item for product_item in self.product if product_item.is_active]

    def order(self, shopping_list):
        total_price = 0
        for product,quantity in shopping_list:
            total_price += product.buy(quantity)
        return  total_price


def main() :
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products_list = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products_list[0], 1), (products_list[1], 2)]))

if __name__ == "__main__":
    main()