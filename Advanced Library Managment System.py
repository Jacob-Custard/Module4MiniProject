#Create an improved, user-friendly command-line interface (CLI) for the Library Management System with separate menus for each class of the system.

#Implement a class structure that represents key entities in the library management system, including:
#Book: A class representing individual books with attributes such as title, author,  genre, publication date, and availability status.
#User: A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
#Author: A class representing book authors with attributes like name and biography.

#Apply encapsulation principles by defining private attributes and using getters and setters for necessary data access.

#Organize your code into modules to promote code organization and maintainability. Create separate modules for classes, user interactions, and error handling.

#Implement the following actions in response to menu selections using the classes you've created: Adding a new book with all relevant details, allowing users to
#borrow a book, marking it as "Borrowed", allowing users to return a book, marking it as "available", searching for a book by its unique identifier (title) and displaying its details,
#displaying a list of all books with their unique identifiers, adding a new user with user details, viewing user details, displaying a list of all users, adding a new author with
#author details, viewing author details, displaying a list of all authors, quitting the application.

#Utilize the input() function within the appropriate menus to enable users to interact with the CLI and select menu options.
#Implement input validation using regular expressions (regex) to ensure the correct formatting of user input. (Bonus)

#Implement error handling where applicable using try, except, else, and finally blocks to manage potential issues gracefully, such as incorrect user input or file operations.

import book_systems as booksys
import author_systems as authorsys
import user_systems as usersys

def main():
     while True:
        print("\nWelcome to the Advanced Library Managment Application")
        print("\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Exit")
        user_choice = input("Enter function you'd like to perform (1-4): ")
        
        if user_choice == "1":                                                                                                                                  #if block determining if the user selected choice 1
            booksys.book_operations()
        
        elif user_choice =="2":                                                                                                                                 #elif block determining if the user selected choice 2
            usersys.user_operations()

        elif user_choice == "3":                                                                                                                                #elif block determining if the user selected choice 3
            authorsys.author_operations()

        elif user_choice == "4":                                                                                                                                #elif block determining if the user selected choice 4
            print("Thank you for using Advanced Library Managment Application!")
            break

        else: print("Input not recognized please enter a number 1-4 for your choice.")                                                                          #else block and print statement letting the user know their input wasnt recognized


main()