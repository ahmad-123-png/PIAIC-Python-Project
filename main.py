from auth import AuthSystem
from product import Product, ProductManager
from inventory import Inventory

def main():
    auth_system = AuthSystem()
    inventory = Inventory()
    
    try:
        # User authentication
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = auth_system.login(username, password)
        
        print(f"Welcome, {user.role}!")

        # Main application loop to keep the session active
        while True:
            if user.role == "Admin":
                # Admin-specific tasks
                command = input("Enter command (add, edit, delete, view, exit): ")
                
                if command == "add":
                    # Code to add a product
                    pass
                elif command == "edit":
                    # Code to edit a product
                    pass
                elif command == "delete":
                    # Code to delete a product
                    pass
                elif command == "view":
                    # Code to view inventory
                    pass
                elif command == "exit":
                    print("Exiting the system.")
                    break
                else:
                    print("Unknown command, please try again.")
            
            elif user.role == "User":
                # User-specific tasks
                command = input("Enter command (view, exit): ")
                
                if command == "view":
                    # Code to view inventory
                    pass
                elif command == "exit":
                    print("Exiting the system.")
                    break
                else:
                    print("Unknown command, please try again.")
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()


