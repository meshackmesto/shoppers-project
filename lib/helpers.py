# lib/helpers.py

from models.products import Product
from models.customer import Customer
from models.sales import Sales



def exit_program():
    print("Waah! You have money!!")
    exit()



def list_products():
    products = Product.get_all()
    for product in products:
        print(product)

def find_products_by_name():
    name = input("Enter the name of the product: ")
    products = Product.find_by_name(name)
    print(products) if products else print(
        f"No product found with name {name}"
    )

def add_products():
    name = input("Enter products name: ")
    description = input("Enter products description: ")
    price = float(input("Enter products price: "))
    stock = int(input("Enter products stock: "))
    try:
        products = Product.create(name, description, price,stock)
        print(f'Added: {products}')
    except Exception as exc:
        print("Error ocurred adding product:", exc)

def update_products():
    id_ = input("Enter the department's id: ")
    if products := Product.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            products.name = name
            description = input("Enter the description of the product: ")
            products.description = description
            price = input("Enter price of the Product: ")
            products.price = price
            stock = input("Enter stock of the Product: ")
            products.stock = stock

            products.update()
            print(f'Updated: {products}')
        except Exception as exc:
            print("Error updating products: ", exc)
    else:
        print(f'Products {id_} not found')

def delete_products():
    id_ = input("Enter the products id: ")
    if products := Product.find_by_id(id_):
        try:
            products.delete()
            print(f'Deleted: {products}')
        except Exception as exc:
            print("Error deleting products: ", exc)
    else:
        print(f'Products {id_} not found')
def list_of_customers():
    customers = Customer.get_all()
    for customer in customers:
        print(customer)
def view_customer_by_name():
    name = input("Enter the name of the customer: ")
    customers = Customer.find_by_name(name)
    print(customers) if customers else print(
        f"No customer found with name {name}"
    )
def add_customer():
    name = input("Enter customers name: ")
    email = input("Enter customers email: ")
    try:
        customer = Customer.create(name, email)
        print(f'Added: {customer}')
    except Exception as exc:
        print("Error ocurred adding customer:", exc)

def delete_customer():
    id_ = input("Enter the customer's id: ")
    if customer := Customer.find_by_id(id_):
        try:
            customer.delete()
            print(f'Deleted: {customer}')
        except Exception as exc:
            print("Error deleting customer: ", exc)
    else:
        print(f'Customer {id_} not found')

def list_sales():
    sales = Sales.get_all()
    for sale in sales:
        print(sale)