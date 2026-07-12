from db import get_connection

conn = get_connection()
cursor = conn.cursor()


# ----------------------------
# Book Appointment
# ----------------------------
def book_appointment():
    patient_id = int(input("Enter Patient ID: "))
    doctor_id = int(input("Enter Doctor ID: "))
    appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
    appointment_time = input("Enter Appointment Time (HH:MM:SS): ")
    status = "Booked"

    sql = """
    INSERT INTO appointment
    (patient_id, doctor_id, appointment_date, appointment_time, status)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (patient_id, doctor_id,
                         appointment_date,
                         appointment_time,
                         status))
    conn.commit()

    print("Appointment Booked Successfully.")


# ----------------------------
# View Appointment List
# ----------------------------
def view_appointments():

    cursor.execute("""
    SELECT appointment_id,
           patient_id,
           doctor_id,
           appointment_date,
           appointment_time,
           status
    FROM appointment
    """)

    records = cursor.fetchall()

    if records:
         print("\n========== APPOINTMENT RECORDS ==========")
         print("-------------------------------------------------------------------------------")
         print("ID\tPatient ID\tDoctor ID\tDate\t\tTime\t\tStatus")
         print("-------------------------------------------------------------------------------")
        for row in records:
            print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}\t{row[4]}\t{row[5]}")
    
    else:
        print("No Appointments Found.")


# ----------------------------
# Update Appointment
# ----------------------------
def update_appointment():

    appointment_id = int(input("Enter Appointment ID: "))
    new_date = input("Enter New Date (YYYY-MM-DD): ")
    new_time = input("Enter New Time (HH:MM:SS): ")
    new_status = input("Enter Status: ")

    sql = """
    UPDATE appointment
    SET appointment_date=%s,
        appointment_time=%s,
        status=%s
    WHERE appointment_id=%s
    """

    cursor.execute(sql,
                   (new_date,
                    new_time,
                    new_status,
                    appointment_id))

    conn.commit()

    print("Appointment Updated Successfully.")


# ----------------------------
# Check Doctor Availability
# ----------------------------
def check_doctor_availability():

    doctor_id = int(input("Enter Doctor ID: "))
    date = input("Enter Date (YYYY-MM-DD): ")

    sql = """
    SELECT appointment_time
    FROM appointment
    WHERE doctor_id=%s
    AND appointment_date=%s
    """

    cursor.execute(sql, (doctor_id, date))

    records = cursor.fetchall()

    if records:
        print("Doctor is Busy at:")
        for row in records:
            print(row[0])
    else:
        print("Doctor is Available.")


# ----------------------------
# Cancel Appointment
# ----------------------------
def cancel_appointment():

    appointment_id = int(input("Enter Appointment ID: "))

    sql = """
    UPDATE appointment
    SET status='Cancelled'
    WHERE appointment_id=%s
    """

    cursor.execute(sql, (appointment_id,))

    conn.commit()

    print("Appointment Cancelled Successfully.")


# ----------------------------
# Appointment Menu
# ----------------------------
def appointment_menu():

    while True:

        print("\n===== Appointment Management =====")
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Update Appointment")
        print("4. Check Doctor Availability")
        print("5. Cancel Appointment")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            book_appointment()

        elif choice == "2":
            view_appointments()

        elif choice == "3":
            update_appointment()

        elif choice == "4":
            check_doctor_availability()

        elif choice == "5":
            cancel_appointment()

        elif choice == "6":
            print("Thank You")
            break

        else:
            print("Invalid Choice")

appointment_menu()
