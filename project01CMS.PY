import re
contacts = []


def create_contact():
    """Prompts user for contact details and creates a new dictionary"""
    
    name = str(input("Enter contact name:"))
    if not name:  # Check if name is empty
        print("Name cannot be empty!")
        return None
    
    while True:
        phone = input("Enter phone number: ")
        if not phone:  # Check if phone number is empty
            print("Phone number cannot be empty!")
            continue  # Restart the loop to prompt for phone number again
        elif not phone.isdigit():  # Check if phone number contains non-digit characters
            print("Phone number can only contain digits!")
            continue  # Restart the loop to prompt for phone number again
        else:
            break  # Phone number is valid, exit the loop
        
    while True:
        email = input("Enter email: ")
        if not email:  # Check if email is empty
            print("Email cannot be empty!")
            continue  # Restart the loop to prompt for email again
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):  # Check if email format is valid
            print("Invalid email format!")
            continue  # Restart the loop to prompt for email again
        else:
            break  # Email is valid, exit the loop


    for contact in contacts:
        if contact["phone"] == phone:
            print("Contact with the same phone number already exists!")
            return None
        
    

    return {"name": name, "phone": phone,"id":phone, "email": email}
    

def edit_contact(contacts, query):
    """Edits an existing contact based on name"""
    match = None
    for contact in contacts:
        if query.lower() == contact["name"].lower() or query == str(contact["id"]):
            match = contact
            break
    if match:
        new_name = input("Update name (press Enter to keep): ")
        while True:
            new_phone = input("Update phone number (press Enter to keep): ")
            if not new_phone:  # Check if phone number is empty
                print("Phone number cannot be empty!")
                continue  # Restart the loop to prompt for phone number again
            elif not new_phone.isdigit():  # Check if phone number contains non-digit characters
                print("Phone number can only contain digits!")
                continue  # Restart the loop to prompt for phone number again
            else:
                break  # Phone number is valid, exit the loop
        
        while True:
            new_email = input("Update email (press Enter to keep): ")
            if not new_email:  # Check if email is empty
                print("Email cannot be empty!")
                continue  # Restart the loop to prompt for email again
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):  # Check if email format is valid
                print("Invalid email format!")
                continue  # Restart the loop to prompt for email again
            else:
                break  # Email is valid, exit the loop
        
        for contact in contacts:
            if contact["phone"] == new_phone:
                print("Contact with the same phone number already exists!")
                return None
            
        
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
    """Deletes a contact based on name"""
    for i, contact in enumerate(contacts):
        if contact["name"] == name:
            del contacts[i]
            print(f"Contact '{name}' deleted successfully!")
            return
    print(f"Contact '{name}' not found.")

def view_contacts(contacts):
    """Prints the entire contact list"""
    if not contacts:
        print("Contact list is empty!")
        return
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
    """Searches for contacts by name or ID"""
    matches = []
    query = query.lower()
    for contact in contacts:
        if query in contact["name"].lower() or query == str(contact["id"]):
            matches.append(contact)
    if matches:
        print(f"Search results for '{query}':")
        view_contacts(matches)
    else:
        print(f"No contacts found matching '{query}'.")
def main():
    """Main program loop for user interaction"""
   
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Search Contacts")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            contact = create_contact()
            if contact is not None:  # Check if create_contact() returns a valid contact
                contacts.append(contact)
                print("Contact added successfully!")
        elif choice == '2':
            query = input("Enter name or ID to edit for: ")
            edit_contact(contacts, query)
        elif choice == '3':
            name = input("Enter name of contact to delete: ")
            delete_contact(contacts, name)
        elif choice == '4':
            view_contacts(contacts)
        elif choice == '5':
            query = input("Enter name or ID to search for: ")
            search_contacts(contacts.copy(), query)
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.") 

if __name__ == "__main__":
    main()
