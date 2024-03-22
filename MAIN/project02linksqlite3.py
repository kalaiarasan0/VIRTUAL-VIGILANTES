import os
import re
import sqlite3
from datetime import datetime
import pandas as pd

# Establish connection to SQLite database
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

# Create contacts table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT NOT NULL
                  )''')
conn.commit()

contacts=[]

def generate_id():
    """Generates an ID based on the current date and time."""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S%f")  # Format: YYYYMMDDHHMMSSmicroseconds
    return timestamp


def validate_phone_number(phone):
    """Validates the phone number."""
    if not phone:
        raise ValueError("Phone number cannot be empty!")
    elif not phone.isdigit():
        raise ValueError("Mobile number can only contain digits!")
    elif len(phone) != 10:  # Check for 10 digits
        raise ValueError("Mobile number must be 10 digits long!")
    return phone.strip()

def validate_email(email):
    """Validates the email address."""
    if not email:
        raise ValueError("Email cannot be empty!")
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email format!")
    return email.strip()

def validate_phone_number_edit(new_phone):
    """Validates the phone number."""
    if not new_phone:
        return new_phone  # Allow empty phone number
    elif not new_phone.isdigit():
        raise ValueError("Mobile number can only contain digits!")
    return new_phone.strip()


def validate_email_edit(new_email):
    """Validates the email address."""
    if not new_email:
        return new_email  # Allow empty email
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
        raise ValueError("Invalid email format!")
    return new_email.strip()


def create_contact():
    """Prompts user for contact details and inserts into database."""
    name = input("Enter contact name: ").strip()
    while True:
        phone = input("Enter mobile number: ").strip()
        try:
            phone = validate_phone_number(phone)
            cursor.execute('SELECT * FROM contacts WHERE phone = ?', (phone,))
            if cursor.fetchone():
                print("Mobile number already exists!")
                continue
            break
        except ValueError as e:
            print(str(e))
    while True:
        email = input("Enter Email: ").strip()
        try:
            email = validate_email(email)
            cursor.execute('SELECT * FROM contacts WHERE email = ?', (email,))
            if cursor.fetchone():
                print("Email ID already exists!")
                continue
            break
        except ValueError as e:
            print(str(e)) 

    id = generate_id()

    cursor.execute('INSERT INTO contacts (id, name, phone, email) VALUES (?, ?, ?, ?)', (id, name, phone, email))
    conn.commit()
    print("Contact added successfully!")
    return {"id": id, "name": name, "phone": phone, "email": email}

def edit_contact(query):
    """Edits an existing contact based on name or ID."""
    # Fetch contact from database based on query
    cursor.execute('SELECT * FROM contacts WHERE name=? OR id=?', (query, query))
    match = cursor.fetchone()

    if match:
        # Ask user for updated details
        new_name = input("Update name (press Enter to keep): ").strip()
        new_phone = input("Update phone number (press Enter to keep): ").strip()
        new_email = input("Update email (press Enter to keep): ").strip()

        # Update contact in database
        if new_name:
            cursor.execute('UPDATE contacts SET name=? WHERE id=?', (new_name, match[0]))
        if new_phone:
            cursor.execute('UPDATE contacts SET phone=? WHERE id=?', (new_phone, match[0]))
        if new_email:
            cursor.execute('UPDATE contacts SET email=? WHERE id=?', (new_email, match[0]))

        conn.commit()
        print(f"Contact '{match[1]}' updated successfully!")
    else:
        print(f"Contact with name or ID '{query}' not found.")

def delete_contact(id):
    """Deletes a contact based on name."""
    cursor.execute('DELETE FROM contacts WHERE name=?', (id,))
    if cursor.rowcount > 0:
        conn.commit()
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

def view_contacts():
    """Prints the entire contact list from the database."""
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    if contacts:
        df = pd.DataFrame(contacts, columns=['ID', 'Name', 'Phone', 'Email'])
        print(df.to_string(index=False))    
    else:
        print("Contact list is empty!")

def main():
    """Main program loop for user interaction."""
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Search Contacts")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            create_contact()
        elif choice == '2':
            query = input("Enter name or ID to edit for: ").strip()
            edit_contact(query)
        elif choice == '3':
            name = input("Enter name of contact to delete: ").strip()
            delete_contact(name)
        elif choice == '4':
            view_contacts()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

    # Close database connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()