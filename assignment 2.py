### Part 2: Python Code Implementation for UML Diagram

#### 1. EBook Class (EBook.py)
```python
class EBook:
    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    def get_price(self):
        return self.__price

    def set_title(self, new_title):
        self.__title = new_title

    def display_details(self):
        return f"Title: {self.__title}, Author: {self.__author}, Published: {self.__publication_date}, Genre: {self.__genre}, Price: ${self.__price:.2f}"

    def __str__(self):
        return self.display_details()
```

#### 2. Customer Class (Customer.py)
```python
class Customer:
    def __init__(self, name, contact_info, is_loyalty_member=False):
        self.__name = name
        self.__contact_info = contact_info
        self.__is_loyalty_member = is_loyalty_member

    def add_to_cart(self, item):
        pass  # Implementation placeholder

    def remove_from_cart(self, item):
        pass  # Implementation placeholder

    def get_contact_info(self):
        return self.__contact_info

    def __str__(self):
        return f"Customer: {self.__name}, Contact: {self.__contact_info}, Loyalty Member: {self.__is_loyalty_member}"
```

#### 3. Order Class (Order.py)
```python
class Order:
    def __init__(self, order_id, order_date, total_price, customer, cart):
        self.__order_id = order_id
        self.__order_date = order_date
        self.__total_price = total_price
        self.__customer = customer
        self.__cart = cart

    def apply_discount(self, discount_amount):
        self.__total_price -= discount_amount

    def finalize_order(self):
        pass  # Implementation placeholder

    def get_order_summary(self):
        return f"Order ID: {self.__order_id}, Date: {self.__order_date}, Total Price: ${self.__total_price:.2f}"

    def __str__(self):
        return self.get_order_summary()
```

#### 4. ShoppingCart Class (ShoppingCart.py)
```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, ebook):
        self.items.append(ebook)

    def remove_item(self, ebook):
        if ebook in self.items:
            self.items.remove(ebook)

    def calculate_total(self):
        return sum(item.get_price() for item in self.items)

    def display_cart(self):
        return ", ".join(str(item) for item in self.items)

    def __str__(self):
        return self.display_cart()
```

#### 5. Payment Class (Payment.py)
```python
class Payment:
    def __init__(self, payment_id, payment_date, amount, order):
        self.__payment_id = payment_id
        self.__payment_date = payment_date
        self.__amount = amount
        self.__order = order

    def process_payment(self):
        pass  # Implementation placeholder

    def refund_payment(self):
        pass  # Implementation placeholder

    def __str__(self):
        return f"Payment ID: {self.__payment_id}, Date: {self.__payment_date}, Amount: ${self.__amount:.2f}"
```

#### 6. Invoice Class (Invoice.py)
```python
class Invoice:
    def __init__(self, subtotal, vat, total, order):
        self.__subtotal = subtotal
        self.__vat = vat
        self.__total = total
        self.__order = order

    def generate_invoice(self):
        pass  # Implementation placeholder

    def apply_vat(self):
        self.__total = self.__subtotal * (1 + self.__vat / 100)

    def display_invoice(self):
        return f"Invoice Total: ${self.__total:.2f}, Order: {self.__order.get_order_summary()}"

    def __str__(self):
        return self.display_invoice()
```

#### 7. LoyaltyProgram Class (LoyaltyProgram.py)
```python
class LoyaltyProgram(Customer):
    def __init__(self, name, contact_info, loyalty_points, discount_rate):
        super().__init__(name, contact_info, True)
        self.__loyalty_points = loyalty_points
        self.__discount_rate = discount_rate

    def apply_loyalty_discount(self, total):
        return total * (1 - self.__discount_rate / 100)

    def __str__(self):
        return f"Loyalty Member with {self.__loyalty_points} points and {self.__discount_rate}% discount"
```

### Part 3: Test Cases for UML Implementation
Create a `test_cases.py` file to demonstrate:

#### Test Case Structure
```python
import unittest
from EBook import EBook
from Customer import Customer
from Order import Order
from ShoppingCart import ShoppingCart
from Payment import Payment
from Invoice import Invoice
from LoyaltyProgram import LoyaltyProgram

class TestEBookStore(unittest.TestCase):
    def test_ebook_creation(self):
        ebook = EBook("Python Basics", "John Doe", "2024-01-01", "Programming", 29.99)
        self.assertEqual(ebook.get_price(), 29.99)

    def test_add_item_to_cart(self):
        cart = ShoppingCart()
        ebook = EBook("Python Basics", "John Doe", "2024-01-01", "Programming", 29.99)
        cart.add_item(ebook)
        self.assertIn(ebook, cart.items)

    def test_customer_order_creation(self):
        customer = Customer("Alice", "alice@example.com")
        cart = ShoppingCart()
        order = Order(1, "2024-11-04", 100.0, customer, cart)
        self.assertEqual(order.get_order_summary(), "Order ID: 1, Date: 2024-11-04, Total Price: $100.00")

    def test_payment_processing(self):
        customer = Customer("Bob", "bob@example.com")
        cart = ShoppingCart()
        order = Order(1, "2024-11-04", 100.0, customer, cart)
        payment = Payment(101, "2024-11-04", 100.0, order)
        self.assertEqual(str(payment), "Payment ID: 101, Date: 2024-11-04, Amount: $100.00")

    def test_loyalty_discount(self):
        loyalty_customer = LoyaltyProgram("Charlie", "charlie@example.com", 100, 10)
        discounted_total = loyalty_customer.apply_loyalty_discount(200)
        self.assertEqual(discounted_total, 180.0)

if __name__ == "__main__":
    unittest.main()
```

