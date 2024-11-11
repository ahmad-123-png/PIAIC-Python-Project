"""
import streamlit as st
from auth import AuthSystem
from inventory import Inventory

# Set up authentication system and inventory
auth_system = AuthSystem()
inventory = Inventory()

# Title and Sidebar for Login
st.title("Inventory Management System")
st.sidebar.header("Login")

# User inputs for login
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
login_button = st.sidebar.button("Login")

# Check login credentials
if login_button:
    try:
        user = auth_system.login(username, password)
        st.success(f"Welcome, {user.role}!")
        
        # Admin role - show product management controls
        if user.role == "Admin":
            st.header("Admin Dashboard")

            # Display all products
            st.subheader("All Products")
            products = inventory.view_all_products()
            for product in products:
                st.write(product)

            # Controls for adding new products
            st.subheader("Add a New Product")
            new_name = st.text_input("Product Name")
            new_category = st.text_input("Category")
            new_price = st.number_input("Price", min_value=0.0, step=0.01)
            new_stock = st.number_input("Stock Quantity", min_value=0, step=1)
            if st.button("Add Product"):
                inventory.add_product(new_name, new_category, new_price, new_stock)
                st.success("Product added successfully!")

            # Controls for editing or deleting products
            st.subheader("Edit or Delete a Product")
            edit_id = st.number_input("Enter Product ID to Edit", min_value=1, step=1)
            if st.button("Edit Product"):
                # Implement editing logic here, depending on your ProductManager
                st.info("Product edit feature not fully implemented in this example.")
            if st.button("Delete Product"):
                # Implement delete functionality here
                st.info("Product delete feature not fully implemented in this example.")
                
        # User role - viewing access only
        elif user.role == "User":
            st.header("User Dashboard")
            st.subheader("Available Products")
            products = inventory.view_all_products()
            for product in products:
                st.write(product)

    except ValueError as e:
        st.error(str(e))
        """

import streamlit as st
from auth import AuthSystem
from inventory import Inventory

# Initialize the auth system and inventory
auth_system = AuthSystem()
inventory = Inventory()

# Title and Sidebar for Login
st.title("Inventory Management System")
st.sidebar.header("Login")

# User inputs for login
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
login_button = st.sidebar.button("Login")

# Check login credentials
if login_button:
    try:
        user = auth_system.login(username, password)
        st.success(f"Welcome, {user.role}!")

        if user.role == "Admin":
            st.header("Admin Dashboard")

            # Display all products
            st.subheader("All Products")
            products = inventory.view_all_products()
            for product in products:
                st.write(product)

            # Controls for adding new products
            st.subheader("Add a New Product")
            new_name = st.text_input("Product Name")
            new_category = st.text_input("Category")
            new_price = st.number_input("Price", min_value=0.0, step=0.01)
            new_stock = st.number_input("Stock Quantity", min_value=0, step=1)
            if st.button("Add Product"):
                inventory.add_product(new_name, new_category, new_price, new_stock)
                st.success("Product added successfully!")

        elif user.role == "User":
            st.header("User Dashboard")
            st.subheader("Available Products")
            products = inventory.view_all_products()
            for product in products:
                st.write(product)

    except ValueError as e:
        st.error(str(e))

