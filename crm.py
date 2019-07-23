from contact import Contact
import sys

class CRM:

    def main_menu(self):
        while True:
            self.print_main_menu()
            user_selected = int(input())
            self.call_option(user_selected)

    def print_main_menu(self):
        print('[1] Add a new contact')
        print('[2] Modify an existing contact')
        print('[3] Delete a contact')
        print('[4] Display all the contacts')
        print('[5] Search by attribute')
        print('[6] Exit')
        print('Enter a number: ')
  
    def call_option(self, user_selected):
        if user_selected == 1:
            self.add_new_contact()
        elif user_selected == 2:
            self.modify_existing_contact()
        elif user_selected == 3:
            self.delete_contact()
        elif user_selected == 4:
            self.display_all_contacts()
        elif user_selected == 5:
            self.search_by_attribute()
        elif user_selected == 6:
            sys.exit()            
  #
    def add_new_contact(self):
        print('Enter First Name: ')
        first_name = input()
        print('Enter Last Name: ')
        last_name = input()
        print('Enter Email Address: ')
        email = input()
        print('Enter a Note: ')
        note = input()
        contact = Contact.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            note=note
            )
  #
    def modify_existing_contact(self):
        print('Please enter Contact ID to be modified: ')
        identity = int(input())
        contact_to_mod = Contact.get(id=identity)
        print('For this contact which attribute would you like to modify: ')
        attribute_to_modify = input()
        print('For this attribute what is the value of the modification: ')
        value_of_mod = input()
        contact_to_mod.update(attribute_to_modify, value_of_mod)
  #
    def delete_contact(self):
        print('Please enter Contact ID to be deleted: ')
        ident_contact = int(input())
        delete_contact = Contact.get(id=ident_contact)
        delete_contact.delete()
  #
    def display_all_contacts(self):
        Contact.all()

    def search_by_attribute(self):
        print('Please select which attribute you want to search by: ')
        attribute_to_search = input()
        print('Please enter the value you want to search by: ')
        value_to_search = input()
        print(Contact.find_by(attribute_to_search, value_to_search))

a_crm_app = CRM()
a_crm_app.main_menu()