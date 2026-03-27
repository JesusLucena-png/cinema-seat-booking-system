# ==========================================
# VIEW SALES
# Created by Jesus Lucena
# ==========================================

# Import
import visualizacion_sala
import clients
from datetime import datetime  # for purchase date

# Cinema room structure
cinema_room = { 
    "columna_1" : { 
        "fila_A" : [["A1","[]",None],["A2","[-]",None],["A3","[]",None]], 
        "fila_B" : [["B1","[]",None],["B2","[]",None],["B3","[]",None]], 
        "fila_C" : [["C1","[]",None],["C2","[-]",None],["C3","[]",None]], 
        "fila_D" : [["D1","[]",None],["D2","[]",None],["D3","[]",None]]
    }, 
    "columna_2" : {
        "fila_A" : [["A4","[]",None],["A5","[]",None],["A6","[]",None]], 
        "fila_B" : [["B4","[]",None],["B5","[]",None],["B6","[]",None]], 
        "fila_C" : [["C4","[]",None],["C5","[]",None],["C6","[]",None]], 
        "fila_D" : [["D4","[]",None],["D5","[]",None],["D6","[]",None]]
    },  
    "columna_3" : { 
        "fila_A" : [["A7","[]",None],["A8","[]",None],["A9","[]",None]], 
        "fila_B" : [["B7","[]",None],["B8","[]",None],["B9","[]",None]], 
        "fila_C" : [["C7","[]",None],["C8","[]",None],["C9","[]",None]], 
        "fila_D" : [["D7","[]",None],["D8","[]",None],["D9","[-]",None]]
    } 
}

# Validation: field not empty
def validate_not_empty(field_value, field_name):
    if not str(field_value).strip():
        return ("\n\033[1;31m" + "-"*113 + 
                f"{f'\nERROR: {field_name} CANNOT BE EMPTY':^113}" + 
                "\n" + "-"*113 + "\033[0m")
    return None

# Validate user by ID
def validate_user(user_id):
    for client in clients.clientes:
        if client.get("id") == user_id:
            return client
    return None

# Seat states
seat_available = "[]"
seat_occupied = "[X]"
seat_disabled = "[-]"

# Purchase history (tuple storage)
purchase_history = []
# History purchase
def get_history():
    return purchase_history

def execute_purchase():
    active_purchase = True
    while active_purchase:
        visualizacion_sala.view_sales(cinema_room)
        seat_list = []
        seats_to_buy = []
        valid_indices = []
        user = None

        free_seats = 0
        interval = 0
        max_interval = 0
        position = None

        if clients.clientes == []:
            print("\n\033[1;31m" + "-"*113 + "\n" +
                f"{'THERE ARE NO USERS IN THE SYSTEM':^113}" +
                "\n" + "-"*113 + "\033[0m")
            active_purchase = False
            continue

        # ================= GET ALL SEATS =================
        for column_key, columns in cinema_room.items():
            for row_key, rows in columns.items():
                for seat in rows:
                    seat_list.append(seat)
                    if seat[1] == seat_available:
                        free_seats += 1

        seat_list.sort(key=lambda x: x[0])

        # ================= AVAILABLE SEATS =================
        if free_seats != 0:
            print("\n\033[1;32m" + "-"*113 + "\n" + 
                f"{f'THERE ARE {free_seats} AVAILABLE SEATS!':^113}" + 
                "\n" + "-"*113 + "\033[0m")
        else:
            print("\n\033[1;31m" + "-"*113 + "\n" + 
                f"{'NO SEATS AVAILABLE!':^113}" + 
                "\n" + "-"*113 + "\033[0m")
            active_purchase = False
            continue

        # ================= USER INPUT =================
        while True:
            user_id = input("\n\033[34m >> \033[0mEnter User ID: ")

            error = validate_not_empty(user_id, "USER ID")
            if error:
                print(error)
                continue

            user = validate_user(user_id)

            if not user:
                print("\n\033[1;31m" + "-"*113 + "\n" + 
                    f"{'ERROR! USER NOT FOUND':^113}" + 
                    "\n" + "-"*113 + "\033[0m")
                continue

            break

        # ================= MAX CONSECUTIVE =================
        for seat in seat_list:
            if seat[1] == seat_available:
                interval += 1
            else:
                interval = 0

            if max_interval < interval:
                max_interval = interval

        print(f"{'-'*113}")
        print(f"{'\033[1;34m >> \033[0m ONLY CONSECUTIVE SEATS ALLOWED \033[1;34m << \033[0m':^134}")

        # ================= QUANTITY =================
        while True:
            try:
                quantity = int(input("\n\033[34m >> \033[0mEnter number of seats: "))
            except ValueError:
                print("\n\033[1;31m" + "-"*113 + "\n" + 
                    f"{'INVALID INPUT':^113}" + 
                    "\n" + "-"*113 + "\033[0m")
                continue

            error = validate_not_empty(quantity, "SEAT QUANTITY")
            if error:
                print(error)
                continue

            if quantity > free_seats:
                print("\n\033[1;31m" + "-"*113 + "\n" + 
                    f"{'NOT ENOUGH SEATS AVAILABLE':^113}" + 
                    "\n" + "-"*113 + "\033[0m")
                continue

            if quantity > max_interval:
                print("\n\033[1;31m" + "-"*113 + "\n" + 
                    f"{'NO CONSECUTIVE SEATS AVAILABLE FOR THAT QUANTITY':^113}" + 
                    "\n" + "-"*113 + "\033[0m")
                continue

            break

        # ================= VALID INDICES =================
        for seat in seat_list:
            valid_indices.append(seat[0])

        print("\n\033[1;34m" + "-"*113 + "\033[0m")
        while True:
            # ================= INDEX INPUT =================
            seats_to_buy = []
            
            index = input("\n\033[34m >> \033[0mEnter seat index: ").upper()

            error = validate_not_empty(index, "SEAT INDEX")
            if error:
                print(error)
                continue

            if index not in valid_indices:
                print("\n\033[1;31m" + "-"*113 + "\n" + 
                    f"{'INDEX DOES NOT EXIST':^113}" + 
                    "\n" + "-"*113 + "\033[0m")
                continue


            # ================= FIND POSITION =================
            for seat in seat_list:
                if index == seat[0] and seat[1] == seat_available:
                    position = seat_list.index(seat)
                elif index == seat[0] and seat[1] != seat_available:
                    print("\n\033[1;31m" + "-"*113 + "\n" + 
                        f"{'SEAT NOT AVAILABLE':^113}" + 
                        "\n" + "-"*113 + "\033[0m")

            if position is None:
                continue

            end = position + quantity

            print(f"\n{'-'*113}")

            if len(seat_list[position:end]) < quantity:
                print("\n\033[1;31m" + "-"*113 + "\n" + 
                f"{'NOT ENOUGH SEATS AVAILABLE':^113}" + 
                "\n" + "-"*113 + "\033[0m")
                continue


            error_flag = None
            for seat in seat_list[position:end]:
                if seat[1] != seat_available:
                    print(f"\033[1;31mSEAT {seat[0]+seat[1]}\033[0m")
                    error_flag = True
                else:
                    seats_to_buy.append(seat)

            if error_flag:
                print("\033[1;31mSEATS NOT AVAILABLE!\033[0m")
                continue

            break

        # ================= UPDATE SEATS =================
        for column_key, columns in cinema_room.items():
            for row_key, rows in columns.items():
                for seat in rows:
                    if seat in seats_to_buy:
                        seat[1] = seat_occupied
                        seat[2] = False

        # ================= SAVE PURCHASE =================
        purchase_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        purchase = (
            purchase_date,
            user.get("id"),
            user.get("nombre"),
            [seat[0] for seat in seats_to_buy]
        )

        purchase_history.append(purchase)

        # ================= PRINT SUMMARY =================
        visualizacion_sala.title("Purchase History")
        print(f"NAME: {user.get('nombre'):^50}- ID: {user.get('id'):^50}")
        print("\033[1;34m" + "-"*113 + "\033[0m")
        print(f"Seats purchased: {quantity}")
        print("\033[1;34m" + "-"*113 + "\033[0m")
        for i, seat in enumerate(seats_to_buy):
            print(f"{i+1}. {seat[0]}")
        print("\033[1;34m" + "-"*113 + "\033[0m")

        active_purchase = False




if __name__ == "__main__":
    execute_purchase()