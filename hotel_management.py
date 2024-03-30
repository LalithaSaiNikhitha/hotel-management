import mysql.connector

myConnection = ""
cursor = ""
userName = ""
password = ""
roomrent = 0
restaurentbill = 0
gamingbill = 0
totalAmount = 0
cid = ""

def MYSQLconnectionCheck():
    global myConnection
    global userName
    global password

    userName = input("\nEnter MySQL server's username: ")
    password = input("\nEnter MySQL server's password: ")

    myConnection = mysql.connector.connect(host="localhost", user="root", password="root", database="hoteldb")

    if myConnection:
        print("\nCONGRATULATIONS! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED!")
        cursor = myConnection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS hotel")
        cursor.execute("COMMIT")
        cursor.close()
        return myConnection
    else:
        print("ERROR")

def MYSQLconnection():
    global userName
    global password
    global myConnection
    global cid

    myConnection = mysql.connector.connect(host="localhost", user="root", passwd="root", database="hoteldb")

    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION!")
        myConnection.close()

def userEntry():
    global cid

    if myConnection:
        cursor = myConnection.cursor()
        createTable = """CREATE TABLE IF NOT EXISTS C_DETAILS(CID VARCHAR(20), C_NAME VARCHAR(30), C_ADDRESS VARCHAR(30), C_AGE VARCHAR(30), C_COUNTRY VARCHAR(30), P_NO VARCHAR(30), C_EMAIL VARCHAR(30))"""
        cursor.execute(createTable)

        cid = input("Enter Customer Identification Number: ")
        name = input("Enter Customer Name: ")
        address = input("Enter Customer Address: ")
        age = input("Enter Customer Age: ")
        nationality = input("Enter Customer Country: ")
        phoneno = input("Enter Customer Contact Number: ")
        email = input("Enter Customer Email: ")

        sql = "INSERT INTO C_Details VALUES(%s, %s, %s, %s, %s, %s, %s)"
        values = (cid, name, address, age, nationality, phoneno, email)
        cursor.execute(sql, values)
        cursor.execute("COMMIT")

        print("\nNew Customer Entered In The System Successfully!")
        cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION!")

def bookingRecord():
    global cid

    customer = searchCustomer()

    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS BOOKING_RECORD(CID VARCHAR(20), CHECK_IN DATE, CHECK_OUT DATE)"""
            cursor.execute(createTable)

            checkin = input("\nEnter Customer CheckIN Date [YYYY-MM-DD]: ")
            checkout = input("\nEnter Customer CheckOUT Date [YYYY-MM-DD]: ")

            sql = "INSERT INTO BOOKING_RECORD VALUES(%s, %s, %s)"
            values = (cid, checkin, checkout)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")

            print("\nCHECK-IN AND CHECK-OUT ENTRY MADE SUCCESSFULLY!")
            cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION!")

def roomRent():
    global cid
    global roomrent

    customer = searchCustomer()

    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS ROOM_RENT(CID VARCHAR(20), ROOM_CHOICE INT, NO_OF_DAYS INT, ROOMNO INT, ROOMRENT INT)"""
            cursor.execute(createTable)

            print("\n##### We have The Following Rooms For You #####")
            print("1. Ultra Deluxe ----> 3000 Rs.")
            print("2. Deluxe ----> 2000 Rs.")
            print("3. Budget ----> 1000 Rs.")

            roomchoice = int(input("Enter Your Option: "))
            roomno = int(input("Enter Customer Room No: "))
            noofdays = int(input("Enter No. Of Days: "))

            if roomchoice == 1:
                roomrent = noofdays * 3000
                print("\nUltra Royal Room Rent: ", roomrent)
            elif roomchoice == 2:
                roomrent = noofdays * 2000
                print("\nRoyal Room Rent: ", roomrent)
            elif roomchoice == 3:
                roomrent = noofdays * 1000
                print("\nElite Royal Room Rent: ", roomrent)
            else:
                print("Sorry, May Be You Are Giving Me Wrong Input, Please Try Again!!!")
                return

            sql = "INSERT INTO ROOM_RENT VALUES(%s, %s, %s, %s, %s)"
            values = (cid, roomchoice, noofdays, roomno, roomrent)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")

            print("Thank You, Your Room Has Been Booked For:", noofdays, "Days")
            print("Your Total Room Rent is: Rs.", roomrent)
            cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION!")

def Restaurent():
    global cid
    global restaurentbill

    customer = searchCustomer()

    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS RESTAURENT(CID VARCHAR(20), CUISINE VARCHAR(30), QUANTITY VARCHAR(30), BILL VARCHAR(30))"""
            cursor.execute(createTable)

            print("1. Vegetarian Combo -----> 300 Rs.")
            print("2. Non-Vegetarian Combo -----> 500 Rs.")
            print("3. Vegetarian & Non-Vegetarian Combo -----> 750 Rs.")

            choice_dish = int(input("Enter Your Cuisine: "))
            quantity = int(input("Enter Quantity: "))

            if choice_dish == 1:
                print("\nSO YOU HAVE ORDERED: Vegetarian Combo")
                restaurentbill = quantity * 300
            elif choice_dish == 2:
                print("\nSO YOU HAVE ORDERED: Non-Vegetarian Combo")
                restaurentbill = quantity * 500
            elif choice_dish == 3:
                print("\nSO YOU HAVE ORDERED: Vegetarian & Non-Vegetarian Combo")
                restaurentbill = quantity * 750
            else:
                print("Sorry, May Be You Are Giving Me Wrong Input, Please Try Again!!!")
                return

            sql = "INSERT INTO RESTAURENT VALUES(%s, %s, %s, %s)"
            values = (cid, choice_dish, quantity, restaurentbill)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")

            print("Your Total Bill Amount Is: Rs.", restaurentbill)
            print("\n\n**** HOPE YOU WILL ENJOY YOUR MEAL ***\n\n")
            cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION!")

def Gaming():
    global cid
    global gamingbill

    customer = searchCustomer()

    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS GAMING(CID VARCHAR(20), GAMES VARCHAR(30), HOURS VARCHAR(30), GAMING_BILL VARCHAR(30))"""
            cursor.execute(createTable)

            print("""
            1. Table Tennis -----> 150 Rs./HR
            2. Bowling -----> 100 Rs./HR
            3. Snooker -----> 250 Rs./HR
            4. VR World Gaming -----> 400 Rs./HR
            5. Video Games -----> 300 Rs./HR
            6. Swimming Pool Games -----> 350 Rs./HR
            7. Exit
            """)

            game = int(input("Enter What Game You Want To Play: "))
            hour = int(input("Enter No Of Hours You Want To Play: "))
            print("\n\n#################################################")

            if game == 1:
                print("YOU HAVE SELECTED TO PLAY: Table Tennis")
                gamingbill = hour * 150
            elif game == 2:
                print("YOU HAVE SELECTED TO PLAY: Bowling")
                gamingbill = hour * 100
            elif game == 3:
                print("YOU HAVE SELECTED TO PLAY: Snooker")
                gamingbill = hour * 250
            elif game == 4:
                print("YOU HAVE SELECTED TO PLAY: VR World Gaming")
                gamingbill = hour * 400
            elif game == 5:
                print("YOU HAVE SELECTED TO PLAY: Video Games")
                gamingbill = hour * 300
            elif game == 6:
                print("YOU HAVE SELECTED TO PLAY: Swimming Pool Games")
                gamingbill = hour * 350
            else:
                print("Sorry, May Be You Are Giving Me Wrong Input, Please Try Again!!!")
                return

            sql = "INSERT INTO GAMING VALUES(%s, %s, %s, %s)"
            values = (cid, game, hour, gamingbill)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")

            print("Your Total Gaming Bill Is: Rs.", gamingbill)
            print("FOR:", hour, "HOURS", "\n *** WE HOPE YOU WILL ENJOY YOUR GAME ***")
            print("\n\n#################################################")
            cursor.close()
    else:
        print("ERROR ESTABLISHING MYSQL CONNECTION!")

def totalAmount():
    global cid
    global totalAmount
    global roomrent
    global restaurentbill
    global gamingbill

    customer = searchCustomer()

    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS TOTAL(CID VARCHAR(20), C_NAME VARCHAR(30), ROOMRENT INT, RESTAURENTBILL INT, GAMINGBILL INT, TOTALAMOUNT INT)"""
            cursor.execute(createTable)

            name = input("Enter Customer Name: ")
            grandTotal = roomrent + restaurentbill + gamingbill

            values = (cid, name, roomrent, restaurentbill, gamingbill, grandTotal)
            sql = "INSERT INTO TOTAL VALUES(%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, values)
            cursor.execute("COMMIT")

            print("\n **** HOTEL SUNRISE **** CUSTOMER BILLING ****")
            print("\n CUSTOMER NAME: ", name)
            print("\nROOM RENT: Rs.", roomrent)
            print("\nRESTAURENT BILL: Rs.", restaurentbill)
            print("\nGAMING BILL: Rs.", gamingbill)
            print("___________________________________________________")
            print("\nTOTAL AMOUNT: Rs.", grandTotal)
            cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION!")

def searchOldBill():
    global cid
    customer = searchCustomer()

    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            sql = "SELECT * FROM TOTAL WHERE CID= %s"
            cursor.execute(sql, (cid,))
            data = cursor.fetchall()
            if data:
                print(data)
            else:
                print("Record Not Found Try Again!")
            cursor.close()
    else:
        print("\nSomething Went Wrong, Please Try Again!")

def searchCustomer():
    global cid

    if myConnection:
        cursor = myConnection.cursor()
        cid = input("ENTER CUSTOMER ID: ")
        sql = "SELECT * FROM C_DETAILS WHERE CID= %s"
        cursor.execute(sql, (cid,))
        data = cursor.fetchall()

        if data:
            print(data)
            return True
        else:
            print("Record Not Found Try Again!")
            return False

        cursor.close()
    else:
        print("\nSomething Went Wrong, Please Try Again!")

print("""
***************HOTEL MANAGEMENT SYSTEM *************************
""")
myConnection = MYSQLconnectionCheck()

if myConnection:
    MYSQLconnection()
    while True:
        print("""
        1--->Enter Customer Details
        2--->Booking Record
        3--->Calculate Room Rent
        4--->Calculate Restaurant Bill
        5--->Calculate Gaming Bill
        6--->Display Customer Details
        7--->GENERATE TOTAL BILL AMOUNT
        8--->GENERATE OLD BILL
        9--->EXIT
        """)

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            userEntry()
        elif choice == 2:
            bookingRecord()
        elif choice == 3:
            roomRent()
        elif choice == 4:
            Restaurent()
        elif choice == 5:
            Gaming()
        elif choice == 6:
            searchCustomer()
        elif choice == 7:
            totalAmount()
        elif choice == 8:
            searchOldBill()
        elif choice == 9:
            print(" ")
            print("GOODBYE!!")
            break
        else:
            print("Sorry, May Be You Are Giving Me Wrong Input, Please Try Again!!!")
else:
    print("\nERROR ESTABLISHING MYSQL CONNECTION!")
