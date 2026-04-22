import mysql.connector
import getpass

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="userdb"
)

cursor = conn.cursor()


# ---------------- REGISTER ----------------
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(sql, (username, password))
        conn.commit()
        print("Registration successful!")
    except Exception as e:
        print("Error:", e)


# ---------------- LOGIN ----------------
def login():
    
 attempts = 3

 while attempts > 0:
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))

    if cursor.fetchone():
        print("✅ Login successful!")
        return
    else:
        attempts -= 1
        print(f"❌ Attempts left: {attempts}")

def change_password():
    username = input("Enter username:")
    old_password = input("enter old password:")
    
    sql = "SELECT *FROM users WHERE username=%s AND password=%s"
    cursor.execute(sql,(username,old_password))
    result = cursor.fetchone()
    
    if result:
        new_password = input("Enter new password")
        update_sql = "UPDATE users SET password=%s WHERE username=%s"
        cursor.execute(update_sql,(new_password,username))
        conn.commit()
        print("password change successfully")
    else:
        print("invalid username")


def delete_account():
    username = input("Enter the username:")
    password = input("enter the password:")
    
    sql = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(sql,(username,password))
    result = cursor.fetchone()
    
    if result:
        confirm = input("are you sure to delete account(yes/no): ")
        if confirm.lower( ) == "yes":
            delete_sql = "DELETE FROM users WHERE username=%s"
            cursor.execute(delete_sql,(username,))
            conn.commit()
            print("account deleted successfully")
        else:
            print("deletion cancelled")
    else:
        print("invalid username or password")
        
def view_users():
     sql = "SELECT * FROM users"
     cursor.execute(sql)
     result = cursor.fetchall()
     print("\n---all users--")
     for row in result:
         print (row)
        

# ---------------- MENU ----------------
while True:
    print("\n--- MENU ---")
    print("1. Register")
    print("2. Login")
    print("3. change password")
    print("4. deletion")
    print("5. view user")
    print("6.Exit ")

    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice== "3":
        change_password()
    elif choice == "4":
        delete_account()
    elif choice == "5":
        view_users()
    elif choice == "6":
         print("Thank you for using the system!")
         break
    else:
        print("Invalid choice")
