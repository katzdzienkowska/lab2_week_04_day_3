from flask import Flask, render_template, request, redirect
from repositories import author_repository, book_repository
from models.author import Author
from models.book import Book


from flask import Blueprint

tasks_blueprint = Blueprint ("library", __main__)
