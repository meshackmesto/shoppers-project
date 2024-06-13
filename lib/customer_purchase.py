import tkinter as tk
from tkinter import messagebox
from models.customer import Customer
from models.products import Product
from models.sales import Sales

def create_tables():
    Customer.create_table()
    Product.create_table()
    Sales.create_table()

def populate_products():
    products_listbox.delete(0, tk.END)
    products = Product.get_all()
    for product in products:
        products_listbox.insert(tk.END, f"{product.name} - ${product.price} - ${product.description} - Stock: {product.stock}")

def populate_customers():
    customers_listbox.delete(0, tk.END)
    customers = Customer.get_all()
    for customer in customers:
        customers_listbox.insert(tk.END, f"{customer.name} - {customer.email}")

def handle_purchase():
    name = name_entry.get()
    email = email_entry.get()
    product_name = product_name_entry.get()

    # Validate inputs
    if not name or not email or not product_name:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    # Check if product exists
    product = Product.find_by_name(product_name)
    if not product:
        messagebox.showerror("Product Error", "Product not found.")
        return

    # Check if the product is in stock
    if product.stock <= 0:
        messagebox.showerror("Stock Error", "Product is out of stock.")
        return

    # Create customer if doesn't exist
    customer = Customer.find_by_name(name)
    if not customer:
        customer = Customer.create(name, email)
    else:
        # Update email if necessary
        if customer.email != email:
            customer.email = email
            customer.update()

    # Create sale
    Sales.create(product.id, customer.id, 1, "2024-06-10")

    # Update product stock
    product.stock -= 1
    product.update()

    # Refresh product and customer lists
    populate_products()
    populate_customers()

    messagebox.showinfo("Success", f"Product {product_name} purchased successfully!")

# Create main window
root = tk.Tk()
root.title("Customer Purchase")

# Name entry of the customer
tk.Label(root, text="Name").grid(row=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Email of the customer
tk.Label(root, text="Email").grid(row=1)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1)

# Product name you enter
tk.Label(root, text="Product Name").grid(row=2)
product_name_entry = tk.Entry(root)
product_name_entry.grid(row=2, column=1)

# Submit button
submit_button = tk.Button(root, text="Purchase", command=handle_purchase)
submit_button.grid(row=3, columnspan=2)

# Products list
tk.Label(root, text="Available Products").grid(row=4, columnspan=2)
products_listbox = tk.Listbox(root, width=50)
products_listbox.grid(row=5, columnspan=2)

# Customers list
tk.Label(root, text="Customers").grid(row=6, columnspan=2)
customers_listbox = tk.Listbox(root, width=50)
customers_listbox.grid(row=7, columnspan=2)

# Populate products and customers list
populate_products()
populate_customers()

# Run the Tkinter event loop
root.mainloop()
