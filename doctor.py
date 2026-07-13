from db import get_connection

conn = get_connection()
cursor = conn.cursor()


def add_doctor():
    print("\n========== ADD DOCTOR ==========")

    name = input("Enter Doctor Name: ")
    specialization = input("Enter Specialization: ")
    experience = int(input("Enter Experience (Years): "))

    cursor.execute(
        "INSERT INTO doctor(name, specialization, experience) VALUES(%s,%s,%s)",
        (name, specialization, experience)
    )

    conn.commit()
    print("\nDoctor added successfully!")


def view_doctors():
    cursor.execute("SELECT * FROM doctor")
    records = cursor.fetchall()

    if records:
        print("\n========== DOCTOR RECORDS ==========")
        print("-------------------------------------------------------------")
        print("ID\tName\t\tSpecialization\t\tExperience")
        print("-------------------------------------------------------------")

        for row in records:
            print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]} Years")

        print("-------------------------------------------------------------")

    else:
        print("\nNo doctor records found.")


def search_doctor():
    did = input("\nEnter Doctor ID or Doctor Name: ")

    cursor.execute("SELECT * FROM doctor WHERE doctor_id=%s OR name=%s", (did, did))
    doctor = cursor.fetchone()

    if doctor:
        print("\n========== DOCTOR DETAILS ==========")
        print(f"Doctor ID       : {doctor[0]}")
        print(f"Doctor Name     : {doctor[1]}")
        print(f"Specialization  : {doctor[2]}")
        print(f"Experience      : {doctor[3]} Years")
    else:
        print("\nDoctor not found.")


def update_doctor():
    did = input("\nEnter Doctor ID: ")

    cursor.execute("SELECT * FROM doctor WHERE doctor_id=%s", (did,))
    doctor = cursor.fetchone()

    if doctor:
        name = input("Enter New Doctor Name: ")
        specialization = input("Enter New Specialization: ")
        experience = int(input("Enter New Experience: "))

        cursor.execute(
            """UPDATE doctor
               SET name=%s,
                   specialization=%s,
                   experience=%s
               WHERE doctor_id=%s""",
            (name, specialization, experience, did)
        )

        conn.commit()
        print("\nDoctor details updated successfully!")

    else:
        print("\nDoctor not found.")


def delete_doctor():
    did = input("\nEnter Doctor ID : ")

    cursor.execute("SELECT * FROM doctor WHERE doctor_id=%s", (did,))
    doctor = cursor.fetchone()

    if doctor:
        confirm = input("Are you sure you want to delete this doctor? (Y/N): ")

        if confirm.lower() == "y":
            cursor.execute(
                "DELETE FROM doctor WHERE doctor_id=%s",
                (did,)
            )

            conn.commit()
            print("\nDoctor deleted successfully!")

        else:
            print("\nDeletion cancelled.")

    else:
        print("\nDoctor not found.")
def doctor_dashboard():
    print("\n========== DOCTOR DASHBOARD ==========")

    did = input("Enter Doctor ID or Name: ")

    cursor.execute(
        "SELECT * FROM doctor WHERE doctor_id=%s OR name=%s",
        (did,did)
    )

    doctor = cursor.fetchone()

    if doctor:
        print("\n========== DOCTOR DETAILS ==========")
        print("\nDoctor ID       :", doctor[0])
        print("Doctor Name     :", doctor[1])
        print("Specialization  :", doctor[2])
        print("Experience      :", doctor[3], "Years")

        print("\n===================================")
        cursor.execute(
            "SELECT * FROM visitor WHERE doctor_id=%s",
            (doctor[0],)
        )
        visits = cursor.fetchall()
        if visits:
            print("\n========== VISITORS RECORDS ==========")
            for visit in visits:
                print(f"Visit ID      : {visit[0]}")
                print(f"Patient ID    : {visit[1]}")
                print(f"Visit Date    : {visit[2]}")
                print(f"Reason        : {visit[3]}")
                print("------------------------------------------------------")
        else:
            print("\nNo visit records found for this doctor.")

    else:
        print("\nDoctor not found!")


def doctor_menu():
    while True:
        print("\n===================================")
        print("      DOCTOR MANAGEMENT")
        print("===================================")
        print("1. Add Doctor")
        print("2. View All Doctors")
        print("3. Search Doctor")
        print("4. Update Doctor")
        print("5. Delete Doctor")
        print("6. Doctor Dashboard")
        print("7. Return to Main Menu")
        print("===================================")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                add_doctor()

            case "2":
                view_doctors()

            case "3":
                search_doctor()

            case "4":
                update_doctor()

            case "5":
                delete_doctor()

            case "6":
                doctor_dashboard()

            case 7:
                print("\nReturning to Main Menu...")
                break

            case _:
                print("\nInvalid choice! Please try again.")
