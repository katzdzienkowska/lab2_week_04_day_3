import pdb
from models.author import Author
from models.book import Book

import repositories.book_repository as book_repository
import repositories.authors_repository as authors_repository

book_repository.delete_all()
authors_repository.delete_all()

author_1 = Author("Fyodor Dostoevsky")
authors_repository.save(author_1)

book_1 = Book("Crime and Punishment", author_1, "Fiction")
book_repository.save(book_1)
book_2 = Book("Ther Idiot", author_1, "Fiction")
book_repository.save(book_2)

authors_repository.select_all()
book_repository.select_all()
