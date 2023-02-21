# Name: Abdullah Mehtab, Roll No#: 241607845
# Assignment-1 
O = '-'*10
print(O,'Assignment One',O,'\n')
# Task-1
print(O,'Task One',O,'\n')
print('Multiplication of Matrixes\n')
# Program to multiply two matrices
# Inputting the order of the matrices to check if can be multiplied or not
R1 = int(input("Enter the number of rows for Matrix A: "))
C1 = int(input("Enter the number of columns for Matrix A: "))
R2 = int(input("\nEnter the number of rows for Matrix B: "))
C2 = int(input("Enter the number of columns for Matrix B: "))

if C1 == R2:                               #Column of first matrix must be equal to Row
    print("\nMatrices can be multiplied.")  #Column of first matrix is equal to Row of second matrix
elif C1 != R2:
    print("\nMatrix cannot be multiplied.")   #Column of first matrix is not equal to Row
    while C1 != R2:
        print('\nColumn of Matrix A should be equal to Rows of Matrix B\nPlease Enter again')
        C1 = int(input("Enter the number of columns for Matrix A: "))
        R2 = int(input("Enter the number of rows for Matrix B: "))
    print('\nNow Matrices can be multiplied.')
# Initializing and inputting the Matrix A
Matrix_A = []
print("\nEnter the elements for Matrix A row-wise: ")  #Inputting the Matrix
for i in range(R1):          # A for loop for row entries
    a = []
    for j in range(C1):      # A for loop for column entries
         a.append(int(input()))
    Matrix_A.append(a)
#Printing the matrix A
print('\nMatrix A =')
for i in range(R1):
    for j in range(C1):
        print(Matrix_A[i][j],end = " ")
    print()

# Initializing and inputting the Matrix B
Matrix_B = []
print("\nEnter the elements for Matrix B row-wise: ")  #Inputting the Matrix
for i in range(R2):          # A for loop for row entries
    b = []
    for j in range(C2):      # A for loop for column entries
         b.append(int(input()))
    Matrix_B.append(b)
  
#Printing the Matrix B
print('\nMatrix B =')
for i in range(R2):
    for j in range(C2):
        print(Matrix_B[i][j],end = " ")
    print()

#Making a blank resultant Matrix
Matrix_C = []
for i in range(R1):
    emp = []
    for j in range(C2):
        emp.append(0)
    Matrix_C.append(emp)

#Multiplying the Matrices
print("\nMultiplying Matrx A and Matrix B and storing answer in Matrix C\n")
print("Answer (Matrix C) = ")
# iterating by row of A
for i in range(len(Matrix_A)):
    # By column by B
    for j in range(len(Matrix_B[0])):
        # By rows of B
        for k in range(len(Matrix_B)):
            Matrix_C[i][j] += Matrix_A[i][k] * Matrix_B[k][j]
for r in Matrix_C:
    print(r)

# Task Two
print('\n\n'+O,'Task Two',O,'\n')
print("Tower of Hanoi (Transering disct from rod to rod\n")
#Defining the Recursive function
def TowerOfHanoi(n , rod_1, rod_2, rod_3): #There are n discs and three rods so disk argument 'n' and 3 arguments for rods
    if n == 1:
        print("Move disk 1 from rod",rod_1,"to rod",rod_2)
        return
    TowerOfHanoi(n-1, rod_1, rod_3, rod_2)
    print("Move disk",n,"from rod",rod_1,"to rod",rod_2)
    TowerOfHanoi(n-1, rod_3, rod_2, rod_1)
# Inputting and Running the code
n = int(input("Enter the number of discs: "))
TowerOfHanoi(n, 'A', 'C', 'B') # A, C, B are the name of rods

# Task Three
print('\n\nTask Three\n')
print("Defining a Phonebook dictionary")
# Aid taken from https://www.geeksforgeeks.org/implementing-a-contacts-directory-in-python/
import sys
from types import DynamicClassAttribute
diff = '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
def initial_phonebook():
    rows, cols = int(input("Enter initial number of contacts: ")), 4
    # We are collecting the initial number of contacts the user wants to have in the
    # phonebook already. User may also enter 0 if he doesn't wish to enter any.
    phone_book = []
    dicc = {}
    for i in range(rows):
        print("\nEnter contact "+str(i+1)+" details:")
        print("NOTE: * indicates mandatory fields")
        print(diff)
        temp = []
        for j in range(cols):  
        # J amoung of columns for things 
        # such as name, number, e-mail id, dob, category etc
            if j == 0:
                name = str(input("Enter name*: "))
                if name == '' or name == ' ':
                    sys.exit("Name is a mandatory field. Process exiting due to blank field...")
                    # This will exit the process if a blank field is encountered.
                     
            if j == 1:
                temp.append(int(input("Enter number: ")))
                # No need to check using condition since int value cannot accept a blank as that counts as a string.
                # So process automatically exits without us using the sys package.
            
            if j == 2:
                temp.append(str(input("Enter address: ")))
                if temp[j-1] == '' or temp[j-1] == ' ':
                    temp[j-1] = None
            
            if j == 3:
                temp.append(str(input("Enter e-mail address: ")))
                if temp[j-1] == '' or temp[j-1] == ' ':
                    temp[j-1] = None
                     

        dicc.update({name:temp})
     
    print('\nCurrent Phone-book:')
    print(dicc)
    return dicc
 
def menu():
    input('\nPress ENTER to continue.\n')
    print(diff)
    print("\t\t\tPHONE-BOOK DIRECTORY")
    print(diff)
    print("You can now perform the following operations on this phonebook\n")
    print("1. Display all the contacts")
    print("2. Add a new contact")
    print("3. Search for a contact")
    print("4. Delete an existing contact")
    print("5. Exit phonebook")
    # Out of the provided 5 choices, user needs to enter any 1 choice among the 6
    choice = int(input("Please enter your choice: "))   
    return choice
 
def add_contact(pb):
    dip = []
    print('Adding new contact\n')
    for i in range(4):
        if i == 0:
            name = (str(input("Enter name*: ")))
        if i == 1:
            dip.append(int(input("Enter number: ")))
        if i == 2:
            dip.append(str(input("Enter address: ")))
        if i == 3:
            dip.append(str(input("Enter email: ")))
    pb.update({name:dip})
    return pb
 
def remove_existing(pb):
    query = str(input("\nPlease enter the name of the contact you wish to remove: "))     
    temp = 0   
    if query in pb.keys():
            temp += 1
            # Temp will be incremented & it won't be 0 anymore in this function's scope
            print("{'"+query+"':",pb.pop(query),"}")
            # The pop function removes entry at that index
            print("This contact has now been removed")
             
            return pb
    if temp == 0:
        # Now if at all any case matches temp should've incremented but if otherwise,
        # temp will remain 0 and that means the query does not exist in this phonebook
        print("Sorry, you have entered an invalid query. Please recheck and try again later.")
         
        return pb
 
def search_existing(pb):
    # This function searches for an existing contact and displays the result  
    print('')
    # This will execute for searches based on contact name
    query = str(input("Please enter the name of the contact you wish to search: "))
    if query in pb.keys():
        print("Displaying the contact that was searched for\n")
        print("{'"+query+"':",pb[query],"}")
        # we're just returning a index value wiz not -1 to calling function just to notify
        # that the search worked successfully
    else: 
        return -1
 
def display_all(pb):
    if not pb:
        print("Phonebook is empty: []")
    else:
        print(pb)

def exitt():
    print('\n'+diff+'\nThank you for using our Phonebook.\n'+diff)
    sys.exit("Goodbye.")
 
print(diff)
print("Hello user, welcome to the Phonebook")
print("You may now proceed.")
print(diff)

ch = 1
pb = initial_phonebook()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        print('\nAll contacts: \n')
        pb_1 = display_all(pb)
    elif ch == 2:
        pb = add_contact(pb)
    elif ch == 3:
        d = search_existing(pb)
        if d == -1:
            print("The contact does not exist. Please try again")
    elif ch == 4:
        remove_existing(pb)
    else:
        exitt()
