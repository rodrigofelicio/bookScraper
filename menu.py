import app

def print_best_books():
    best_books = sorted(app.books, key=lambda x: x.rating * -1)[:10]
    for book in best_books:
            print(book)

print_best_books()