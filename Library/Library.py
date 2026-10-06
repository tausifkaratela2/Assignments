class Book:
    def __init__(self, title, book_id, author):
        self.title = title
        self.book_id = book_id
        self.author = author
        self.is_borrowed = False


class Library:
    def __init__(self, name):
         self.name = name
         self.books = []

    def add(self, title):
        self.books.append(title)
        print(f"Added {title} to {self.name}")
    
    def show_Books(self):
         print(f"books in {self.name}", self.books)

    def borrow(self, title):
        if title in self.books:
            self.books.remove(title)
            print(f"you borrowed {title} from {self.name}")
        else:
            print(f"{title} is not available in {self.name}")


lib1 = Library("One")
lib2 = Library("Two")

while True:
    print("\n1. Add | 2. Show | 3. Borrow | 4. Exit")
    a = input("Choose an option: ")

    if a == 4:
        break

    t = input("WHich Library? lib1/lib2: ")
    lib = lib1 if t == "lib1" else lib2

    if a == "1":
        title = input("Enter the book title: ")
        lib.add(title)

    elif a == "2":
        lib.show_Books()

    elif a == "3":
        try:
            t == input("Enter book title")
            lib.borrow(title)
        except:
            print("You have already borrowed this book once")