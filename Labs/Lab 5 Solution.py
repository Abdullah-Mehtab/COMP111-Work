#Lab-5
#Task-1
'''
METHOD:
Classes are used to create user-defined data structures. Classes define functions called methods, which identify the behaviors and actions that an object created from the class can perform with its data.

INSTANCE VARIABLE:
An instance is an object that is built from a class and contains real data.An instance variable is a variable which is declared in a class but outside of constructors, methods, or blocks. Instance variables are created when an object is instantiated, and are accessible to all the constructors, methods, or blocks in the class.

CONSTRUCTOR:
Constructors are generally used for instantiating an object. The task of constructors is to initialize (assign values) to the data members of the class when an object of the class is created. In Python the __init__() method is called the constructor and is always called when an object is created.

Accessor Method:
This method is used to access the state of the object i.e, the data hidden in the object can be accessed from this method. However, this method cannot change the state of the object, it can only access the data hidden. We can name these methods with the word get.

Mutator Method:
This method is used to mutate/modify the state of an object i.e, it alters the hidden value of the data variable. It can set the value of a variable instantly to a new value. This method is also called as update method. Moreover, we can name these methods with the word set. 
'''
#Task-2
print('\nTask Two\n')
import math

class Ball:
    def __init__(self,radius):
        self.radius = radius
    
    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return 4 * math.pi * self.radius**2

    def volume(self):
        return 4 * math.pi * self.radius**3 / 3

def task2():
    rad = eval(input("Enter radius: "))
    ball = Ball(rad)
    area = ball.surfaceArea()
    vol = ball.volume()
    print("\nSurface area: "+str(area)+'\nVolume: '+str(vol))
task2()

#Task-3
print('\nTask Three\n')
class Flower:

    # Constructor
    def __init__(self, name, petals, price):
        self._name = str(name)
        self._petals = int(petals)
        self._price = float(price)


    # Accessors
    def get_name(self):
        return self._name

    def get_petals(self):
        return self._petals

    def get_price(self):
        return self._price

    def Show(self):
        print('Displaying all the attributes of class Flower')
        print('Flowers Name: ',self._name)
        print('Flowers Petal: ',self._petals)
        print('Flowers Price: ',self._price)

    # Mutators
    def set_name(self, name):
        self._name = name

    def set_petals(self, petals):
        self._petals = petals

    def set_price(self, price):
            self._price = price

    def UpdatePetals(self, petals, task):
        if task == "Add":
            self._petals += petals
        elif task == "less":
            self._petals -= petals

def task3():
    myFlower = Flower('Rose',20,50)
    myFlower.UpdatePetals(10,'Add')    # Add 10 + 20 and update the petals 
    myFlower.UpdatePetals(15,'less')   # subtract 30 - 15 and update the petals myFlower.Show() 
    myFlower.Show()                    # Display all the attributes of flower
task3()

#Task-4
print('\nTask Four\n')
class Car:

    #constructor
    def __init__(self, efficiency, fuel=0):
        self._fuel = fuel
        self._efficiency = efficiency


    #accessors
    #return efficiency
    def efficiency(self):
        return self._efficiency

    #returns Fuel Level
    def getGasLevel(self):
        return self._fuel


    #mutators
    #adding fuel
    def addfuel(self, addfuel):
        self._fuel += addfuel

    #fuel after drive
    def drive(self, distance):
        self._fuel = ((self._efficiency * self._fuel) - distance) / self._efficiency  #returns reduceded fuel tank after driven distance

       
def main():

    #Efficiency
    myHybrid = Car(50)    #50 miles per gallon
    print('Car Efficiency: ',myHybrid.efficiency())
    print('Current fuel: ',myHybrid.getGasLevel())

    #Adding Fuel
    myHybrid.addfuel(20)
    print('Fuel after adding 20 gallons: ',myHybrid.getGasLevel())    # Tank 20 gallons

    #Drive
    myHybrid.drive(100)    # Drive 100 miles
    print('Fuel After driving 100 miles: ',myHybrid.getGasLevel())         # Print fuel remaining

main()