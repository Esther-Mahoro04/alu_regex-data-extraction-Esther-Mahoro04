# app.py

def login(users):
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in users and users[username] == password:
        print("Login Successful!")
        return True
    else:
        print("Login Failed: Wrong Username or Password")
        return False

def display_dashboard():
    print("\n--- Farmer's Dashboard ---")
    print("1. Watering System Monitor")
    print("2. Smart Crop Monitor")
    print("3. Collaboration Hub")
    print("4. Settings and Support")
    print("5. Exit")
    
    while True:
        choice = input("\nSelect an option (1-5): ")
        if choice == '1':
            print("Watering System Monitor: Daily tasks and reminders.")
        elif choice == '2':
            print("Smart Crop Monitor: Video tutorials and guides.")
        elif choice == '3':
            print("Collaboration Hub: Daily tasks and reminders.")
        elif choice == '4':
            print("Settings and Support: Farmer's profile and customer support.")
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select again.")

def main():
    # Sample user credentials
    users = {
        "farmer": "password123",
        "farmer2":"password456",
    }

    print("Welcome to the Nexus Farmer Application")
    
    if login(users):
        display_dashboard()

if __name__ == "__main__":
    main()