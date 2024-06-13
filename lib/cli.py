# lib/cli.py

from helpers import (
    exit_program,
    list_products,
    find_products_by_name,
    add_products,
    update_products,
    delete_products,
    list_of_customers,
    view_customer_by_name,
    add_customer,
    delete_customer,
    list_sales
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_products()
        elif choice == "2":
            find_products_by_name()
        elif choice == "3":
            add_products()
        elif choice == "4":
            update_products()
        elif choice == "5":
            delete_products()
        elif choice == "6":
            list_of_customers()
        elif choice == "7":
            view_customer_by_name()
        elif choice == "8":
            add_customer()
        elif choice == "9":
            delete_customer()
        elif choice == "10":
            list_sales()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1.view all products")
    print("2.find products by name")
    print("3.add products")
    print("4.update products")
    print("5.delete products")
    print("6.view all customers")
    print("7.view customer by name")
    print("8.add new customer")
    print("9.delete customer")
    print("10.view all sales")

if __name__ == "__main__":
    main()
