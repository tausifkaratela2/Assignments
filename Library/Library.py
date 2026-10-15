import csv
import os
 
FILE = "books.csv"
 
 
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
 
 
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
 
    def add(self, title, author):
        self.books.append(Book(title, author))
        with open(FILE, "a", newline="") as f:
            csv.writer(f).writerow([title, author])
        print(f"Added {title} to {self.name}")
 
    def show_books(self):
        if not os.path.exists(FILE):
            print("No books saved yet.")
            return
        with open(FILE, newline="") as f:
            for row in csv.reader(f):
                print(f"{row[0]} by {row[1]}")
 
 
lib = Library("My Library")
 
while True:
    print("\n1. Add book | 2. View books | 3. Exit")
    choice = input("Choose an option: ")
 
    if choice == "1":
        title = input("Book title: ")
        author = input("Author: ")
        lib.add(title, author)
    elif choice == "2":
        lib.show_books()
    elif choice == "3":
        break
    else:
        print("Please choose 1, 2 or 3.")
 