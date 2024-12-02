#user_systems is a module to manage all classes and functions related to users in the advanced library managment system.

def add_user():
    try:                                                                                                                                                        #try block for error handling
        user_id = int(input("Enter new User ID number: ").strip())                                                                                              #obtaining user input
        user_name = input("Enter name of user: ")                                                                                                               #obtaining user input
        user_id2 = user_id                                                                                                                                      #setting new variable equal to original user input
        user_id = Users(user_name, user_id2)                                                                                                                    #setting up an object of Users
        user_ids[user_id2] = user_id                                                                                                                            #appending class object to user_ids list
    except ValueError:                                                                                                                                          #except block for ValueError
        print("User ID number must be a whole number.")                                                                                                         #print statement to inform the user there was an error

    
def list_all_users():                                                                                                                                           #function to list all user in user_ids dictionary
    for user in user_ids:
        print(user)

user_ids = {}                                                                                                                                                   #empty dictionary

class Users:                                                                                                                                                    #establishing class called User
    def __init__(self, name, library_id):                                                                                                                       #initiating class
        self.__name = name                                                                                                                                      #private attribute
        self.__library_id = library_id                                                                                                                          #private attribute
        self.loaned_books = []                                                                                                                                  #empty list

    def get_name(self):                                                                                                                                         #getter for name
        return self.__name

    def get_id(self):                                                                                                                                           #getter for library id
        return self.__library_id  
    
    def user_details(self):                                                                                                                                     #method to display user details
        print(f"{self.get_name()}: User ID - {self.get_id()}\nBooks currently checkout to this user:")                                                          #print statement to format user details and present them to the user
        for book in self.loaned_books:                                                                                                                          #for loop to print all the books in loaned_books list
            print (book)

    def add_book(self, book):                                                                                                                                   #method to add a book to loaned books list
        self.loaned_books.append(book)                                                                                                                          #appeding book to list
    
    def remove_book(self, book):
        self.loaned_books.remove(book)

def user_operations():                                                                                                                                          #defining funciton for user operations
    while True:                                                                                                                                                 #establishing infinite while loop
        print("\n1. Add a new user\n2. View user details\n3. Display all users\n4. Exit")                                                                       #print statement listing the available options
        user_op_choice = input("Enter function you'd like to perform (1-4): ")                                                                                  #obtaining user input
        
        if user_op_choice == "1":                                                                                                                               #if block determining if the user selected choice 1
            add_user()
        
        elif user_op_choice =="2":                                                                                                                              #elif block determining if the user selected choice 2
            user_id = int(input("Enter the User ID you'd like to view: "))                                                                                      #obtaining user input
            if user_id in user_ids:                                                                                                                             #checking if user input is in user_ids list using if statement
                user_ids[user_id].user_details()                                                                                                                #calling user_details method

            else: print("User ID not found")                                                                                                                    #else and print statement telling the user that the user input was not found

        elif user_op_choice == "3":                                                                                                                             #elif block determining if the user selected choice 3
            list_all_users()

        elif user_op_choice == "4":                                                                                                                             #elif block determining if the user selected choice 4
            break

        else: print("Input not recognized please enter a number 1-4 for your choice.")                                                                          #else block and print statement letting the user know their input wasnt recognized
