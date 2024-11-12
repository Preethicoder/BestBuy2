import pytest

from products import Product


def test_valid_initialization():
    product = Product("Laptop", 1000, 10)
    assert product.name == "Laptop"
    assert product.price == 1000
    assert product.quantity == 10
    assert product.active == True
    assert product.promotion == None


# Test that creating a product with invalid details (empty name, negative price, etc.) raises an exception
def test_create_product_with_invalid_details():
    with pytest.raises(ValueError, match="Name cannot be empty."):
        Product("", 300, 10)
    with pytest.raises(ValueError, match="Price cannot be less than zero"):
        Product("Tablet", -300, 10)
    with pytest.raises(ValueError, match="Quantity cannot be negative."):
        Product("Tablet", 300, -5)


def test_zero_price_and_quantity_are_valid():
    product = Product("Laptop", 0, 0)
    assert product.price == 0
    assert product.quantity == 0
    assert product.active is True
    assert product.promotion == None


def test_product_becomes_inactive_when_quantity_is_zero():
    product = Product("Laptop", 12, 34)
    product.quantity = 0
    assert product.active == False


def test_product_purchase_modifies_quantity_and_returns_correct_output():
    product = Product("Laptop", 12, 34)
    total_price = product.buy(4)
    assert total_price == 48
    assert product.quantity == 30


# Test that buying a larger quantity than exists raises an exception
def test_purchase_larger_quantity_than_exists_raises_exception():
    product = Product("Laptop", 12, 34)
    with pytest.raises(ValueError, match="More quantity than available"):
        product.buy(100)


# Test that setting a negative quantity raises an exception
def test_set_negative_quantity_raises_exception():
    product = Product("Laptop", 12, 34)
    with pytest.raises(ValueError, match="Quantity cannot be negative."):
        product.quantity = -2


# Test that buying with negative quantity
def test_purchase_negative_quantity():
    product = Product("Laptop", 12, 34)
    with pytest.raises(ValueError, match="Quantity cannot be zero"):
        product.buy(-2)
