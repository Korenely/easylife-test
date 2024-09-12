
# Easylife test task

This project implements a simple API for managing users and transactions.

## Features

- **User Management**: Create and retrieve users.
- **Transaction Management**: Create transactions for a specific user.
- **Admin Panel**: View, edit, delete users and transactions through an admin panel.
- **Statistics**: View transaction statistics via the admin panel.

## Endpoints

### Add a User
- **POST** `/users/`
    - Add a new user with a username.
    - Request body should contain the username.
    - Returns the ID of the created user.

### Get a User by ID
- **GET** `/users/{user_id}`
    - Retrieve a user by their ID.
    - Returns the user data.

### Get All Users
- **GET** `/users/`
    - Retrieve a list of all users.

### Add a Transaction
- **POST** `/transaction/`
    - Add a new transaction for a specific user.
    - Request body should contain the `transaction_type` and `amount`.
    - Returns the transaction details.

## Admin Panel
- Navigate to `/admin`
    - **User Management**: Admins can view, edit, and delete users.
    - **Transaction Management**: Admins can view, edit, and delete transactions.
    - **Statistics**: Admins can view statistics including the total number of transactions and the total transaction amount.

## Installation

1. Clone the repository.
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```
