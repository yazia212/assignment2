# Create EBook Class with attributes of it
class EBook:
    def __init__(self, title, author, publication_date, genre, price):
        # Initialize an eBook with title, author, publication date, genre, and price
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.genre = genre
        self.price = price

    def get_price(self):
        # Returns the price of the eBook
        return self.price

    def display_details(self):
        # Displays details of the eBook in a formatted string
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_date}, Genre: {self.genre}, Price: ${self.price:.2f}"

    def __str__(self):
        return self.display_details()


# Customer Class represents a regular customer without loyalty benefits
class Customer:
    def __init__(self, name, contact_info, is_loyalty_member=False):
         # Initialize a customer with name, contact info, and loyalty membership status
        self.name = name
        self.contact_info = contact_info
        self.is_loyalty_member = is_loyalty_member
        self.cart = ShoppingCart()

    def __str__(self):
        # String representation of the customer
        return f"Customer: {self.name}, Contact: {self.contact_info}, Loyalty Member: {self.is_loyalty_member}"


# ShoppingCart Class holds the eBooks added by the customer
class ShoppingCart:
    def __init__(self):
        self.items = []  # empty List to store eBooks in the cart

    def add_item(self, ebook):
        # Adds an eBook to the cart
        self.items.append(ebook)

    def calculate_total(self):
        # Calculates the total price of items in the cart
        return sum(item.get_price() for item in self.items)

    def display_cart(self):
        # Displays all items in the cart
        return "\n".join(str(item) for item in self.items)

    def __str__(self):
        return self.display_cart()


# LoyaltyProgram Class is an extension of Customer with additional discount benefits it is inheritance
class LoyaltyProgram(Customer):
    def __init__(self, name, contact_info, loyalty_points=0, discount_rate=10):
        super().__init__(name, contact_info, True)  # Inherits from Customer
        self.loyalty_points = loyalty_points
        self.discount_rate = discount_rate

    def apply_loyalty_discount(self, total):
        # Applies discount for loyalty members
        return total * (1 - self.discount_rate / 100)


# Order Class associates a customer with their shopping cart
class Order:
    def __init__(self, order_id, order_date, customer, cart):
        self.order_id = order_id
        self.order_date = order_date
        self.customer = customer  # Aggregation: Order "references" a Customer
        self.cart = cart  # Aggregation: Order "references" a ShoppingCart
        self.total_price = self.cart.calculate_total()  # Total price of the cart items

    def apply_discount(self, discount_amount):
        # Applies a discount to the order
        self.total_price -= discount_amount

    def get_order_summary(self):
        return f"Order ID: {self.order_id}, Date: {self.order_date}, Total Price: ${self.total_price:.2f}"

    def __str__(self):
        return self.get_order_summary()


# Payment Class processes the payment for an order
class Payment:
    def __init__(self, payment_id, payment_date, amount, order):
        self.payment_id = payment_id
        self.payment_date = payment_date
        self.amount = amount
        self.order = order  # Aggregation: Payment "references" an Order

    def process_payment(self):
        # Simulate payment processing
        return f"Payment of ${self.amount:.2f} processed for {self.order}"


# Invoice Class generates an invoice for a completed order
class Invoice:
    def __init__(self, subtotal, vat, order):
        self.subtotal = subtotal
        self.vat = vat
        self.total = self.subtotal * (1 + self.vat / 100)
        self.order = order  # Composition: Invoice "contains" an Order

    def display_invoice(self):
        return f"Invoice Total: ${self.total:.2f}, Order: {self.order.get_order_summary()}"


# Interactive test cases to simulate user interactions
def interactive_tests():
    print("Welcome to the EBook Store! We are here to serve you!\n")

    # Available eBooks for selection
    ebooks = [
        EBook("Python Basics", "John Smith", "2023-01-01", "Programming", 25.99),
        EBook("Advanced Python", "Prof Jane", "2023-05-05", "Programming", 50.00),
        EBook("Data Science Essentials", "Steve Brown", "2024-02-01", "Data Science", 39.99)
    ]

    # Display available books to the user
    print("Available Books:")
    for i, book in enumerate(ebooks, 1):
        print(f"{i}. {book.display_details()}")

    # Adding multiple books to the cart
    cart = ShoppingCart()
    while True:
        choice = int(input("\nEnter the number of the book you want to add to the cart (0 to finish): "))
        if choice == 0:
            break
        if 1 <= choice <= len(ebooks):
            cart.add_item(ebooks[choice - 1])
        else:
            print("Invalid choice. Try again.")

    # Enter customer information
    customer_name = input("\nEnter customer name: ")
    customer_contact = input("Enter customer contact info: ")
    loyalty_status = input("Is this a loyalty member? (yes/no): ").strip().lower() == 'yes'

    # Determine if customer is a regular or loyalty member to apply discount or not
    if loyalty_status:
        customer = LoyaltyProgram(customer_name, customer_contact)
    else:
        customer = Customer(customer_name, customer_contact)
    customer.cart = cart  # Assign cart to customer

    # Display cart and calculate total
    print("\nCart Summary:")
    print(customer.cart.display_cart())
    cart_total = customer.cart.calculate_total()
    print(f"Cart Total: ${cart_total:.2f}")

    # Apply loyalty discount if applicable
    if loyalty_status:
        discount_total = customer.apply_loyalty_discount(cart_total)
        print(f"Total after loyalty discount: ${discount_total:.2f}")
    else:
        discount_total = cart_total

    # Create an order and process payment
    order = Order(1, "2024-11-06", customer, customer.cart)
    payment = Payment(1001, "2024-11-06", discount_total, order)
    print("\nProcessing Payment...")
    print(payment.process_payment())

    # Generate and display invoice to the user
    invoice = Invoice(subtotal=discount_total, vat=5, order=order)
    print("\nInvoice Details:")
    print(invoice.display_invoice())


# Run the interactive tests
interactive_tests()
