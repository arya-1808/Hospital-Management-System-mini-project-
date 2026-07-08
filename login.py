from db import get_connection
conn = get_connection()
cursor = conn.cursor()

user = input("Enter your username: ")
pas = input("Enter your password: ")
role = input("Enter your role (admin/doctor/patient): ")
 
query = "SELECT * FROM user WHERE username = %s AND password = %s AND role = %s"
cursor.execute(query, (user, pas, role))

result = cursor.fetchone()

if result:
    print("Login successful!")
    if role == "admin":
        print("Welcome, Admin!")
        # Admin-specific functionality can be added here
    elif role == "doctor":
        print("Welcome, Doctor!")
        # Doctor-specific functionality can be added here
    elif role == "patient":
        print("Welcome, Patient!")
        # Patient-specific functionality can be added here
    else:
        print("Invalid role specified.")
else:
    print("Invalid username, password, or role. Please try again.")

