from db import get_connection

conn = get_connection()
cursor = conn.cursor()


def add_bill():
    print("\n========== ADD BILL ==========")

    patient_id = input("Enter Patient ID: ")
    amount = float(input("Enter Bill Amount: "))
    bill_date = input("Enter Bill Date (YYYY-MM-DD): ")

    # Check Patient
    cursor.execute("SELECT * FROM patient WHERE patient_id=%s", (patient_id,))
    patient = cursor.fetchone()

    if patient:

        cursor.execute(
            "INSERT INTO bill(patient_id, amount, bill_date) VALUES(%s,%s,%s)",
            (patient_id, amount, bill_date)
        )

        conn.commit()
        print("Bill generated successfully!")

    else:
        print("Patient not found.")


def view_bills():
    cursor.execute("SELECT * FROM bill")
    records = cursor.fetchall()

    if records:

        print("\n============== BILL RECORDS ==============")
        print("------------------------------------------------")
        print("Bill ID\tPatient ID\tAmount\t\tBill Date")
        print("------------------------------------------------")

        for row in records:
            print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}")

        print("------------------------------------------------")

    else:
        print("No bill records found.")


def search_bill():
    bill_id = input("Enter Bill ID: ")

    cursor.execute("SELECT * FROM bill WHERE bill_id=%s", (bill_id,))
    bill = cursor.fetchone()

    if bill:

        print("\n========== BILL DETAILS ==========")
        print(f"Bill ID     : {bill[0]}")
        print(f"Patient ID  : {bill[1]}")
        print(f"Amount      : {bill[2]}")
        print(f"Bill Date   : {bill[3]}")

    else:
        print("Bill not found.")


def update_bill():
    bill_id = input("Enter Bill ID: ")

    cursor.execute("SELECT * FROM bill WHERE bill_id=%s", (bill_id,))
    bill = cursor.fetchone()

    if bill:

        amount = input("Enter New Amount: ")
        bill_date = input("Enter New Bill Date (YYYY-MM-DD): ")

        cursor.execute(
            """UPDATE bill
               SET amount=%s,
                   bill_date=%s
               WHERE bill_id=%s""",
            (amount, bill_date, bill_id)
        )

        conn.commit()
        print("Bill updated successfully!")

    else:
        print("Bill not found.")


def delete_bill():
    bill_id = input("Enter Bill ID: ")

    cursor.execute("SELECT * FROM bill WHERE bill_id=%s", (bill_id,))
    bill = cursor.fetchone()

    if bill:

        confirm = input("Are you sure you want to delete this bill? (Y/N): ")

        if confirm.lower() == "y":

            cursor.execute(
                "DELETE FROM bill WHERE bill_id=%s",
                (bill_id,)
            )

            conn.commit()
            print("Bill deleted successfully!")

        else:
            print("Deletion cancelled.")

    else:
        print("Bill not found.")


def billing_menu():

    while True:

        print("\n====================================")
        print("       BILLING MANAGEMENT")
        print("====================================")
        print("1. Generate Bill")
        print("2. View Bills")
        print("3. Search Bill")
        print("4. Update Bill")
        print("5. Delete Bill")
        print("6. Back to Main Menu")
        print("====================================")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                add_bill()

            case "2":
                view_bills()

            case "3":
                search_bill()

            case "4":
                update_bill()

            case "5":
                delete_bill()

            case "6":
                print("Returning to Main Menu...")
                break

            case _:
                print("Invalid choice! Please try again.")
