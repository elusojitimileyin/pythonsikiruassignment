contact_name = []
contact_phone_number = []


def get_contact_name():
    return contact_name


def get_contact_phone_number():
    return contact_phone_number


def add_contact(name, phoneNumber):
    contact_name.append(name)
    contact_phone_number.append(phoneNumber)


def remove_contact_name(name_to_remove):
    for name in contact_name:
        if name == name_to_remove:
            contact_name.remove(name)
        else:
            print("contact not found")


def remove_contact_phone_number(phone_number_to_remove):
    for phone_number in contact_phone_number:
        if phone_number == phone_number_to_remove:
            contact_phone_number.remove(phone_number)


def display_contacts():
    print("Contact Details: ")
    for index in range(len(contact_name)):
        print("---------------")
        print(contact_name[index], contact_phone_number[index])
        print("---------------")


def edit_contacts(name, phoneNumber, new_name, new_phoneNumber):
    for index in range(len(contact_name)):
        if contact_name[index] == name:
            contact_name[index] = new_name
    for index in range(len(contact_phone_number)):
        if contact_phone_number[index] == phoneNumber:
            contact_phone_number[index] = new_phoneNumber
