class LibraryAccount:
    def __init__(self, name):
        self.name = name
        self.books_issued = []

    def issue_book(self, book_name):
        self.books_issued.append(book_name)
        return True

    def return_book(self, book_name):
        if book_name in self.books_issued:
            self.books_issued.remove(book_name)
            return True
        return False

    def has_books(self):
        return len(self.books_issued) > 0

    def total_books(self):
        return len(self.books_issued)

acc = LibraryAccount("Raghav")

acc.issue_book("Clean Code")
acc.issue_book("Introduction to Algorithms")

acc.return_book("Clean Code")

