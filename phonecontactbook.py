import sys
def initial_phonebook():
    rows,cols = int(input("please enter the inital number of contact: ")),5
    
    phone_book = []
    print("phone_book")
    for i in range(rows):
        print("enter contact %d details in the following order: " %(i+1))
        print("NOTE: * indicate mandatory fields")
        print("..........................................................")
        temp = []
        for j in range(cols):
            #0:enter name of contact person
            #1:enter contact number 
            #2:enter e-mail id
            #3:enter date of birth
            #4:enter category (family,friends,work,others)
            if j == 0:
                temp.append(str(input("enter name*: ")))
                #check the name is empty r NOT and exit the operation
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("name is mandatory field. Process exit due blank feild")
                    
            if j == 1:
                temp.append(int(input("enter number*: ")))
                #checking not need because "int" will take care of it. if it empty it will return '0' 
                    
            if j == 2:
                temp.append(str(input("enter E-mail id: ")))
                #Even this feild is empty no error will be shown. 
                #fill with "None" will take place in empty feils
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
                    
            if j == 3:
                temp.append(str(input("enter date of birth(dd/mm/yy): ")))
                #even this field is empty no error will be shown.
                #"None" will take place in empty place
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
                    
            if j == 4:
                temp.append(str(input("enter category(family, friends,work,others): ")))
                #even this field is empty no error will be shown.
                #"None" will take place in empty place
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
                    
        phone_book.append(temp)
    print("****")
    print(phone_book)
    print('****')
    return phone_book
        
def menu():
    #we create this simple menu function
    print("**************************************************************")
    print("smartphone directory",flush = False)
    print("**************************************************************")
    print("you can now perform the following operation on this phonebook")
    print("1.Add new contact")
    print("2.Remove the existing contact")
    print("3.Delete all contact")
    print("4.Search for a contact")
    print("5.Display all contact")
    print("6.Exit phonebook")
    choice = int(input("please enter your choice1: "))
    return choice
    
def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter name*: ")))
        if i == 1:
            dip.append(int(input("enter number*: ")))
        if i == 2:
            dip.append(str(input("enter e-mail id: ")))
        if i == 3:
            dip.append(str(input("enter date of birth(dd/mm/yy): ")))
        if i == 4:
            dip.append(str(input("enter category (family,friends,work,others): ")))
    #in above it will appened each element to particrual contact 
    #and append to the details to every contact
    pb.append(dip)
   # print("value of pb",pb)
    for i in range(len(pb)):
        print(pb[i])
    return pb
    
def remove_contact(pb):
    #the function to remove the contact details from exit phonebook
    query = str(input("please enter the name of the contact you want to remove "))
    temp = 0
    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += -1
            print(pb.pop(i))
            print("this query has now been removed")
            return pb
            
    if temp == 0:
        print("you enter data is invalid \n please recheck and try again")
        return pb
        
def delete_all(pb):
    #function will simple delete all the contacts in phonebook and returns empty 
    return pb.clear()
    
def serach_contact(pb):
    #this function search the contact from exist contact list
    choice = int(input("enter search option:\n1.Name\n2.Number\n3.Email\n4.DOB\n5.category(family,friends,work,others)"))
    temp = []
    check = -1
    
    if choice == 1:
        query = str(input("please enter the name of the contact to search : "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])
                
    elif choice == 2:
        #this will sreach for contact based on number
        query = int(input("please enter the number of the contact to search: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])
    elif choice == 3:
        #this will search based on email id
        query = str(input("please enter the e-mail id: "))
        for i in range(len(pb)):
            if query == pb[i][2]:
                check = i
                temp.append(pb[i])
    elif choice == 4:
        #this will search based on the DOB
        query = str(input("please enter the DOB(in dd/mm/yy format Only of the contact need to search: "))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check = i
                temp.append(pb[i])
    elif choice == 5:
        #this will sreach based on category
        query = str(input("please enter the contact category: "))
        for i in range(len(pb)):
            if query == pb[i][4]:
                check = i
                temp.append(pb[i])
    else:
        print("invalid search ")
        return -1
        
    if check == -1:
        retun -1
    else:
        display_all(temp)
        return check

def display_all(pb):
    if not pb:
        #if this function is called after the delete_all then it have nothing to display_all
        print("list is empty")
        
    else:
        for i in range(len(pb)):
            print(pb[i])
            
def thank():
    print("******************************************************************")
    print("thank for using")
    print("phone book ended")
    print("******************************************************************")
    sys.exit("phonebook exited")
                
print("smartphone directory system ")
ch = 1
pb = initial_phonebook()
while ch in (1,2,3,4,5):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = remove_contact(pb)
    elif ch == 3:
        pb = delete_all(pb)
    elif ch == 4:
        d = serach_contact(pb)
        if d == -1:
            print("the cotact does not exit")
    elif ch == 5:
        display_all(pb)
    else:
        thank()
        
        
