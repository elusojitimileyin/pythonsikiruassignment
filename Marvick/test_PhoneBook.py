import unittest
import PhoneBook




class TestPhoneBook(unittest.TestCase):


    def test_add_contact(self):
        PhoneBook.add_contact("timi","seee","081111112222", "dshdhhd@dkdk")
        self.assertEqual(1, )
    def test_remove_contact(self):
        Phonebook.add_contact()

        Phonebook.remove_contact()

    def test_display_contacts(self):
        Phonebook.add_contact()
        Phonebook.display_contacts()
