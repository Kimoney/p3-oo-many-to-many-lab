from datetime import date

class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        pass


class Book:
    def __init__(self, title):
        self.title = title


class Contract:
    def __init__(self, author, book, date=date.today(), royalties=10):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception
        self._author = author

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if not isinstance (book, Book):
            raise Exception
        self._book = book

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if type(date) != str:
            raise Exception
        self._date = date

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self,royalties):
        if type(royalties) != int:
            raise Exception
        self._royalties = royalties