# PIAIC-Python-Project
Inventory Management System

This is a console-based Inventory Management System designed for small businesses, allowing role-based access to manage products in inventory. The system allows Admins to add, edit, and delete products, while Users can only view product details. This project was built using Python with an optional Streamlit interface for a simple GUI.

Project Structure

project-root/
├── auth.py             # Handles user authentication
├── inventory.py        # Manages the inventory operations
├── product.py          # Contains product and product manager classes
├── main.py             # Main script with Streamlit-based interface
├── Dockerfile          # Docker configuration file to containerize the app
└── requirements.txt    # Python dependencies
Features
Core Functionalities
User Authentication:

Role-based access for "Admin" and "User".
Admin can add, edit, and delete products.
User can only view products.
Product Management:

Add, edit, and delete products with attributes such as name, category, price, and stock quantity.
Display all products in the inventory.
Inventory Tracking:

View all products.
Add new products and manage stock.
Streamlit Interface (Optional GUI):

A simple web interface for both Admins and Users.
Accessible on localhost:8501 in the browser.
Prerequisites
Docker installed on your system.
(Optional) Streamlit for the GUI.

Installation and Setup
Follow these instructions to set up the project locally or in a Docker container.

1. Clone the Repository

git clone https://github.com/your-username/inventory-management.git
cd inventory-management
2. Build the Docker Image
Run the following command in the project directory to build the Docker image:


docker build -t inventory_system .

3. Run the Docker Container
To run the container, use the following command. This will map port 8501 on your host machine to the Streamlit app:


docker run -p 8504:8501 inventory_system

4. Access the Application

Open your browser and go to http://localhost:8501. You’ll see a login interface.

5. Login Credentials
The system has two roles:

Admin:
Username: admin
Password: password
Permissions: Can add, edit, and delete products.
User:
Username: user
Password: password
Permissions: Can only view products.

Project Code Walkthrough
auth.py
Handles user authentication:

User class: Stores user data such as username, password, and role.
AuthSystem class: Manages login credentials for predefined users (Admin and User).
product.py
Defines product-related operations:

Product class: Defines a product with attributes like ID, name, category, price, and stock.
ProductManager class: Manages adding, deleting, and retrieving products.
inventory.py
Contains the Inventory class that interfaces with ProductManager:

Provides view_all_products and add_product methods.

main.py
Main entry point for the application:

Uses Streamlit to create a simple web interface.
Admin can add new products and view all products.
User can view products.
Usage Guide
Admin Login:
After logging in, Admins can view a dashboard where they can add new products and view all products.
User Login:
Users will only see a list of available products and cannot add or edit products.

Troubleshooting
Port 8501 is already in use: If you encounter this error, stop any existing container using that port or specify a different port.
Streamlit module not found: Ensure requirements.txt includes streamlit and that the Docker image is rebuilt.
Future Enhancements

Database Integration: Replace in-memory storage with a database.
Enhanced User Roles: Add more roles with varying permissions.
Improved UI/UX: Extend the Streamlit interface to include advanced filtering, search, and sorting options.
Conclusion
This project demonstrates a simple inventory management system with role-based access, providing both a command-line and web interface. It uses Docker for easy deployment and Streamlit for a basic GUI, making it easily extendable.

This README.md file provides all the essential information needed to set up, understand, and run the project. 










