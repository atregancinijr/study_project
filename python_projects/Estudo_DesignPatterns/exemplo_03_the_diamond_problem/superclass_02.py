class Contact:
    all_contacts = []

    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class AddressHolder:
    def __init__(self, street='', city='', state='', code='', **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone

"""**kwargs syntax.
it basically collects any keyword arguments passed into the method that 
were not explicitly listed in the parameter list. These arguments are stored
in a dictionary named kwargs (we can call the variable whatever we like,
but convention suggests kw, or kwargs). When we call a different method 
(for example: super().__init__) with a **kwargs syntax, it unpacks the dictionary
and passes the results to the method as normal keyword arguments."""

