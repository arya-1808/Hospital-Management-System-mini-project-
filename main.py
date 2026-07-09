
from login import login_menu
from bill import billing_menu


user = login_menu()
if user:
    while True:
        print("\nWelcome, {}! You are logged in as a {}.".format(user[1], user[3]))
        print("\n ==========Hospital Management System==========")
        print("\n1. Patient Management \n2. Doctor Management \n3. Appointment Management \n4. Billing Management \n5. Medicine Management \n6.Logout")

        ch = input("Enter your choice: ")
        match ch:
            case "1":
                print("Patient Management")
           
            case "2":
                print("Doctor Management")
            
            case "3":
                print
            
            case "4":
                billing_menu()
            
            case "5":
                print("Medicine Management")
            
            case "6":
                print("Logging out...")
                break
            case _:
                print("Invalid choice. Please try again.")