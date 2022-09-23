from secrets import choice

# The library class


class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("\nBooks present in this library are: ")
        for book in self.books:
            print(" * " + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"You have been issued {bookName}, Please keep it safe and return it within 10 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry! This book is either not available or has already been borrowed by someone else. Please wait for it to be available.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it.")

# The student class


class Student:
    def requestBook(self):
        self.book = input("\nEnter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input(
            "\nEnter the name of the book you want to add or return: ")
        return self.book


# main function
if __name__ == "__main__":
    centralLibrary = Library(
        ["Algorithm", "Swift", "Jungle Book", "Java", "Python"])
    student = Student()
    while (True):
        welcomeCLMS = '''\n******* Welcome to Central Library *******
        Please choose an option:
        1. List of all the available books
        2. Request a book
        3. Add/Return a book
        4. Exit'''
        print(welcomeCLMS)
        choice = int(input("\nEnter a choice: "))
        if choice == 1:
            centralLibrary.displayAvailableBooks()
        elif choice == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif choice == 3:
            centralLibrary.returnBook(student.returnBook())
        elif choice == 4:
            print("\nThanks for choosing Central Library! Have a great day.")
            exit()
        else:
            print("\nInvalid Choice!")
