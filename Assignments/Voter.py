class Voter:
    def __init__(self,ID=None,name='',fhname='',age=0,address='',province='',vlisty=[],tlisty=[]):
        self._id = ID
        self._name = name
        self._fhname = fhname
        self._age = age
        self._adres = address
        self._prov = province
        self._vlisty,self.tlisty = vlisty,tlisty
        
        if self._id != None: 
            self._vlisty = [self._id,self._name,self._fhname,self._age,self._adres,self._prov]
            self.tlisty.append(self._vlisty)
            ally=[]
            for i in self.tlisty:
                ally.append(str(i)+'\n')
            with open('VoterTest.txt','w') as all:
                all.writelines(ally)  

    def addd(self):
        self._id = int(input('\nEnter your ID (must be four digits)*: '))
        while len(str(self._id)) != 4:
            print('Error! Invalid input, kindly enter a valid ID card number')
            self._id = int(input('Enter ID*: '))
    
        self._name = input('Enter your name: ')
        self._fhname = input('Enter your Husband/Father name: ')
        if not self._fhname:
            self._fhname = 'N/A'
        self._age = int(input('Enter your age: '))
        self._adres = input('Enter your address: ')
        self._prov = input('Enter your province: ')
        if self._id != None:
            self._vlisty = [self._id,self._name,self._fhname,self._age,self._adres,self._prov]
            self.tlisty.append(self._vlisty)
            ally=[]
            for i in self.tlisty:
                ally.append(str(i)+'\n')
            with open('VoterTest.txt','w') as all:
                all.writelines(ally) 

    def disp(self):
        print('')
        my_file = open("VoterTest.txt", "r")
        print(my_file.read())

    def find_v(self):
        x,vID,nam = int(input("\nEnter '0' if you want to search using ID, or Enter '1' if you want to search using Name: ")),'',''
        if x == 0:
            vID = input("Enter the ID of the voter you want to search: ")
            if len(str(vID)) <= 3:
                print('ID must have four digits.')
        elif x == 1:
            nam = input("Enter the Name of the voter you want to search: ")
        else: 
            print("Wrong input, please enter either '0' or '1'")
        print('')
        if len(str(vID))==4 or len(nam)>=1:
            filey = open("VoterTest.txt", "r")
            flag = 0
            index = 0
            for line in filey:  
                index += 1 
                if (nam or vID) in line:
                    flag = 1
                    print(line)
                    break 
                    
            if flag == 0: 
                if not nam:
                    print('ID',vID,'not Found.\n') 
                elif not vID:
                    print('Name',nam,'not found.\n')
            else: 
                print('\n')
     
            filey.close() 


    def quit(self):
        print('\nFile Saved and Closed! \n{:>15}'.format('Thank you'))

    def menu(self):
        print('\n\t\tMenu')
        print('{0:<15}    {1:>27}'.format('Add Voter' ,'{1}'))
        print('{0:<15}    {1:>24}'.format('Display All Voters','{2}'))
        print('{0:<15}    {1:>19}'.format('Find Voter (by Name/ID)','{3}'))
        print('{0:<15}    {1:>27}'.format('Quit','{4}'))

    def choose(self):
        choice = int(input('\nSelect 1 - 4: '))
        if choice == 1:
            self.addd()
        elif choice == 2:
            self.disp()
        elif choice == 3:
            self.find_v()
        else:
            self.quit()
        if choice != 4:
            return True
        else:
            return False
    
    def run(self):
        check = True
        while check:
            self.menu()
            check = self.choose()



def VoterTest():

    v1 = Voter(1024,'Laiba','Pardesi',20,'G-4','Punjab')
    v2 = Voter(2013,'Ali','N/A',23,'D-23','Sindh')
    driverr = Voter()
    driverr.run()

VoterTest()