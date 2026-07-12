from db import get_connection

conn=get_connection()
cursor=conn.cursor()

#User table
cursor.execute('''CREATE TABLE IF NOT EXISTS user
               (
               user_id INT AUTO_INCREMENT PRIMARY KEY, 
               username VARCHAR(255) NOT NULL, 
               password VARCHAR(255) NOT NULL,
                role VARCHAR(50) NOT NULL)''')
# print("Tables created successfully.")

# patient table
cursor.execute('''CREATE TABLE IF NOT EXISTS patient (
               patient_id INT AUTO_INCREMENT PRIMARY KEY, 
               name VARCHAR(255) NOT NULL, 
               age INT NOT NULL,
               gender VARCHAR(10)
               
               )''')
# print("Patient table created successfully.")

# doctor table
cursor.execute('''CREATE TABLE IF NOT EXISTS doctor (
               doctor_id INT AUTO_INCREMENT PRIMARY KEY, 
               name VARCHAR(255) NOT NULL, 
               specialization VARCHAR(255) NOT NULL,
               experience INT NOT NULL
               )''')
# print("Doctor table created successfully.")

# appointment table
cursor.execute('''CREATE TABLE IF NOT EXISTS appointment (
               appointment_id INT AUTO_INCREMENT PRIMARY KEY, 
               patient_id INT NOT NULL, 
               doctor_id INT NOT NULL, 
               appointment_date DATE NOT NULL,
               appointment_time TIME NOT NULL,
               status VARCHAR(20) NOT NULL,
               FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
               FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id)
               )''')
# print("Appointment table created successfully.")

# bill table
cursor.execute('''CREATE TABLE IF NOT EXISTS bill (
               bill_id INT AUTO_INCREMENT PRIMARY KEY,  
                patient_id INT NOT NULL,
                amount DECIMAL(10, 2) NOT NULL,
                bill_date DATE NOT NULL,
                FOREIGN KEY (patient_id) REFERENCES patient(patient_id)
               )''')
# print("Bill table created successfully.")

# medicine table
cursor.execute('''CREATE TABLE IF NOT EXISTS medicine (
               medicine_id INT AUTO_INCREMENT PRIMARY KEY, 
               name VARCHAR(255) NOT NULL, 
               price DECIMAL(10, 2) NOT NULL,
               stock_quantity INT NOT NULL
               )''')
# print("Medicine table created successfully.")

conn.commit()
