# ==========================================
# Report Data
# Created by Andres
# ==========================================

# Import required modules
import compra_de_entradas as compra
from visualizacion_sala import title


def report(cinema_room):
    # Initialize counters for total and occupied seats
    total = 0
    occupied = 0

    # Iterate through the cinema room structure (columns -> rows -> seats)
    for columns in cinema_room.values():
        for rows in columns.values():
            for seat in rows:
                state = seat[1]  # Get seat state

                # Count valid seats (ignore unavailable seats "[-]")
                if state != "[-]":
                    total += 1

                    # Count occupied seats
                    if state == "[X]":
                        occupied += 1

    # Calculate occupancy percentage (avoid division by zero)
    if total > 0:
         percent = (occupied / total) * 100
    else:
        percent = 0

    # Print top separator line
    print("\033[1;34m" + "-"*113 + "\033[0m")
    
    # Display report title
    title("ROOM OCCUPANCY REPORT")
    
    # Print another separator line
    print("\033[1;34m" + "-"*113 + "\033[0m")

    # Display seat statistics
    print(f"Total seats: {total}")
    print(f"Occupied seats: {occupied}")
    print(f"Available seats: {total - occupied}")
    print(f"Percent occupied: {percent:.2f}%")

    # Show customers who have purchased tickets
    if compra.purchase_history:
        title("Customers who bought tickets:")

        # Iterate through purchase history and display client data
        for data_client in compra.purchase_history:
            print(f"Name: {data_client[2]:^50} | ID: {data_client[1]:^50}")
            print("\n\033[1;34m" + "-"*113 + "\033[0m")   

    else:
        # Message when there are no purchases yet
        print("\n\033[1;31m" + "-"*113 + "\n" + 
                    f"{'NO PURCHASES YET!':^113}" + 
                    "\n" + "-"*113 + "\033[0m")