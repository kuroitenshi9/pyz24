def welcome_user(username: str) -> str:
    return f"welcome {username}"

class Person:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactManager:
    def __init__(self):
        self.contacts = []

    def display_menu(self) -> None:
        print("1. Display all contacts")
        print("2. Add a new contact")
        print("3. Delete a contact")
        print("4. Quit the program")
    
    def display_all(self) -> None:
        if not self.contacts:
            print("No available contacts.")
        else:
            for contact in self.contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print()
                
    def add_contact(self):
        try:
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")

            if not name or not phone or not email:
                raise ValueError("Name, phone number, and email address are required.")
            
            if not name.isalpha():
                name = input("Name should contain only letters. Please enter again: ")
            
            if not email.isalpha() and ['@', '.'] in email:
                email = input("Enter the correct email address: ")

            while True:
                phone = input("Enter the phone number: ")
                if phone.isdigit() and len(phone) == 9:
                    break
                else:
                    phone = input("Phone should contain only numbers. Please enter the correct phone number: ")
    
            new_contact = Person(name, phone, email)
            self.contacts.append(new_contact)
            print("New contact added!")

        except ValueError as e:
            print("Error:", e)


    '''def new_contact(contacts):
    
        name = input("Enter the name: ")
        email = input("Enter the email address: ")

        while True:
                phone = input("Enter the phone number: ")
                if phone.isdigit() and len(phone) == 9:
                    break
                else:
                    phone = input("Phone should contain only numbers. Please enter the correct phone number: ")
    
            
        contact = {
            "name": name,
            "phone": phone,
            "email": email
            }

        contacts.append(contact)
        print("New contact added!")'''
        
    '''name = input("Enter the name: ")
            if not name.isalpha():
                name = input("Name should contain only letters. Please enter again: ")

            phone = input("Enter the phone number: ")
            if not phone.isdigit():
                phone = input("Phone should contain only numbers. Please enter the correct phone number: ")

            email = input("Enter the email address: ")
            if not email.isalpha() and ['@', '.'] in email:
                email = input("Enter the correct email address: ")
    '''

    def delete_contact(self):
        try:
            name = input("Enter the name of the contact to delete: ")

            if not name:
                raise ValueError("Name is required for deletion.")

            for contact in self.contacts:
                if contact.name == name:
                    self.contacts.remove(contact)
                    print("Contact deleted!")
                    return

            print("Contact not found.")

        except ValueError as e:
            print("Error:", e)

    def start(self):
        user_name = input("Input your name: ")
        print(welcome_user(8))
        self.display_menu()

        while True:
            choice = input("Select an option (1-4): ")

            if choice == "1":
                self.display_all()
            elif choice == "2":
                self.add_contact()
            elif choice == "3":
                self.delete_contact()
            elif choice == "4":
                print("Program terminated.")
                break
            else:
                print("Invalid choice. Please try again.")

''' def delete_contact(contacts):
        name = input("Enter the name of the contact to delete: ")
        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                print("Contact deleted!")
                return
        print("Contact not found.")'''


'''def main(self):
    print("Welcome to the contact management program!")
    display_menu()
    contact_book = []

    while True:
        user_selection = input("Select an option (1-4): ")

        if  user_selection == "1":
            display_all(contact_book)
        elif user_selection  == "2":
            new_contact(contact_book)
        elif user_selection  == "3":
            delete_contact(contact_book)
        elif user_selection  == "4":
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please try again.")
'''


if __name__ == '__main__':
    contact_manager = ContactManager()
    contact_manager.start()
