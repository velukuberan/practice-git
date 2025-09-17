# This script simulates a simplified e-commerce inventory management system.
# It allows you to add, update, and view product inventory.
# It also provides functionality to simulate orders and track sales.

import datetime

# Define a Product class to represent items in the inventory
class Product:
    def __init__(self, product_id, name, description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def update_quantity(self, change):
        """Updates the product quantity."""
        self.quantity += change
        if self.quantity < 0:
            self.quantity = 0  # Ensure quantity doesn't go below zero
        return self.quantity

# Inventory management functions
def add_product(inventory):
    """Adds a new product to the inventory."""
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter initial quantity: "))
        new_product = Product(product_id, name, description, price, quantity)
        inventory[product_id] = new_product
        print(f"Product '{name}' added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number for price and quantity.")

def update_product(inventory):
    """Updates an existing product in the inventory."""
    product_id = input("Enter product ID to update: ")
    if product_id in inventory:
        product = inventory[product_id]
        print(f"Updating product: {product}")

        # Allow updating individual fields
        name = input(f"Enter new name (leave blank to keep '{product.name}'): ")
        if name:
            product.name = name
        description = input(f"Enter new description (leave blank to keep current): ")
        if description:
            product.description = description

        try:
            price = input(f"Enter new price (leave blank to keep ${product.price}): ")
            if price:
                product.price = float(price)
            quantity = input(f"Enter new quantity (leave blank to keep {product.quantity}): ")
            if quantity:
                product.quantity = int(quantity)
        except ValueError:
            print("Invalid input. Please enter a valid number for price and quantity.")

        print("Product updated successfully.")
    else:
        print("Product not found.")

def view_inventory(inventory):
    """Displays the current inventory."""
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for product in inventory.values():
            print(product)

def process_order(inventory):
    """Simulates processing an order."""
    order_items = {}  # Dictionary to store items and quantities in the order
    total_cost = 0.0

    while True:
        product_id = input("Enter product ID to order (or 'done' to finish): ")
        if product_id.lower() == 'done':
            break

        if product_id not in inventory:
            print("Product not found.")
            continue

        product = inventory[product_id]
        try:
            quantity = int(input(f"Enter quantity of '{product.name}' to order: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

            if quantity > product.quantity:
                print(f"Not enough stock available.  Only {product.quantity} available.")
                continue

            order_items[product_id] = quantity
            total_cost += product.price * quantity
            print(f"Added {quantity} of '{product.name}' to order.")
        except ValueError:
            print("Invalid quantity. Please enter a valid number.")

    if not order_items:
       print("No items added to the order.  Order cancelled.")
        return

    print("\nOrder Summary:")
    for product_id, quantity in order_items.items():
        product = inventory[product_id]
        print(f"{product.name}: {quantity} x ${product.price} = ${product.price * quantity}")
    print(f"Total Cost: ${total_cost}")

    confirm = input("Confirm order? (yes/no): ")
    if confirm.lower() == 'yes':
        # Update inventory and record sale
        for product_id, quantity in order_items.items():
            inventory[product_id].update_quantity(-quantity)  # Reduce quantity
        record_sale(order_items, total_cost)
        print("Order processed successfully.")
    else:
        print("Order cancelled.")

def record_sale(order_items, total_cost):
    """Records the sale in a sales log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("sales_log.txt", "a") as f:
        f.write(f"Sale at: {timestamp}\n")
        for product_id, quantity in order_items.items():
            product = inventory[product_id]  # Access the inventory from the global scope
            f.write(f"\t{product.name}: {quantity} x ${product.price} = ${product.price * quantity}\n")
        f.write(f"\tTotal Cost: ${total_cost}\n")
        f.write("-" * 30 + "\n")

def view_sales_log():
    """Displays the contents of the sales log."""
    try:
        with open("sales_log.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Sales log is empty.")



# Main program loop
def main():
    inventory = {}  # Dictionary to store products (product_id: Product object)

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. View Inventory")
        print("4. Process Order")
        print("5. View Sales Log")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_product(inventory)
        elif choice == '2':
            update_product(inventory)
        elif choice == '3':
            view_inventory(inventory)
        elif choice == '4':
            process_order(inventory)
        elif choice == '5':
            view_sales_log()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 
