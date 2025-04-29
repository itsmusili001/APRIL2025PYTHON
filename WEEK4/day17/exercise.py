#a program that enables the user to enter their name and phone number
#and give the user choices to add,update,delete and quit a program
#The program should also allow the user to store  the information in a dictionary and save  to a file.
def get_menu_choice():
    print()
    print("my adress book")
    print("*******************")
    print("1. search for a contact")
    print("2. add a contact")
    print("3. update a contact")
    print("4. delete a contact")
    print("5. quit the program")
    print()

    choice=int(input("Enter your choice: "))
    while choice<1 or choice>5:
        choice=int(input("Enter a valid choice(1-5): "))

    return choice
def search(contacts):
    name=input("Enter name of contact to search: ")
    
    print(contacts.get(name,"Contact not found"))
    

def add(contacts):
    name=input("Enter name: ")
    phone=input("Enter phone number: ")
    if name not in contacts:
        contacts[name]=phone
    else:
        print("Contact already exists")

def update(contacts):
    name=input("Enter name of contact to update: ")
    if name in contacts:
        phone=input("Enter new phone number to update: ")
        contacts[name]=phone
    else:
        print("name doesn't exist")
        
def delete(contacts):
    name=input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
    else:
        print("Contact not found")


def main ():
    contacts = {}
    choice = 0
    while choice != 5:
        choice = get_menu_choice()
        if choice == 1:
            search(contacts)
        elif choice == 2:
            add(contacts)
        elif choice == 3:
            update(contacts)
        elif choice == 4:
            delete(contacts)
main()