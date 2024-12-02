#book_systems is a module to manage all classes and functions related to books in the advanced library managment system.
import user_systems as usersys


def add_book():                                                                                                                                                 #defining a function to add a book to the class
    try:
        title = input("Enter the title of the book you want to add: ").strip().title()                                                                          #obtaining user input, added .title() for formatting 
        author = input("Enter the book's author: ").strip().title()                                                                                             #obtaining user input, added .title() for formatting
        genre = input("Enter book's genre: ").strip().title()                                                                                                   #obtaining user input, added .title() for formatting
        publication_year = int(input("Enter the book's first year of publication: ").strip())                                                                   #obtaining user input
        title2 = title                                                                                                                                          #second title variable set to the original user input
       
        if len(str(publication_year)) == 4:
            title = Book(title2, author, genre, publication_year)                                                                                               #creating object for class Book using user inputs
            books[title2] = title                                                                                                                               #adding object to books dictionary using the book title as the key
        else: print("\nPublication year must be a 4 digit whole number.")   
    
    except ValueError:
        print("\nPublication year must be a 4 digit whole number.")

def search_book():                                                                                                                                              #defining a fcuntion to search for a specific book
    user_book = input("Enter the title of the book you're serching for: ").strip().title()                                                                      #obtaining user input
    if user_book in books:                                                                                                                                      #if block to see if the user input is in the 'books' dictionary
        books[user_book].display_details()                                                                                                                      #calling the display details function from Books

    else: print("Title not found.")                                                                                                                             #Else and print statement letting the user know the title wasn't found   


def list_books():                                                                                                                                               #defining a function to list all books
    for book in books:                                                                                                                                          #for loop to cycle through the books dictionary
        print(book)                                                                                                                                             #printing each book

books = {}                                                                                                                                                      #empty dictionary

class Book:                                                                                                                                                     #establishing a class called Book
    def __init__(self, title, author, genre, publication_year):                                                                                                 #initializing the class
        self.__title = title                                                                                                                                    #private attribute
        self.__author = author                                                                                                                                  #private attribute
        self.__genre = genre                                                                                                                                    #private attribute
        self.__publication_year = publication_year                                                                                                              #private attribute
        self.__available = True                                                                                                                                 #private attribute

    def get_title(self):                                                                                                                                        #getter for title
        return self.__title  
    
    def get_author(self):                                                                                                                                       #getter for author
        return self.__author 
    
    def get_genre(self):                                                                                                                                        #getter for genre
        return self.__genre 
    
    def get_pub_year(self):                                                                                                                                     #getter for publication year
        return self.__publication_year
    
    def get_available(self):                                                                                                                                    #getter for available
        return self.__available   
     
    def loan_book(self):                                                                                                                                        #method to loan books
        if self.__available:                                                                                                                                    #if statement checking the available attribute
           self.__available = False                                                                                                                             #changing available attribute to False
           return True
        else:                                                                                                                                                   #else statement
            return False
    
    def return_book(self):                                                                                                                                      #method to return books                                                                                                                                  
        self.__available = True                                                                                                                                 #changing available attribute to True
    
    def display_details(self):                                                                                                                                  #method to display book details
        print(f"\nTitle: {self.get_title()}\nAuthor: {self.get_author()}\nGenre: {self.get_genre()}\nPublication Year: {self.get_pub_year()}\n")                #printing off book details using getters
        if self.get_available(): print("Availability: Available")
        else: print("Availability: Not Available")


def book_operations():                                                                                                                                          #defining function called book operations
    while True:                                                                                                                                                 #infinite while loop
        print("\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\n6. Exit")                                   #print statement listing the users options
        book_choice = input("Enter the function you'd like to perform (1-6): ")                                                                                 #obtaining a user input
        print("\n")                                                                                                                                             #new line for a little bit of formatting

        if book_choice == "1":                                                                                                                                  #if block determining if the user selected choice 1
            add_book()
        
        elif book_choice =="2":                                                                                                                                 #elif block determining if the user selected choice 2
            user_id = int(input("Enter your User ID: "))                                                                                                        #obtaining user input
            user_book = input("Enter the title you wish to check out: ").strip().title()                                                                        #obtaining user input
           
            if user_id in usersys.user_ids:
               
                if user_book in books:                                                                                                                          #if statement checking books dictionary
                    book_available = books[user_book].loan_book()                                                                                               #calling function from Book and setting a variable to it

                    if book_available:                                                                                                                          #if block checking book availability
                       usersys.user_ids[user_id].add_book(user_book)
                       print(f"{user_book} has been check out to user {user_id}.")                                                                              #print statement telling the user the book has been checked out to them
                  
                    else: print(f"{user_book} has already been checked out.")                                                                                   #else and print statement letting the user know the book has already been checked out

                else: print("Book not found.")                                                                                                                  #else and print statement telling the user the book was not found
           
            else: print("User ID not found.")
       
        elif book_choice == "3":                                                                                                                                #elif block determining if the user selected choice 3
            user_id = int(input("Enter your User ID: "))                                                                                                        #obtaining user input
            user_book = input("Enter the title you wish to return: ").strip().title()                                                                           #obtaining user input
            
            if user_id in usersys.user_ids:
                
                if user_book in books and not books[user_book].get_available():                                                                                 #if and statment to call the method return_book
                    books[user_book].return_book()  
                    usersys.user_ids[user_id].remove_book(user_book)    
                    print(f"User {user_id} had returned {user_book}")                                                
                
                else: print("Book is not checked out or the title was not found.")                                                                              #else statement telling the user the book could not be returned
            
            else: print("User ID not found.")
       
        elif book_choice == "4":                                                                                                                                #elif block determining if the user selected choice 4
            search_book()

        elif book_choice == "5":                                                                                                                                #elif block determining if the user selected choice 5
            list_books()

        elif book_choice == "6":                                                                                                                                #elif block determining if the user selected choice 6
            break

        else: print("Input not recognized please enter a number 1-4 for your choice.")                                                                          #else block and print statement letting the user know their input wasnt recognized


