# Hotel Management System

This is a Hotel Management System implemented in Python using MySQL database for storing customer details, booking records, and billing information. It allows users to perform various tasks such as entering customer details, managing booking records, calculating room rent, restaurant bills, gaming bills, and generating total billing amounts.

## Features

- **Enter Customer Details**: Allows users to input customer information such as name, address, age, contact details, etc.
- **Booking Record**: Enables users to record check-in and check-out dates for customers.
- **Calculate Room Rent**: Calculates room rent based on the room choice and number of days of stay.
- **Calculate Restaurant Bill**: Calculates the bill for restaurant orders based on the chosen cuisine and quantity.
- **Calculate Gaming Bill**: Calculates the bill for gaming activities based on the selected game and duration.
- **Display Customer Details**: Displays details of a specific customer based on their ID.
- **Generate Total Bill Amount**: Calculates and displays the total billing amount including room rent, restaurant bill, and gaming bill.
- **Generate Old Bill**: Allows users to search for and display previous billing records based on customer ID.
- **Exit**: Terminates the program.

## Prerequisites

- Python 3.x
- MySQL Server
- `mysql-connector-python` package (Install using `pip install mysql-connector-python`)

## How to Run

1. Make sure you have Python and MySQL server installed on your system.
2. Install the required `mysql-connector-python` package using pip.
3. Create a MySQL database named `hoteldb`.
4. Update the MySQL connection details (username, password) in the code if necessary.
5. Run the Python script `hotel_management_system.py`.
6. Follow the on-screen instructions to use the Hotel Management System.

## Usage

- Upon running the script, follow the prompts to perform various tasks such as entering customer details, managing bookings, and generating bills.
- Input data as per the instructions provided by the system.
- Follow the menu options to navigate through different functionalities.
- Exit the program when done.
