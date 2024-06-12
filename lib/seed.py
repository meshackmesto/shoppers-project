# lib/seed.py
from models.customer import Customer
from models.products import Product
from models.sales import Sales

def seed_database():
    # Drop tables if they exist
    Sales.drop_table()
    Customer.drop_table()
    Product.drop_table()

    # Create tables
    Customer.create_table()
    Product.create_table()
    Sales.create_table()

    # Create seed data for Customers
    customer_1 = Customer.create("Alice Johnson", "alice@example.com")
    customer_2 = Customer.create("Bob Smith", "bob@example.com")
    customer_3 = Customer.create("Carol White", "carol@example.com")

    # Create seed data for Products
    product_1 = Product.create("Laptop", "15-inch, 16GB RAM", 1200, 50)
    product_2 = Product.create("Smartphone", "128GB storage, 8GB RAM", 800, 100)
    product_3 = Product.create("Headphones", "Noise-cancelling", 200, 150)
    product_4 = Product.create("Smartwatch", "Heart rate monitor, GPS", 250, 75)
    product_5 = Product.create("Tablet", "10-inch, 64GB storage", 400, 60)
    product_6 = Product.create("Camera", "24MP, 4K video", 900, 40)
    product_7 = Product.create("Printer", "Wireless, All-in-One", 150, 30)
    product_8 = Product.create("Monitor", "27-inch, 4K UHD", 350, 25)
    product_9 = Product.create("Keyboard", "Mechanical, Backlit", 100, 80)
    product_10 = Product.create("Mouse", "Wireless, Ergonomic", 50, 90)
    # Create seed data for Sales
    Sales.create(product_1.id, customer_1.id, 1, "2024-06-01")
    Sales.create(product_2.id, customer_1.id, 2, "2024-06-02")
    Sales.create(product_3.id, customer_2.id, 1, "2024-06-03")
    Sales.create(product_1.id, customer_3.id, 1, "2024-06-04")
    Sales.create(product_2.id, customer_3.id, 1, "2024-06-05")

    print("Seeded database")

seed_database()
