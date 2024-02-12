# class PhoneBook:
#     contacts = []
#
#
# def add_contact():
#     name = input("Enter user name: ")
#     phoneNumber = input("Enter user phone number: ")
#     new_contact = {"name": name, "phoneNumber": phoneNumber}
#     PhoneBook.contacts.append(new_contact)
#     return "contact saved success "
#
# def remove_contact():
#     name_to_remove = input("Enter contact name to remove: ")
#     found_contact = None
#     for contact in PhoneBook.contacts:
#         if contact["name"] == name_to_remove:
#             found_contact = contact
#             break
#
#     if found_contact:
#         PhoneBook.contacts.remove(found_contact)
#     else:
#         print("Contact not found")
#
#
# def display_contacts():
#     print("Contact Details: ")
#     for contact in PhoneBook.contacts:
#         print("---------------")
#         print(f"Name: {contact['name']}\nPhone Number: {contact['phoneNumber']}")
#         print("---------------")
#
#
# def main():
#     while True:
#         print("\nWelcome to Timi Phonebook App Menu:")
#         print("1. Add Contact")
#         print("2. Remove Contact")
#         print("3. Display Contacts")
#         print("4. Exit Contact")
#         user_choice = input("Choose an option: ")
#
#         if user_choice == '1':
#             add_contact()
#         elif user_choice == '2':
#             remove_contact()
#         elif user_choice == '3':
#             display_contacts()
#         elif user_choice == '4':
#             print("Exit Timi Phonebook App")
#             break
#         else:
#             print("Invalid option.")
#
#
# if __name__ == "__main__":
#     main()

