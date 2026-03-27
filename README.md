# RiwiFilms - Cinema Management System

## Project Overview

**RiwiFilms Cinema Management System** is a Python-based console application designed to manage ticket sales and seat allocation in a multi-cinema environment.

The system replaces manual processes with a structured, automated solution that allows administrators to:
- Control seat availability in real time
- Prevent duplicate seat sales
- Track customer purchases
- Generate occupancy reports

---

## Problem Context

RiwiFilms currently manages ticket sales manually using paper records, which causes:

- No visual control of available seats  
- Risk of duplicate seat sales  
- No real-time occupancy tracking  
- Difficulty identifying customers  
- No structured sales records  

This system solves these issues through automation and structured data handling.

---

## System Architecture

The application follows a **modular structure**, separating responsibilities into different components:


**project**

-  main.py

-  clients.py

-  cinema.py

-  sales.py

-  reports.py

-  visualization.py

-  utils.py


---

## Features

### 1. Client Registration
- Register new clients
- Required data:
  - ID
  - Name

---

### 2. Cinema Visualization
- Display the cinema layout in console
- Seat states:
  - `[ ]` Available
  - `[X]` Occupied
  - `[-]` Disabled

---

### 3. Ticket Purchase
- Assign seats to a client
- Store:
  - Client
  - Seats
  - Purchase date

#### Validations:
- Seat availability
- Consecutive seat rule
- Column restrictions
- Optional automatic seat assignment

---

### 4. Sales Consultation
- View all purchases
- Shows:
  - Client name
  - Seat(s)
  - Purchase date

---

### 5. Occupancy Report
- Total available seats
- Total occupied seats
- Occupancy percentage
- List of clients with purchases

---

## Cinema Configuration

- 3 Columns
- 4 Rows (A, B, C, D)
- 9 seats per row (3 per column)

### Example:


A1[] A2[X] A3[]
A4[] A5[] A6[]
A7[-] A8[] A9[]


---

## Business Rules

### Rule 1: Consecutive Seats
Customers must select **adjacent seats only**.

Invalid:

A1, A3, A4


Valid:

A1, A2, A3, A4


---

### Rule 2: Automatic Assignment
System can assign seats automatically while respecting adjacency rules.

---

### Rule 3: Visualization Before Purchase
The system must display the cinema layout before allowing a purchase.

---

## Technical Requirements

### Functions
- Must receive parameters
- Must return values
- No print-only functions
- Must be reusable

---

### Lambda Usage
At least one `lambda` function is required.

Example:
```python
sorted(seats, key=lambda x: x[0])