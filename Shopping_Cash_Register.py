#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import display, HTML
from copy import deepcopy

# Invoice Store
daily_invoices = []

# Display Menu
def display_menu():
    display(HTML("<span style='color:Green; font-weight: bold;'>\n --- Shop Cash Counter --- </span>"))
    print("1. Add item by 'add' command")
    print("2. View cart by 'view cart' command")
    print("3. Update item by 'update (item_name)' command")
    print("4. Remove item by 'remove (item_name)' command")
    print("5. Checkout by 'checkout' command")
    print("6. View all invoices by 'invoices' command")
    print("7. Clear invoices by 'clear' command")
    print("8. Exit by 'exit' command")

# Add multiple items
def add_item(items):
    display(HTML("<span style='color: green; font-weight: bold;'>\n --- Add Items (type 'exit' to stop) --- </span>"))
    restricted_cmds = ("view cart", "update", "remove", "checkout", "invoices", "clear")

    while True:
        name = input("Enter item name: ").strip().lower()
        if name == "exit":
            display(HTML("<span style='color : gray; font-weight : bold;'> You exited add mode.</span>"))
            break
        if any(name.startswith(cmd) for cmd in restricted_cmds):
            display(HTML("<span style='color : red; font-weight : bold;'>Command not allowed. Type 'exit' to leave add mode.</span>"))
            continue

        price_input = input("Enter price (₹): ").strip().lower()
        quantity_input = input("Enter quantity: ").strip().lower()
        discount_input = input("Enter discount rate (%): ").strip().lower()

        if any(val == "exit" for val in [price_input, quantity_input, discount_input]):
            display(HTML("<span style='color : gray; font-weight : bold;'> You exited add mode.</span>"))
            break
        if any(val.startswith(cmd) for val in [price_input, quantity_input, discount_input] for cmd in restricted_cmds):
            display(HTML("<span style='color : red; font-weight : bold;'>Command not allowed. Type 'exit' to leave add mode.</span>"))
            continue

        try:
            items.append({
                "name": name.title(),
                "price": float(price_input),
                "quantity": int(quantity_input),
                "discount": float(discount_input)
            })
            print(f"Added {quantity_input} x {name.title()} at ₹{price_input} with {discount_input}% discount.\n")
        except ValueError:
            print("Invalid input. Enter numbers for price, quantity, and discount.\n")

# Update item
def update_item(items, item_name):
    for item in items:
        if item['name'].lower() == item_name.lower():
            print(f"\nFound: {item['name']}. Options: name, price, quantity, discount")
            field = input("Field to update: ").strip().lower()
            if field not in ['name', 'price', 'quantity', 'discount']:
                print("Invalid field.")
                return

            new_value = input(f"New value for {field}: ").strip()
            try:
                if field == 'name':
                    item['name'] = new_value.title()
                elif field == 'price':
                    item['price'] = float(new_value)
                elif field == 'quantity':
                    item['quantity'] = int(new_value)
                elif field == 'discount':
                    item['discount'] = float(new_value)
                print(f"{field.title()} updated successfully.")
            except ValueError:
                print("Invalid input.")
            return
    print(f"Item '{item_name}' not found.")

# Remove item
def remove_item(items, item_name):
    for i, item in enumerate(items):
        if item['name'].lower() == item_name.lower():
            items.pop(i)
            print(f"Removed {item['name']}.")
            return
    print(f"Item '{item_name}' not found.")

# View bill
def view_bill(items):
    display(HTML(f"<span style='color: green; font-weight: bold;'>\n --- Current Bill --- </span>"))
    total = 0
    for item in items:
        item_total = item["price"] * item["quantity"] * (1 - item["discount"] / 100)
        print(f"{item['name']} - ₹{item['price']} x {item['quantity']} - {item['discount']}% = ₹{round(item_total, 2)}")
        total += item_total
    display(HTML(f"<span style='color: blue; font-weight: bold;'>Subtotal: ₹{round(total, 2)}</span>"))

# Checkout
def checkout(items):
    if not items:
        print("No items to checkout.")
        return

    subtotal = sum(item["price"] * item["quantity"] for item in items)
    total_discount = sum((item["discount"] / 100) * item["price"] * item["quantity"] for item in items)

    try:
        gst_rate = float(input("Enter GST rate (%): "))
    except ValueError:
        print("Invalid GST rate.")
        return

    gst = round((gst_rate / 100) * subtotal, 2)
    total = subtotal + gst - total_discount

    display(HTML(f"<span style='color: Orange; font-weight: bold;'>\n --- Final Bill --- </span>"))
    for item in items:
        print(f"{item['name']} - ₹{item['price']} x {item['quantity']} - {item['discount']}%")
    print(f"Subtotal: ₹{round(subtotal, 2)}")
    print(f"Discount: ₹{round(total_discount, 2)}")
    print(f"GST @ {gst_rate}%: ₹{gst}")
    display(HTML(f"<span style='color: purple; font-weight: bold;'>Total: ₹{round(total, 2)}</span>"))
    print("Thank you for shopping!")

    daily_invoices.append({
        "items": deepcopy(items),
        "subtotal": round(subtotal, 2),
        "discount_amount": round(total_discount, 2),
        "gst_rate": gst_rate,
        "gst": gst,
        "total": round(total, 2)
    })
    items.clear()

# View invoices
def view_invoices():
    if not daily_invoices:
        display(HTML("<span style='color : gold ; font-weight : bold ;'>No invoices today.</span>"))
        return

    display(HTML(f"<span style='color: blue; font-weight: bold; font-size: 18px'>\nInvoices today: {len(daily_invoices)}</span>"))
    for idx, invoice in enumerate(daily_invoices, 1):
        display(HTML(f"<span style='color: violet; font-weight: bold;'>\n--- Invoice #{idx} ---</span>"))
        for item in invoice["items"]:
            print(f"{item['name']} - ₹{item['price']} x {item['quantity']} = ₹{round(item['price'] * item['quantity'],2)}")
        print(f"Subtotal: ₹{invoice['subtotal']}")
        print(f"Discount: ₹{invoice['discount_amount']}")
        print(f"GST @ {invoice['gst_rate']}%: ₹{invoice['gst']}")
        display(HTML(f"<span style='color: purple; font-weight: bold;'>Total: ₹{invoice['total']}</span>"))

# Clear invoices
def clear_invoices():
    if input("Clear all invoices? (yes/no): ").lower() in ("yes", "y"):
        daily_invoices.clear()
        print("Invoices cleared.")
    else:
        print("Cancelled.")

# Main Program
def cash_register():
    items = []
    display_menu()

    while True:
        command = input("\nCommand: ").strip().lower()

        if command == 'add':
            add_item(items)
        elif command == 'view cart':
            view_bill(items)
        elif command.startswith('update '):
            update_item(items, command[7:].strip())
        elif command.startswith('remove '):
            remove_item(items, command[7:].strip())
        elif command == 'checkout':
            checkout(items)
        elif command == 'invoices':
            view_invoices()
        elif command == 'clear':
            clear_invoices()
        elif command == 'exit':
            if input("Exit register? (yes/no): ").strip().lower() in ['yes', 'y']:
                display(HTML("<span style='color : pink; font-weight : bold;'> Exiting cash counter. Goodbye!</span>"))
                break
        elif command == '':
            continue
        else:
            display(HTML("<span style = 'font-weight : bold ;'>Unknown command. Try: add / view cart / update [item] / remove [item] / checkout / invoices / clear / exit</span>"))

# Run
cash_register()

