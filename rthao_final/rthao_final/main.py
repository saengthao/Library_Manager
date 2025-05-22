#Library Manager
#Rashen Thao
#This code is the main program that controls how the program works.

import db
import ui

def main():
    ui.display_separator()
    ui.display_title()
    ui.display_menu()
    ui.display_separator()

    books = db.get_books()

    while True:
        option = input("Menu option: ")

        if option == "1":
            ui.display_books(books)
        elif option == "2":
            book = ui.get_book_input()
            if book:
                db.add_book(book)
                books = db.get_books()
        elif option == "3":
            field, value = ui.get_search_input()
            results = db.search_books(field, value)
            ui.display_books(results)
        elif option == "4":
            print("Bye!")
            break
        else:
            print("Invalid menu option.")
        print()

main()
