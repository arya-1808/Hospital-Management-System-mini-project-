
from login import login_menu
from Patient import patient_menu
from billing import billing_menu
from doctor import doctor_menu
from appointment import appointment_menu
from Pharmacy  import medicine_menu

user = login_menu()
if user:
    while True:
        print("\nWelcome, {}! You are logged in as a {}.".format(user[1], user[3]))
        print("\n ==========Hospital Management System==========")
        print("\n1. Patient Management \n2. Doctor Management \n3. Appointment Management \n4. Billing Management \n5. Medicine Management \n6.Logout")

        ch = input("Enter your choice: ")
        match ch:
            case "1":
                patient_menu()
           
            case "2":
                doctor_menu()
            
            case "3":
                appointment_menu()
            
            case "4":
                billing_menu()
            
            case "5":
                medicine_menu()
            
            case "6":
                print("Logging out...")
                break
            case _:
                print("Invalid choice. Please try again.")