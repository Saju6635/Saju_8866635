from shopping_cart import ShoppingCart
def test_integration1():
    # Create a shopping cart instance
    cart = ShoppingCart()

    # Add two items to the cart: item1 costing $10 and item2 costing $5
    cart.add_to_cart("item1", 10)
    cart.add_to_cart("item2", 5)

    # Calculate the total cost of the items in the cart
    total_cost = cart.calculate_total_cost()

    # Test if the total cost matches the expected value ($15 in this case)
    assert total_cost == 15

def test_integration2():
        # Create a shopping cart instance
        cart = ShoppingCart()

        # Add two items to the cart: item1 costing $10 and item2 costing $5
        cart.add_to_cart("item1", 10)
        cart.add_to_cart("item2", 5)

        # Calculate the total cost of the items in the cart
        total_cost = cart.calculate_total_cost()

        # Test if the total cost matches the expected value ($15 in this case)

        assert total_cost == 1
