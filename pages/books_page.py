from bs4 import BeautifulSoup

from locators.books_page_locators import BooksPageLocators
from parsers.book_parser import BookParser


class BooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')
    
    @property
    def books(self):
        locator = BooksPageLocators.BOOKS
        return [BookParser(e) for e in self.soup.select(locator)]