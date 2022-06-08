import pdb
from models.author import Author
from models.book import Book

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Fyodor Dostoevsky")
author_repository.save(author_1)
author_2 = Author("Han Kang")
author_repository.save(author_2)

author_repository.select_all()

book_1 = Book("Crime and Punishment", author_1, "Fiction")
book_repository.save(book_1)
book_2 = Book("Ther Idiot", author_1, "Fiction")
book_repository.save(book_2)

pdb.set_trace()