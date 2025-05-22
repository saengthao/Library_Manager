#Library Manager
#Rashen Thao
#This code defines the book class, which is used to represent what a book is.

class Book:
    def __init__(self, title, author, genre, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year

    def display(self):
        return f"{self.title}\t{self.author}\t{self.genre}\t{self.year}"
