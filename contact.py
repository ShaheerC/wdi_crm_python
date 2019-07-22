class Contact:

    contacts = []
    next_id = 1

    def __init__(self, first, last, email, note):
        self.first = first
        self.last = last
        self.email = email
        self.note = note
        self.id = Contact.next_id
        Contact.next_id += 1
        """This method should initialize the contact's attributes"""

    def __str__(self):
        return"CONTACT: first:{} - last:{} - email:{} - note:{}".format(self.first, self.last, self.email, self.note)


    @classmethod
    def create(cls, first, last, email, note):
        person = Contact(first, last, email, note)
        cls.contacts.append(person)
        return person
        """This method should call the initializer,
        store the newly created contact, and then return it
        """

    @classmethod
    def all(cls):
        for contact in Contact.contacts:
            print(contact)
        """This method should return all of the existing contacts"""

    @classmethod
    def find(cls, ident):
        for contact in Contact.contacts:
            if ident == contact.id:
                return contact.full_name()

        """ This method should accept an id as an argument
        and return the contact who has that id
        """

    def update(self, attribute_update, value_update):
        if attribute_update == 'first':
            self.first = value_update
        elif attribute_update == 'last':
            self.last = value_update
        elif attribute_update == 'email':
            self.email == value_update
        elif attribute_update == 'note':
            self.note == value_update

        """ This method should allow you to specify
        1. which of the contact's attributes you want to update
        2. the new value for that attribute
        and then make the appropriate change to the contact
        """


    @classmethod
    def find_by(cls, attribute, value):
        for contact in Contact.contacts:
            if attribute == 'first' and value == contact.first:
                return contact
            if attribute == 'last' and value == contact.last:
                return contact
            if attribute == 'email' and value == contact.email:
                return contact
            if attribute == 'note' and value == contact.note:
                return contact
        """This method should work similarly to the find method above
        but it should allow you to search for a contact using attributes other than id
        by specifying both the name of the attribute and the value
        eg. searching for 'first_name', 'Betty' should return the first contact named Betty
        """

    @classmethod
    def delete_all(cls):
        Contact.contacts.clear()
        """This method should delete all of the contacts"""


    def full_name(self):
        name_full = self.first + ' ' + self.last
        return name_full
        """Returns the full (first and last) name of the contact"""


    def delete(self):
        Contact.contacts.remove(self)
        """This method should delete the contact
        HINT: Check the Array class docs for built-in methods that might be useful here
        """

    # Feel free to add other methods here, if you need them.

bob = Contact.create('Bob', 'Bobb', 'bob@bob.bob', 'bob bobbing in the bob')
billy = Contact.create('Billy', 'Billee', 'billy@billy.billy', 'billy billying in the billy')

print(bob.first)
print(bob.last)
print(bob.email)
print(bob.note)
print(billy.first)
print(billy.last)
print(billy.email)
print(billy.note)

print(len(Contact.contacts))
print(bob.id)
print(billy.id)

print(billy.full_name())

print(Contact.find(1))

Contact.all()

bob.delete()

Contact.all()

billy.update('first', 'john')

Contact.all()

print("Find John")
print(Contact.find_by("first", "john"))
print(Contact.find_by("email", "billy@billy.billy"))

Contact.delete_all()

Contact.all()