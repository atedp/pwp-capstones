class User:
    def __init__(self, name, email):
        self.name = name # expect a string
        self.email = email # expect a string
        self.books = {}
        # self.book will map a Book object to this user's rating of the book

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return 'Your email has been updated to: ' + address

    def __repr__(self):
        return 'User ' + self.name + ', email: ' + self.email + ', books read: ' + str(len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name & self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        t = 0
        for book, rating in self.books.items():
            t += rating
        return t / len(self.books)


class Book:
    def __init__(self, title, isbn):
        self.title = title # expect a string
        self.isbn = isbn # expect a number
        self.ratings = []
    
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "You have successfully updated the ISBN to: " + str(new_isbn)

    def add_rating(self, rating):
        if rating >= 0 & rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title & self.isbn == other_book.isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        t = 0
        for i in self.ratings:
            t += i
        return t / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author
    
    def __repr__(self):
        return self.title + " by " + self.author

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject # expect a string
        self.level = level # expect a string
    
    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level
    
    def __repr__(self):
        return self.title + ', a ' + self.level + ' manual on ' + self.subject

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users:
            usr = self.users.get(email)
            usr.read_book(book, rating)
            if book in self.books:
                self.books[book] += 1
                book.add_rating(rating)
            else:
                self.books[book] = 1
        else:
            return "No user withe emai' " + email + "!"

    def add_user(self, name, email, user_books=None):
        self.users[email] = User(name, email)
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        max_read = 0
        max_book = ""
        for book, read in self.books.items():
            if read > max_read:
                max_book = book
                max_read = read
            else:
                continue
        return max_book

    def highest_rated_book(self):
        max_rating = 0
        max_book = ""
        for book in self.books.keys():
            rating = book.get_average_rating()
            if rating > max_rating:
                max_book = book
                max_rating = rating
            else:
                continue
        return max_book

    def most_positive_user(self):
        max_rating = 0
        positive_user = ""
        for user in self.users.values():
            rating = user.get_average_rating()
            if rating > max_rating:
                positive_user = user
                max_rating = rating
            else:
                continue
        return positive_user

    def get_n_most_read_books(self, n):
        if type(n) == int:
            books_sorted = [k for k in sorted(self.books, key=self.books.get, reverse=True)]
            return books_sorted[:n]
        else:
            print("The input n = " + n + " is not of type int. Please pass an integer.")