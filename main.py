# ==========================================
# RIWI FILMS - Customer Management System
# Created by Aura
# ==========================================

# Import required modules for system functionality
import clients 
import visualizacion_sala
import compra_de_entradas as compra
import consulta_de_entradas as consulta
import report_data as report
import os


def main():
    # Main loop of the system (runs until user exits)
    while True:

        # Display system title
        visualizacion_sala.title("RIWI FILMS - Customer Management System")

        # Display menu options to the user
        print("""
\033[1;34m 1. \033[0mRegister Customer
\033[1;34m 2. \033[0mShow Customers
\033[1;34m 3. \033[0mView Cinema Room
\033[1;34m 4. \033[0mBuy Tickets
\033[1;34m 5. \033[0mView Sales History
\033[1;34m 6. \033[0mRoom Occupancy Report
              
\033[1;31m 7. \033[0mExit
""")

        # Print separator line
        print("\033[1;34m" + "-"*113 + "\033[0m")

        # Ask user to select an option
        option = input("\n\033[34m >> \033[0mPlease select a option: ")

        print("\n\033[1;34m" + "-"*113 + "\033[0m")

        # Clear the console screen depending on the operating system
        os.system("cls" if os.name == "nt" else "clear")
        
        # Option 1: Register a new client
        if option == "1":
            clients.register_customer(clients.customers)

        # Option 2: Show all registered clients
        elif option == "2":
            clients.show_customers(clients.customers)

        # Option 3: Display cinema room visualization
        elif option == "3":
            visualizacion_sala.view_sales(compra.cinema_room)

        # Option 4: Execute ticket purchase process
        elif option == "4":
            compra.execute_purchase()

        # Option 5: Show sold tickets history
        elif option == "5":
            consulta.show_history(compra.get_history())

        # Option 6: Generate room occupancy report
        elif option == "6":
            report.report(compra.cinema_room)

        # Option 7: Exit the system
        elif option == "7":
            print("\n\033[1;32m" + "-"*113 + "\n" + 
                    f"{'END OF RIWI FILMS - THANK YOU FOR YOUR PURCHASE':^113}" + 
                    "\n" + "-"*113 + "\033[0m")
            break

        # Handle invalid option
        else:
            print("\n\033[1;31m" + "-"*113 + "\n" + 
                    f"{'INVALID OPTION!':^113}" + 
                    "\n" + "-"*113 + "\033[0m")


# Entry point of the program
if __name__ == "__main__":
    main()