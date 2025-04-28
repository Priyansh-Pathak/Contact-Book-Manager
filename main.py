# Simple Contact Book Application

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("Contact added successfully.\n")

def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if contacts:
                print("\nSaved Contacts:")
                for contact in contacts:
                    name, phone, email = contact.strip().split(",")
                    print(f"Name: {name}, Phone: {phone}, Email: {email}")
            else:
                print("No contacts found.\n")
    except FileNotFoundError:
        print("No contacts found.\n")

def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False
    try:
        with open("contacts.txt", "r") as file:
            for contact in file:
                name, phone, email = contact.strip().split(",")
                if name.lower() == search_name:
                    print(f"\nContact Found: Name: {name}, Phone: {phone}, Email: {email}")
                    found = True
                    break
        if not found:
            print("Contact not found.\n")
    except FileNotFoundError:
        print("No contacts found.\n")

def main():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
