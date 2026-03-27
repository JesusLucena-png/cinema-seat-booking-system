# ==========================================
# Purchase History Module
# Created by Andres
# ==========================================

# Import required functions from other modules
from visualizacion_sala import title


def show_history(history):
    
    # Display section title
    title("PURCHASE HISTORY")

    # Iterate through purchase history and display each record
    for i, (date, user_id, name, seats) in enumerate(history, 1):
        print(f'''
Purchase: {i}
Date: {date}
Name: {name}
User ID: {user_id}
Seats: {seats}
        ''')
        # Print bottom separator line
        print("\033[1;34m" + "-"*113 + "\033[0m")
    