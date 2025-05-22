#Library Manager
#Rashen Thao
#This code is the interface of the program, it display what is being shown.

def display_separator():
    print("===========================================================================")

def display_title():
    print("\t\t\t     Library Manager")

def display_menu():
    print("MENU OPTIONS")
    print("1 - View all books")
    print("2 - Add a new book")
    print("3 - Search by title or author")
    print("4 - Exit program\n")

def get_book_input():
    print("Enter book details")
    title = input("Title: ")
    author = input("Author: ")
    genre = input("Genre: ")

    try:
        year = int(input("Year: "))
    except ValueError:
        print("Invalid year.")
        return None

    return (title, author, genre, year)

def get_search_input():
    field = input("Search by 'title' or 'author': ")
    if field not in ["title", "author"]:
        print("Invalid. Defaulting to title.")
        field = "title"
    value = input(f"{field.title()}: ")
    return field, value

def display_books(books):
    if not books:
        print("No books found.")
        return

    print()
    print(f"{'Title':<30}{'Author':<20}{'Genre':<20}{'Year'}")
    print("---------------------------------------------------------------------------")
    for book in books:
        print(f"{book[1]:<30}{book[2]:<20}{book[3]:<20}{book[4]}")
