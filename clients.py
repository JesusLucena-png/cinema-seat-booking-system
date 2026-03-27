# ==========================================
# Client Management Module
# Created by Aura
# ==========================================

# Import required functions
from visualizacion_sala import title
from compra_de_entradas import validate_not_empty, validate_user


def register_customer(customers):
    # Display section title
    title("Client Registration")

    # Loop to validate and get a valid customer ID
    while True:
        id_customer = input("\n\033[34m >> \033[0mEnter customer ID: ")

        # Validate that the input is not empty
        error = validate_not_empty(id_customer, "CUSTOMER ID")
        if error:
            print(error)
            continue

        # Validate that the user ID does not already exist
        error = validate_user(id_customer)
        if error:
            print("\n\033[1;31m" + "-"*113 + "\n" +
                f"{'THE CUSTOMER ID ALREADY EXISTS.':^113}" +
                "\n" + "-"*113 + "\033[0m")
            continue

        break

    # Print separator line
    print("\n\033[1;34m" + "-"*113 + "\033[0m")

    # Loop to validate and get a valid customer name
    while True:
        name = input("\n\033[34m >> \033[0mEnter customer name: ")

        # Validate that the name is not empty
        error = validate_not_empty(name, "NAME")
        if error:
            print(error)
            continue

        break
    
    # Create customer as a dictionary
    customer  = {
        "id": id_customer,
        "nombre": name
    }
    
    # Add the new customer to the list
    customers.append(customer)

    # Show success message
    print("\n\033[1;32m" + "-"*113 + "\n" +
    f"{'CUSTOMER CREATED SUCCESSFULLY.':^113}" +
    "\n" + "-"*113 + "\033[0m")


def show_customers(customers):
    # Display section title
    title("Client List")
    
    # Check if there are no clients in the system
    if len(customers) == 0:
        print("\n\033[1;31m" + "-"*113 + "\n" +
                f"{'THERE ARE NO USERS IN THE SYSTEM':^113}" +
                "\n" + "-"*113 + "\033[0m")
        return
    
    # Iterate through clients and display their data
    for c in customers:
        print(f"ID: {c['id']} - Name: {c['nombre']}")
        print("\033[1;34m" + "-"*113 + "\033[0m")
    

# Initial list of clients (example data)
customers  = [
    {'id': '123456', 'nombre': 'Jesus Lucena'},
    {'id': '112233', 'nombre': 'Andres Quintero'}
]