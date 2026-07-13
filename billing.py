from db import get_connection

conn = get_connection()
cursor = conn.cursor()


def add_bill():
    print("\n========== ADD BILL ==========")

    patient_id = input("Enter Patient ID: ")

    # Charges
    consultation_fee = float(input("Enter Consultation Fee: "))
    medicine_charge = float(input("Enter Medicine Charge: "))
    test_charge = float(input("Enter Test Charge: "))
    discount = float(input("Enter Discount: "))

    total_amount = consultation_fee + medicine_charge + test_charge - discount

    payment_status = input("Enter Payment Status (Paid/Pending): ")
    bill_date = input("Enter Bill Date (YYYY-MM-DD): ")


    # Check Patient
    cursor.execute(
        "SELECT * FROM patient WHERE patient_id=%s",
        (patient_id,)
    )

    patient = cursor.fetchone()


    if patient:

        cursor.execute(
            """
            INSERT INTO bill
            (patient_id, consultation_fee, medicine_charge, test_charge,
             discount, amount, payment_status, bill_date)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                patient_id,
                consultation_fee,
                medicine_charge,
                test_charge,
                discount,
                total_amount,
                payment_status,
                bill_date
            )
        )

        conn.commit()

        print("Bill generated successfully!")
        print("Total Amount:", total_amount)

    else:
        print("Patient not found.")

def view_bills():
    cursor.execute("SELECT * FROM bill")
    records = cursor.fetchall()

    if records:

        print("\n============== BILL RECORDS ==============")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("Bill ID\tPatient ID\tAmount\t\tBill Date Consultation Fee\tMedicine Charge\tTest Charge\tDiscount\tPayment Status")
        print("-----------------------------------------------------------------------------------------------------------------------------")

        for row in records:
            print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}\t{row[8]}")

        print("-----------------------------------------------------------------------------------------------------------------------------")

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
        print(f"Consultation Fee  : {bill[4]}")
        print(f"Medicine Charge   : {bill[5]}")
        print(f"Test Charge       : {bill[6]}")
        print(f"Discount          : {bill[7]}")
        print(f"Payment Status    : {bill[8]}")

    else:
        print("Bill not found.")


def update_bill():
    bill_id = input("Enter Bill ID: ")

    cursor.execute("SELECT * FROM bill WHERE bill_id=%s", (bill_id,))
    bill = cursor.fetchone()

    if bill:

        amount = input("Enter New Amount: ")
        bill_date = input("Enter New Bill Date (YYYY-MM-DD): ")
        consultation_fee = input("Enter New Consultation Fee: ")
        medicine_charge = input("Enter New Medicine Charge: ")
        test_charge = input("Enter New Test Charge: ")
        discount = input("Enter New Discount: ")
        payment_status = input("Enter New Payment Status: ")

        cursor.execute(
            """UPDATE bill
               SET amount=%s,
                   bill_date=%s
                   consultation_fee=%s,
                   medicine_charge=%s,      
              test_charge=%s,
                discount=%s,
                     payment_status=%s
               WHERE bill_id=%s""",

            (amount, bill_date, consultation_fee, medicine_charge, test_charge, discount, payment_status, bill_id)

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
