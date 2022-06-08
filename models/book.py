class Book:

    def __init__ (self, get_title, get_author, get_genre, get_id = None):
        self.title = get_title
        self.author = get_author
        self.genre = get_genre
        self.id = get_id