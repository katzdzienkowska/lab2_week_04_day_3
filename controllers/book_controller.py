from flask import Flask, render_template, request, redirect
from repositories import book_repository, author_repository
from flask import Blueprint
from models.book import Book

books_blueprint = Blueprint ("library", __name__)

# INDEX
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)


# NEW
@books_blueprint.route("/books/new", methods=["get"])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)

# CREATE
@books_blueprint.route("/books", methods=["post"])
def add_book():
    title = request.form["title"]
    author_id = request.form["author_id"]
    genre = request.form["genre"]
    author = author_repository.select(author_id)
    book = Book(title, author, genre)
    book_repository.save(book)
    return redirect("/books")

# SHOW
@books_blueprint.route("/books/<id>", methods=["get"])
def show_book(id):
    found_book = book_repository.select(id)
    return render_template("books/show.html", book = found_book)

# EDIT
@books_blueprint.route("/books/<id>/edit")
def edit_book(id):
    found_book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template("/books/edit.html", book = found_book, all_authors = authors)

# UPDATE
@books_blueprint.route("/books/<id>", methods=["post"])
def update_book(id):
    title = request.form["title"]
    author_id = request.form["author_id"]
    genre = request.form["genre"]
    author = author_repository.select(author_id)
    book = Book(title, author, genre, id)
    book_repository.update(book)
    return redirect("/books")

# DELETE
@books_blueprint.route("/books/<id>/delete", methods=["post"])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")
