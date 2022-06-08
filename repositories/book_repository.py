from db.run_sql import run_sql
from models.author import Author
from models.book import Book

import repositories.authors_repository as author_repository

# get all books
def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row["user_id"])
        book = Book(row["title"], row["title"], row["genre"], author, row["id"])
        books.append(book)
    return books


# delete a book
def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)


####

# create book
# get single book
