class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []
        self._books = []

    def contracts(self):
        return self._contracts
    
    def books(self):
        return self._books
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)
        



class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []
        self._authors = []
        
    def contracts(self):
        return self._contracts
    
    def authors(self):
        return self._authors



class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.validates_author(author)
        self.validates_book(book)
        self.validates_date(date)
        self.validates_royalties(royalties)

        author._contracts.append(self)

        if book not in author._books:
            author._books.append(book)

        book._contracts.append(self)
        
        if author not in book._authors:
            book._authors.append(author)

        Contract.all.append(self)

        

    def validates_author(self, author):
        if not isinstance(author, Author):

            raise Exception("Expected an instance of Author")
        return True
    
    def validates_book(self, book):
        if not isinstance(book, Book):
            raise Exception("Expected an instance of Book")
        return True
    
    def validates_date(self, date):
        if not isinstance(date, str):
            raise Exception("Expected date type of str")
        return True
    
    def validates_royalties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception("Expected royalty type of int")
        return True
    @classmethod
    def contracts_by_date(cls, date=None):
        sorted_contracts = sorted(cls.all, key=lambda contract: contract.date) 
        if date:
            return [contract for contract in sorted_contracts if contract.date == date]
        return sorted_contracts    