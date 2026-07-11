from db import get_connection

conn = get_connection()
cursor = conn.cursor()


def add_medicine():
    print("\n========== ADD MEDICINE ==========")

    name = input("Enter Medicine Name: ")
    price = float(input("Enter Price: "))
    stock = int(input("Enter Stock Quantity: "))

    cursor.execute(
        "INSERT INTO medicine(name, price, stock_quantity) VALUES(%s,%s,%s)",
        (name, price, stock)
    )

    conn.commit()
    print("Medicine added successfully!")


def view_medicines():
    cursor.execute("SELECT * FROM medicine")
    records = cursor.fetchall()

    if records:
        print("\n========== MEDICINE RECORDS ==========")
        print("------------------------------------------------------")
        print("ID\tName\t\tPrice\t\tStock")
        print("------------------------------------------------------")

        for row in records:
            print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}")

    else:
        print("No medicine records found.")


def search_medicine():
    mid = input("Enter Medicine ID: ")

    cursor.execute("SELECT * FROM medicine WHERE medicine_id=%s", (mid,))
    medicine = cursor.fetchone()

    if medicine:
        print("\n========== MEDICINE DETAILS ==========")
        print(f"Medicine ID : {medicine[0]}")
        print(f"Name        : {medicine[1]}")
        print(f"Price       : {medicine[2]}")
        print(f"Stock       : {medicine[3]}")
    else:
        print("Medicine not found.")


def update_medicine():
    mid = input("Enter Medicine ID: ")

    cursor.execute("SELECT * FROM medicine WHERE medicine_id=%s", (mid,))
    medicine = cursor.fetchone()

    if medicine:
        name = input("Enter New Medicine Name: ")
        price = float(input("Enter New Price: "))
        stock = int(input("Enter New Stock Quantity: "))

        cursor.execute(
            """UPDATE medicine
               SET name=%s,
                   price=%s,
                   stock_quantity=%s
               WHERE medicine_id=%s""",
            (name, price, stock, mid)
        )

        conn.commit()
        print("Medicine updated successfully!")

    else:
        print("Medicine not found.")


def delete_medicine():
    mid = input("Enter Medicine ID: ")

    cursor.execute("SELECT * FROM medicine WHERE medicine_id=%s", (mid,))
    medicine = cursor.fetchone()

    if medicine:
        confirm = input("Are you sure you want to delete this medicine? (Y/N): ")

        if confirm.lower() == "y":
            cursor.execute("DELETE FROM medicine WHERE medicine_id=%s", (mid,))
            conn.commit()
            print("Medicine deleted successfully!")
        else:
            print("Deletion cancelled.")

    else:
        print("Medicine not found.")


def medicine_menu():
    while True:
        print("\n===================================")
        print("   PHARMACY & MEDICINE MANAGEMENT")
        print("===================================")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Search Medicine")
        print("4. Update Medicine")
        print("5. Delete Medicine")
        print("6. Back to Main Menu")
        print("===================================")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                add_medicine()
            case "2":
                view_medicines()
            case "3":
                search_medicine()
            case "4":
                update_medicine()
            case "5":
                delete_medicine()
            case "6":
                print("Returning to Main Menu...")
                break
            case _:
                print("Invalid choice! Please try again.")


medicine_menu()