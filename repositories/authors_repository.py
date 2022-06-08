from db.run_sql import run_sql
from models.author import Author
from models.book import Book
import repositories.authors_repository as author_repository

def save(author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING *"
    values = [author.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def select_all():
    authors = []
    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for result in results:
        author = Author(result["name"], result["id"])
        authors.append(author)
    return authors

