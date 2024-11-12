import products
import promotion
import store

# Setup initial stock of inventory
# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.NonStockedProduct("Windows License", price=125),
                products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                ]
# Create promotion catalog
second_half_price = promotion.SecondHalfPrice("Second Half price!")
third_one_free = promotion.ThirdOneFree("Third One Free!")
thirty_percent = promotion.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].promotion = second_half_price
product_list[1].promotion = third_one_free
product_list[3].promotion = thirty_percent
# Initialize the store with the product list
best_buy = store.Store(product_list)


def show_products(store):
    products = store.get_all_products()

    print("-------------------------")
    for index, product in enumerate(products, 1):
        print(f"{index}.", end="")
        print(str(product))
    print("---------------------")


def make_order(store):
    products = store.get_all_products()
    ordered_list = []
    show_products(store)
    print("When you want to finish order, enter empty text.")
    while True:

        product_nos = input("Which product # do you want?")
        quantity = input("What amount do you want?")
        if product_nos == "" and quantity == "":
            break
        if int(product_nos) >= 1 and int(product_nos) <= 3:
            print("Product added to list!")
            ordered_list.append((product_list[int(product_nos) - 1], int(quantity)))
        else:
            print("Error adding product")
    total_price = store.order(ordered_list)
    print("*****************")
    print(f"Order made! Total payment:${total_price} ")


def start(store):
    """Main function to start the user interface."""
    while True:
        print("\nWelcome to Best Buy!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                show_products(store)
            elif choice == 2:
                print(f"Total of {store.get_total_quantity()} in a store")
            elif choice == 3:
                make_order(store)
            elif choice == 4:
                print("Thank you for visiting the store. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    start(best_buy)
