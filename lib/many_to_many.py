class Author:
    def __init__(self, name):
        self.name = name

        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(self, name):
            if not isinstance(name, str):
                raise TypeError("Name should be a string")
            self._name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self): 
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    def __init__(self, title):
        self.title = title

        @property
        def title(self):
            return self._title
        
        @title.setter
        def title(self, title):
            if not isinstance(title, str):
                raise TypeError("Title should be a string")
            self._title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("author should be an instance of Author clas")
        self._author = author

    @property
    def book(self):
        return self._book
        
    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise TypeError("book should be an instance of Book clas")
        self._book = book

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise TypeError("date should be valid- in string format")
        self._date = date

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise TypeError("royalties should be a number, representing persentage")
        self._royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]