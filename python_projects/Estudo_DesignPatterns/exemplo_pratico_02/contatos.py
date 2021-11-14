class ContactList(list):
    def search(self, name):

        """Return all contacts that contain the search value in their name."""

        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):

    def order(self, order):
        print("If this were a real system we would send a {} order to {}".format(order, self.name))


class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email + "...")
        print(f'{message}')
        # Add e-mail logic here

class EmailableContact(Contact, MailSender):
    pass


class LongNameDict(dict):

    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest


if __name__ == '__main__':
    print('Exemplo 1:')
    c = Contact('meu contato', 'contato@email.com')
    s = Supplier('meu fornecedor', 'fornecedor@email.com')
    print(c.name, c.email, '\n', s.name, s.email)
    s.order('XXX')
    print(s.all_contacts)
    print([c1.name for c1 in Contact.all_contacts.search("contato")])

    print('Exemplo 2:')
    longkeys = LongNameDict()
    longkeys['hello'] = 1
    longkeys['longest yet'] = 5
    longkeys['hello2'] = 'world'
    print(longkeys.longest_key())

    print('Exemplo 3:')
    f = Friend('meu amigo', 'amigo@email.com', '36333333')
    print(f.all_contacts)

    print('Exemplo 4:')
    e = EmailableContact("John Smith", "jsmith@example.net")
    e.send_mail("Hello, test e-mail here")
