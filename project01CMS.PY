import re
import pandas as pd
from datetime import datetime

contacts = []

def generate_id():
    """Generates an ID based on the current date and count of contacts."""
    today = datetime.now().strftime("%Y%m%d")
    count = sum(1 for contact in contacts if contact["id"].startswith(today))
    return f"{today}{count:04d}"

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
    """Prompts user for contact details and creates a new dictionary."""
    name = input("Enter contact name: ").strip()
    while True:
        phone = input("Enter mobile number: ").strip()
        try:
            phone = validate_phone_number(phone)
            if any(contact["phone"] == phone for contact in contacts):
                print("Mobile number already exists!")
                continue
            break
        except ValueError as e:
            print(str(e))
    while True:
        email = input("Enter Email: ").strip()
        try:
            email = validate_email(email)
            if any(contact["email"] == email for contact in contacts):
                print("Email ID already exists!")
                continue
            break
        except ValueError as e:
            print(str(e))  
    id = generate_id()  
    return {"id": id, "name": name, "phone": phone, "email": email}

def edit_contact(contacts, query):
    """Edits an existing contact based on name or ID."""
    match = None
    for contact in contacts:
        if query.lower() == contact["name"].lower() or query == str(contact["id"]):
            match = contact
            break
    if match:
        try:
            new_name = input("Update name (press Enter to keep): ").strip()
            
            while True:
                new_phone = input("Update phone number (press Enter to keep): ").strip()
                try:
                    new_phone = validate_phone_number_edit(new_phone)
                    if any(contact["phone"] == new_phone and contact != match for contact in contacts):
                        print("Mobile number already exists!")
                        continue
                    break
                except ValueError as e:
                    print(str(e))
            
            while True:
                new_email = input("Update email (press Enter to keep): ").strip()
                try:
                    new_email = validate_email_edit(new_email)
                    if any(contact["email"] == new_email and contact != match for contact in contacts):
                        print("Email ID already exists!")
                        continue
                    break
                except ValueError as e:
                    print(str(e))
        except ValueError as e:
            print(str(e))

        if new_phone:
            match["id"] = new_phone
        if new_name:
            match["name"] = new_name
        if new_phone:
            match["phone"] = new_phone
        if new_email:
            match["email"] = new_email
        print(f"Contact '{match['name']}' updated successfully!")
    else:
        print(f"Contact with name or ID '{query}' not found.")

def delete_contact(contacts, name):
    """Deletes a contact based on name."""
    for i, contact in enumerate(contacts):
        if contact["name"] == name:
            del contacts[i]
            print(f"Contact '{name}' deleted successfully!")
            return
    print(f"Contact '{name}' not found.")

def view_contacts(contacts):

    """Prints the entire contact list (optional)in a formatted table using pandas."""
    if not contacts:
        print("Contact list is empty!")
        return
    #convert contact list to a pandas Dataframe
    df = pd.DataFrame(contacts)
    if not df.empty: #check dataframe is empty or not.
        #Format and Display the dataframe(using to_string with formatting)
        print(df.to_string(index=False)) #Avoids unnecessary index column
    else:
        print("-" * 30)
        print("Contact List:")
        for contact in contacts:
            print(f"ID: {contact['id']}")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            if contact.get("email"):
                print(f"Email: {contact['email']}")
        print("-" * 30)

def search_contacts(contacts, query):
    """Searches for contacts by name or ID."""
    matches = []
    query = query.strip().lower()
    for contact in contacts:
        if query in contact["name"].lower() or query == str(contact["id"]):
            matches.append(contact)
    if matches:
        print(f"Search results for '{query}':")
        view_contacts(matches)
    else:
        print(f"No contacts found matching '{query}'.")

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
            contact = create_contact()
            if contact is not None:
                contacts.append(contact)
                print("Contact added successfully!")
        elif choice == '2':
            query = input("Enter name or ID to edit for: ").strip()
            edit_contact(contacts, query)
        elif choice == '3':
            name = input("Enter name of contact to delete: ").strip()
            delete_contact(contacts, name)
        elif choice == '4':
            view_contacts(contacts)
        elif choice == '5':
            query = input("Enter name or ID to search for: ").strip()
            search_contacts(contacts.copy(), query)
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
