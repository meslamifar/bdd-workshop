class PhoneBook:
    def __init__(self, phone_numbers=[], address_book={}):
        self.address_books = address_book
        self.phone_numbers = phone_numbers

    def add_new_number(self, phone_number, details):
        if phone_number in self.phone_numbers:
            raise Exception('It is already in the list')
        else:
            self.phone_numbers.append(phone_number)
            self.address_books[phone_number] = details

    def add_note(self, phone_number, document):
        if len(document) < 250:
            self.address_books[phone_number][document] = document

    def update_details(self, phone_number, details):
        if phone_number in self.phone_numbers:
            self.address_books[phone_number] = details

    def remove_number(self, phone_number):
        if phone_number in self.address_books:
            self.phone_numbers.remove(phone_number)
            self.address_books.pop(phone_number)

    def search(self, name):
        print(self.address_books)
        result = []
        for key in self.phone_numbers:
            if name == self.address_books[key]['first_name']:
                result.append(self.address_books[key])
        print(result)
        return result
