import requests
import logging
import time
""""
#from pages.books_page import BooksPage

#page_content = requests.get('http://books.toscrape.com').content
#page = BooksPage(page_content)
#books = page.books

REQUESTED_PAGE = 'http://books.toscrape.com/catalogue/page-'

def populate_books_list(books_list):
    for i in range(1, 51):
        page_number = str(i)
        page_content = requests.get(REQUESTED_PAGE + page_number + '.html').content
        page = BooksPage(page_content)
        page_books = page.books
        books_list.append(page_books)
    return books_list

books = []
populate_books_list(books)
#print(books)
"""

from pages.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H%:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')

logger.info('Requesting http://books.toscrape.com')
page_content = requests.get('http://books.toscrape.com').content

logger.debug('Creating AllBooksPage from page content')
page = AllBooksPage(page_content)

_books = []
_books.extend(page.books)

start = time.time()
logger.info(f'Going through {page.page_count} pages of books...')
for page_num in range(1, page.page_count):
    page_start = time.time()
    url = f'http://books.toscrape.com/catalogue/page{page_num + 1}.html'
    logger.info(f'Requesting {url}')
    page_content = requests.get(url).content
    logger.debug('Creating AllBooksPage from page cotent')
    page = AllBooksPage(page_content)
    print(f'{url} took { time.time() - page_start}')
    _books.extend(page.books)
print(f'Total took {time.time() - start}')

books = _books
print('------ BOOKS --------')
print(books)