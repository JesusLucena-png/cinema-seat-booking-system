# ==========================================
# Purchase History Module
# Created by Andres
# ==========================================

# Import required functions from other modules
from visualizacion_sala import title


def show_history(history):
    # Print top separator line
    print("\033[1;34m" + "-"*113 + "\033[0m")
    
    # Display section title
    title("PURCHASE HISTORY")
    
    # Print another separator line
    print("\033[1;34m" + "-"*113 + "\033[0m")

    # Iterate through purchase history and display each record
    for i, (fecha, user_id, nombre, asientos) in enumerate(history, 1):
        print(f'''
Purchase: {i}
Date: {fecha}
Name: {nombre}
User ID: {user_id}
Seats: {asientos}
        ''')
        # Print bottom separator line
        print("\033[1;34m" + "-"*113 + "\033[0m")
    