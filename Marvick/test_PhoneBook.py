import unittest
from Marvick import PhoneBook


class test_phone_book(unittest.TestCase):

    def test_add_contact(self):
        self.assertEqual(0, len(PhoneBook.get_contact_name()))
        self.assertEqual(0, len(PhoneBook.get_contact_phone_number()))

        PhoneBook.add_contact("joy", "12334566")
        self.assertEqual(1, len(PhoneBook.get_contact_name()))
        self.assertEqual(1, len(PhoneBook.get_contact_phone_number()))

        PhoneBook.add_contact("joy", "12334566")
        self.assertEqual(2, len(PhoneBook.get_contact_name()))
        self.assertEqual(2, len(PhoneBook.get_contact_phone_number()))
    def test_remove_contact(self):
        PhoneBook.add_contact("joy", "12334566")
        PhoneBook.add_contact("timi", "566")

        PhoneBook.remove_contact("joy", "12334566")
        self.assertEqual(1, len(PhoneBook.get_contact_name()))
        self.assertEqual(1, len(PhoneBook.get_contact_phone_number()))
