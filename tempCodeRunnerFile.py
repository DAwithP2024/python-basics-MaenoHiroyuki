# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        return sorted(products_list, key=lambda x: x[1])  # Ascending order
    elif sort_order == "desc":
        return sorted(products_list, key=lambda x: x[1], reverse=True)  # Descending order

def display_products(products_list):
    for index, (product, price) in enumerate(products_list, 1):
        print(f"{index}. {product} - ${price}")

def display_categories():
    print("\nAvailable categories:")
    for index, category in enumerate(products, 1):
        print(f"{index}. {category}")
    try:
        category_choice = int(input("Choose a category by entering the number: "))
        if 1 <= category_choice <= len(products):
            return category_choice - 1
        else:
            print("Invalid category choice.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    total_cost = 0
    print("\nCart contents:")
    for product, price, quantity in cart:
        item_total = price * quantity
        total_cost += item_total
        print(f"{product} - ${price} x {quantity} = ${item_total}")
    print(f"Total cost: ${total_cost}")
    return total_cost

def generate_receipt(name, email, cart, total_cost, address):
    print("\nReceipt:")
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for product, price, quantity in cart:
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted upon delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email

def main():
    # Step 1: Get and validate user name
    name = ""
    while not validate_name(name):
        name = input("Enter your full name (first and last name): ")
        print(f"Validated name: {name}")

    # Step 2: Get and validate email
    email = ""
    while not validate_email(email):
        email = input("Enter a valid email address: ")
        print(f"Validated email: {email}")

    # Step 3: Shopping process
    cart = []
    shopping = True

    while shopping:
        # Call display_categories once
        category_choice = display_categories()
        if category_choice is not None:
            category = list(products.keys())[category_choice]
            product_list = products[category]
            display_products(product_list)

            while True:
                action = input("Select an action: 1) Buy product 2) Sort products 3) Go back 4) Finish shopping: ")
                if action == "1":
                    try:
                        product_choice = int(input("Choose a product by entering the number: "))
                        if 1 <= product_choice <= len(product_list):
                            selected_product = product_list[product_choice - 1]
                            quantity = int(input("Enter quantity: "))
                            add_to_cart(cart, selected_product, quantity)
                        else:
                            print("Invalid product choice.")
                    except ValueError:
                        print("Please enter a valid number.")
                elif action == "2":
                    sort_order = input("Enter 'asc' for ascending or 'desc' for descending order: ")
                    sorted_products = display_sorted_products(product_list, sort_order)
                    display_products(sorted_products)
                elif action == "3":
                    break  # Go back to category selection
                elif action == "4":
                    if cart:
                        total_cost = display_cart(cart)
                        address = input("Enter your delivery address: ")
                        generate_receipt(name, email, cart, total_cost, address)
                    else:
                        print("Thank you for using our store. Have a nice day!")
                    shopping = False
                    break
                else:
                    print("Invalid action. Please choose again.")

if __name__ == "__main__":
    main()
