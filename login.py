from db import get_connection
conn = get_connection()
cursor = conn.cursor()

def add_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (admin/doctor/patient): ") 
    cursor.execute("INSERT INTO user (username, password, role) VALUES (%s, %s, %s)", (username, password, role))
    
    conn.commit()
    print("User added successfully!")



def login():
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
        return None

def login_menu():
    while True:
        print("\n--- Login Menu ---")
        print("1. Login")
        print("2. Add User")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            user = login()
            if user:
                return user
        elif choice == "2":
            add_user()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    


