
contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print(" Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\n📋 Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    keyword = input("Enter name or phone number to search: ")

    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            print("\n🔍 Contact Found:")
            print(contact)
            return

    print(" Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email: ")
            contact['address'] = input("Enter new address: ")
            print("✏️ Contact updated successfully!")
            return

    print(" Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("🗑️ Contact deleted successfully!")
            return

    print(" Contact not found.")

# Menu-driven interface
while True:
    print("\n====== CONTACT MANAGEMENT SYSTEM ======")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print(" Exiting Contact Management System")
        break
    else:
        print("Invalid choice. Try again.")

