contact_name = []
contact_phoneNumber = []
def add_contact(name, phonenumber):
    contact_name.append(name)
    contact_phoneNumber.append(phonenumber)


def remove_contact(name_to_remove):
    for name in  contact_name:

    PhoneBook.contacts = [contact for contact in PhoneBook.contacts if contact.name != name_to_remove]


def display_contacts():
    print("Contact Details: ")
    for contact in PhoneBook.contacts:
        print("---------------")
        print(contact.get_display_info())
        print("---------------")


def main():
    while True:
        print("\nWelcome to Timi Phonebook App Menu:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts")
        print("4. Exit Contact")
        user_choice = input("Choose an option: ")

        if user_choice == '1':
            add_contact()
        elif user_choice == '2':
            remove_contact()
        elif user_choice == '3':
            display_contacts()
        elif user_choice == '4':
            print("Exit Timi Phonebook App")
            break
        else:
            print("Invalid option.")


class PhoneBook:
    contacts = []

    def __init__(self, name, address, phone_number, email_address):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email_address = email_address

    def get_display_info(self):

        return f"Name: {self.name}\n Address: {self.address}\n Phone Number: {self.phone_number}\n Email Address: {self.email_address}"

    @classmethod
    def Contact(cls, name, address, phone_number, email_address):
        pass
