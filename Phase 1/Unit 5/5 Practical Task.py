# Implement an add_contact() function that appends a new dictionary to the list

# Implement a search_contact(name) function that searches by name and returns the matching dictionary (or None if not found)

#Implement a delete_contact(name) function that removes a contact by name

#Implement a view_all() function that displays all contacts in a formatted layout

#Use a while loop menu to let the user choose an action (1=Add, 2=Search, 3=Delete, 4=View All, 5=Exit)

# options
def options():
    print('choose option below')
    print('1 : View all contacts')
    print('2 : Add new contact')
    print('3 : Search existing contact')
    print('4 : Update existing contact')
    print('5 : Delete contact permanetly')
    option = input('whats your option: ')
    
    if option == '1':
        print('viewing all existing contacts')
        view_all()
    elif option == '2':
        print('Add new contact')
        add_contact()
    elif option == '3':
        print('search a contact')
        search_contact()
    elif option == '4':
        print('search contact: ')
        search_contact()
    elif option == '5':
        print('Delete contact')
        drlete_contact()
    else:
        print('incorect option, try again: ')
        options()
    

contacts = []
    
#Add ne contact function
def add_contact():
    name = input("enter name: ").strip()
    phone = input("enter phone: ").strip()
    email = input("enter email: ").strip()
    
    new_contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(new_contact)
    print(f'{name} was added to contacts')
    
    exit()



#view all contacts
def view_all():
    print('here are all existing contacts')
    for view_all in contacts:
        print(view_all)
    
    exit()
 
 
# search contact function
def search_contact():
    search_name = input().strip()
    print(f'enter contact name: {search_contact}')
    
    for contact in contacts
    
# update function
#def update_contact():
    
    
# delete function
#def delete_contact():
   
#exit function
def exit():
    print('enter 6 to exit')
    exit = input().strip
    if exit == '6':
        options()
    else:
        print('invalid option')
        options()

   
if len(contacts) <= 0 :
    print('no contacts yet, add one below')
    add_contact()
else:
    options()
    