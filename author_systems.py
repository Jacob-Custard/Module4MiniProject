#author_systems is a module to manage all classes and functions related to authors in the advanced library managment system.

def add_author():                                                                                                                                               #defining a funciton to add an author to the class
    name = input("Enter the name of the author you wish to add: ").title()                                                                                      #obtaining user input
    birthday = input("Enter the author's birthday (MM/DD/YYYY): ")                                                                                              #obtaining user input
    hometown = input("Enter the author's hometown: ")                                                                                                           #obtaining user input
    first_book = input("Ente the author's first published book: ")                                                                                              #obtaining user input
    name2 = name                                                                                                                                                #second name variable set to the original user input
    name = Author(name2, birthday, hometown, first_book)                                                                                                        #establishing an object of class Atuhor using the user inputs
    authors[name2] = name                                                                                                                                       #adding the class object to a dictionary using the author name as the key


def list_authors():                                                                                                                                             #defining function to list the all authors
    for author in authors:                                                                                                                                      #for loop to cycle through the 'authors' dictionary
        print (author)                                                                                                                                          #print statement to print off each author

authors = {}                                                                                                                                                    #setting up an empty dictionary to hold the authors

class Author:                                                                                                                                                   #establishing a class called author
    def __init__(self, name, birthday, hometown, first_book):                                                                                                   #initializng the class
        self.__name = name                                                                                                                                      #private attribute
        self.__birthday = birthday                                                                                                                              #private attribute
        self.__hometown = hometown                                                                                                                              #private attribute
        self.__first_book = first_book                                                                                                                          #private attribute

    def get_name(self):                                                                                                                                         #getter for name
        return self.__name
    
    def get_bday(self):                                                                                                                                         #getter for birthday
        return self.__birthday
    
    def get_hometown(self):                                                                                                                                     #getter for hometown
        return self.__hometown
    
    def get_first_book(self):                                                                                                                                   #getter for first book
        return self.__first_book
    
    def display_details(self):                                                                                                                                  #method to display author details
        print(f"\n{self.get_name()}:\nBorn - {self.get_bday()}\nHometown - {self.get_hometown()}\nFirst Published Book - {self.get_first_book()}")              #print statement to print off details in a formatted way
    
        
def author_operations():                                                                                                                                        #defining a function for author operations
    while True:                                                                                                                                                 #setting up an infinite while loop so the user can cycle through choices
        print("\n1. Add a new author\n2. View author details\n3. Display all authors\n4. Exit")                                                                 #print statement list the functions the user can choose from
        author_choice = input("\nEnter the function you'd like to perform (1-4): ")                                                                             #variable author_choice is a user input

        if author_choice == "1":                                                                                                                                #if block determining if the user selected choice 1
            add_author()
        
        elif author_choice =="2":                                                                                                                               #elif block determining if the user selected choice 2
            author = input("Enter the name of the author you wish to see the details for: ").strip().title()                                                    #obtaining user input
            authors[author].display_details()                                                                                                                   #using user input to call a method from class Author

        elif author_choice == "3":                                                                                                                              #elif block determining if the user selected choice 3
            list_authors()

        elif author_choice == "4":                                                                                                                              #elif block determining if the user selected choice 4
            break

        else: print("Input not recognized please enter a number 1-4 for your choice.")                                                                          #else block and print statement letting the user know their input wasnt recognized



