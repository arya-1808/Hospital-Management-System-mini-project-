from db import get_connection

conn = get_connection()
cursor = conn.cursor()


def add_patient():
    print("\n========== ADD PATIENT ==========")

    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender(M/F): ")
    

    cursor.execute(
        "INSERT INTO patient(name, age, gender) VALUES(%s,%s,%s)",
        (name, age, gender)
    )

    conn.commit()
    print("Patient added successfully!")


def view_patients():
    cursor.execute("SELECT * FROM patient")
    records = cursor.fetchall()

    if records:
        print("\n========== PATIENT RECORDS ==========")
        print("-----------------------------------------------")
        print("ID\tName\t\tAge\tGender\tBlood Group")
        print("-----------------------------------------------")

        for row in records:
            print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t{row[3]}")

    else:
        print("No patient records found.")


def search_patient():
    pid = input("Enter Patient ID: ")

    cursor.execute("SELECT * FROM patient WHERE patient_id=%s", (pid,))
    patient = cursor.fetchone()

    if patient:
        print("\n========== PATIENT DETAILS ==========")
        print(f"Patient ID   : {patient[0]}")
        print(f"Name         : {patient[1]}")
        print(f"Age          : {patient[2]}")
        print(f"Gender       : {patient[3]}")
    
    else:
        print("Patient not found.")


def update_patient():
    pid = input("Enter Patient ID: ")

    cursor.execute("SELECT * FROM patient WHERE patient_id=%s", (pid,))
    patient = cursor.fetchone()

    if patient:
        name = input("Enter New Name: ")
        age = input("Enter New Age: ")
        gender = input("Enter New Gender: ")
        

        cursor.execute(
            """UPDATE patient
            SET name=%s,
                age=%s,
                gender=%s
                
            WHERE patient_id=%s""",
            (name, age, gender, pid)
        )

        conn.commit()
        print("Patient updated successfully!")
    else:
        print("Patient not found.")


def delete_patient():
    pid = input("Enter Patient ID: ")

    cursor.execute("SELECT * FROM patient WHERE patient_id=%s", (pid,))
    patient = cursor.fetchone()

    if patient:
        confirm = input("Are you sure you want to delete this patient? (Y/N): ")

        if confirm.lower() == "y":
            cursor.execute("DELETE FROM patient WHERE patient_id=%s", (pid,))
            conn.commit()
            print("Patient deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("Patient not found.")


def patient_menu():
    while True:
        print("\n===================================")
        print("      PATIENT MANAGEMENT")
        print("===================================")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Back to Main Menu")
        print("===================================")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                add_patient()
            case "2":
                view_patients()
            case "3":
                search_patient()
            case "4":
                update_patient()
            case "5":
                delete_patient()
            case "6":
                print("Returning to Main Menu...")
                break
            case _:
                print("Invalid choice! Please try again.")
