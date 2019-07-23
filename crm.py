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
        if attribute_to_modify == 'first_name':
            contact_to_mod.first_name = value_of_mod
            contact_to_mod.save()
        elif attribute_to_modify == 'last_name':
            contact_to_mod.last_name = value_of_mod
            contact_to_mod.save()
        elif attribute_to_modify == 'email':
            contact_to_mod.email = value_of_mod
            contact_to_mod.save()
        elif attribute_to_modify == 'note':
            contact_to_mod.note = value_of_mod
            contact_to_mod.save()            
  #
    def delete_contact(self):
        print('Please enter Contact ID to be deleted: ')
        ident_contact = int(input())
        delete_contact = Contact.get(id=ident_contact)
        delete_contact.delete_instance()
  #
    def display_all_contacts(self):
        for contact in Contact.select():
            print(contact.first_name, contact.last_name, contact.email, contact.note)

    def search_by_attribute(self):
        print('Please select which attribute you want to search by: ')
        attribute_to_search = input()
        print('Please enter the value you want to search by: ')
        value_to_search = input()
        if attribute_to_search == 'first_name':
            searched_contact = Contact.get(Contact.first_name == value_to_search)
        elif attribute_to_search == 'last_name':
            searched_contact = Contact.get(Contact.last_name == value_to_search)
        elif attribute_to_search == 'email':
            searched_contact = Contact.get(Contact.email == value_to_search)
        elif attribute_to_search == 'note':
            searched_contact = Contact.get(Contact.note == value_to_search) 
        print(searched_contact)

a_crm_app = CRM()
a_crm_app.main_menu()