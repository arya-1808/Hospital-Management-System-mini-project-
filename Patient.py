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
        print("ID\tName\t\tAge\tGender")
        print("-----------------------------------------------")

        for row in records:
            print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t{row[3]}")

    else:
        print("No patient records found.")


def search_patient():
    pid = input("Enter Patient ID or Patient Name: ")

    cursor.execute("SELECT * FROM patient WHERE patient_id=%s OR name=%s", (pid, pid))
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
    pid = input("Enter Patient ID : ")

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

def add_visit():
    print("\n========== ADD VISIT ==========")

    p1= input("Enter Patient ID or Name: ")

    # Check if patient exists
    cursor.execute(
        "SELECT * FROM patient WHERE patient_id = %s OR name = %s",
        (p1, p1)
    )
    patient = cursor.fetchone()

    if patient:
        visit_date = input("Enter Visit Date (YYYY-MM-DD): ")
        reason = input("Enter Reason for Visit: ")
        doctor_id = input("Enter Doctor ID : ")  
        cursor.execute(
            "INSERT INTO visitor(patient_id,visit_date, reason, doctor_id) VALUES(%s,%s,%s,%s)",
            (patient[0], visit_date, reason, doctor_id)  
        )

        conn.commit()
        print("Visit added successfully!")
    else:
        print("Patient ID not found.")

def view_visit():
    print("\n========== VIEW VISIT RECORDS ==========")
    print("1. View All Visits")
    print("2. View Visits by Patient ID")

    choice = input("Enter your choice: ")

    if choice == "1":
        cursor.execute("SELECT * FROM visitor")
        records = cursor.fetchall()

        if records:
            print("\nVisit ID\tPatient ID\tVisit Date\tReason\t\tDoctor ID")
            print("-------------------------------------------------------------------------")
            for row in records:
                print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t{row[3]}\t{row[4]}")
        else:
            print("No visit records found.")

   
    elif choice == "2":
        p1 = input("Enter Patient ID or Name: ")

    # Check if patient exists
        cursor.execute(
        "SELECT * FROM patient WHERE patient_id = %s OR name = %s",
        (p1, p1)
        )

        patient = cursor.fetchone()

        if not patient:
            print("Invalid Patient ID! Patient does not exist.")
        else:
        # Fetch visit history
            cursor.execute(
            "SELECT * FROM visitor WHERE patient_id = %s",
            (patient[0],)
            )

            records = cursor.fetchall()

            if records:
                print("\n========== PATIENT VISIT HISTORY ==========")
                count = 1
                for row in records:
                    print(f"\n-------Visit{count}-----------------------------")
                    print(f"Visit ID      : {row[0]}")
                    print(f"Patient ID    : {row[1]}")
                    print(f"Visit Date    : {row[2]}")
                    print(f"Reason        : {row[3]}")
                    print(f"Doctor ID     : {row[4]}")
                    print("------------------------------------------------------")

                    print()
                    count += 1
            else:
                print("No visit records found for this patient.")

    else:
        print("Invalid choice!")



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
        print("6. Add Visit")
        print("7. View Visits")
        print("8. Back to Main Menu")
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
                add_visit()
            case "7":
                view_visit()
            case "8":
                print("Returning to Main Menu...")
                break
            case _:
                print("Invalid choice! Please try again.")
