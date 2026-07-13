from db import get_connection
conn = get_connection()
cursor = conn.cursor()

def add_user():
    try:   
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (admin/doctor/patient): ") 
        cursor.execute("INSERT INTO user (username, password, role) VALUES (%s, %s, %s)", (username, password, role))
    
        conn.commit()
        print("User added successfully!")
    
    except Exception as e:
        print(f"Error adding user: {e}")
        conn.rollback()

def change_password():
    try:
        username = input("Enter your username: ")
        cursor.execute("SELECT * FROM user WHERE username=%s", (username,))
        user = cursor.fetchone()
        if user:
            new_password = input("Enter your new password: ")
            cursor.execute("UPDATE user SET password=%s WHERE username=%s", (new_password, username))
            conn.commit()
            print("Password changed successfully!")
        else:
            print("Username not found.")
    except Exception as e:
        print(f"Error changing password: {e}")
        conn.rollback()

def forgot_password():
    username = input("Enter your username: ")
    cursor.execute("SELECT * FROM user WHERE username=%s", (username,))
    user = cursor.fetchone()
    if user:
        try:
            new_password = input("Enter your new password: ")
            cursor.execute("UPDATE user SET password=%s WHERE username=%s", (new_password, username))
            conn.commit()
            print("Password reset successfully!")
        except Exception as e:
            print(f"Error resetting password: {e}")
            conn.rollback()
    else:
        print("Username not found.")



def login():
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (admin/doctor/patient): ")
        cursor.execute("SELECT * FROM user WHERE username=%s AND password=%s AND role=%s", (username, password, role))
        user = cursor.fetchone()
        if user:
            print("Login successful!")
            return user

        else:
            print("Invalid username, password, or role. Please try again.")
            choice = input("Would you like to reset your password? (yes/no): ")
            if choice == "yes":
                forgot_password()
            return None
         
    except Exception as e:
        print(f"Error during login: {e}")
        return None

def login_menu():
    while True:
        print("\n--- Login Menu ---")
        print("1. Login")
        print("2. Add User")
        print("3. Change Password")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            user = login()
            if user:
                return user
        elif choice == "2":
            add_user()
        elif choice == "3":
            change_password()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

    


