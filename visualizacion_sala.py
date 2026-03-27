# ==========================================
# VIEW SALES
# Created by Jesus Lucena
# ==========================================

# Function to print a centered title with decorative dashes
def title(title_text):

    # If the length is even
    if len(title_text) % 2 == 0:
        dash_count = (111 - len(title_text)) // 2
        print("\033[1;34m" + "-" * dash_count + " " + title_text + "-" * dash_count + "\033[0m")
    
    # If the length is odd
    else:
        dash_count = ((111 - 1) - len(title_text) + 1) // 2
        print("\n\033[1;34m" + "-" * dash_count + " " + title_text + " " + "-" * dash_count + "\033[0m")


# Function to return colored seat representation
def color(seat):

    # Available seat (green)
    if "[]" in seat:
        return f"\033[1;32m{seat}\033[0m"

    # Occupied seat (red)
    elif "[X]" in seat:
        return f"\033[1;31m{seat}\033[0m"

    # Disabled seat (gray)
    elif "[-]" in seat:
        return f"\033[1;30m{seat}\033[0m"


# Function to display the cinema room
def view_sales(room):

    # Display title
    title("Visualización de la Sala ")

    # Table header
    print(f"\n{'-'*113}")
    print(f"|{'Rows':^10}|{'Column 1':^30}|   |{'Column 2':^30}|   |{'Column 3':^30}|")
    print(f"{'-'*113}")

    # Lists to store each row of seats
    row_A = []
    row_B = []
    row_C = []
    row_D = []

    # Iterate through columns and rows
    for column_key, column in room.items():

        for row_key, rows in column.items():
                
            for seat in rows:

                # Assign seats to corresponding row list
                if row_key == "fila_A":
                    row_A.append(f"{seat[0]}{seat[1]}")
                elif row_key == "fila_B":
                    row_B.append(f"{seat[0]}{seat[1]}")
                elif row_key == "fila_C":
                    row_C.append(f"{seat[0]}{seat[1]}")
                elif row_key == "fila_D":
                    row_D.append(f"{seat[0]}{seat[1]}")

    # Group all rows
    data = [row_A, row_B, row_C, row_D]

    # Print each row
    for index in range(0, 4):
        
        # Apply color formatting to each seat
        formatted_row = [color(seat) for seat in data[index]]

        print(f"|{'Row ' + str(index+1):^10}|{formatted_row[0]:^20}|{formatted_row[1]:^20}|{formatted_row[2]:^21}|   |{formatted_row[3]:^20}|{formatted_row[4]:^20}|{formatted_row[5]:^21}|   |{formatted_row[6]:^20}|{formatted_row[7]:^20}|{formatted_row[8]:^21}|")        
        
        # Stop after last row
        if index == 3:
            break
        
        # Row separator
        print(f"-{'-'*10}-{'-'*30}     {'-'*30}     {'-'*30}-")

    # Footer
    print(f"{'-'*113}")
    print(f"""
Available Seats   : \033[1;32m{'FN[]'}\033[0m
Occupied Seats    : \033[1;31m{'FN[X]'}\033[0m
Disabled Seats    : \033[1;30m{'FN[-]'}\033[0m
""")
    print(f"\033[1;34m{'-'*113}\033[0m")
