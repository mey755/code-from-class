import random

class MSDie(): 
    # constructor method, the init, function of the class get called
    #provide default values if someone forget to put it in; sides=6
    def __init__(self, sides):
        # self is indictive of the object
        self.sides = sides
        self.value = 1
    
    def roll(self):
        self.value = random.randint(1,self.sides)
    #method provided in the class of the current value facing up in the class. Retain what we know, what they know.
    #class is a collection of functions
    def getValue(self):
        #sending back the thing that called it the bit of data. Programative interfaces, they get information
        return self.value

    def getSides(self):
        return self.sides
    
    def setValue(self,value):
        self.value = value

    def setSides(self,sides):
        self.sides = sides

dieBag = []

for i in range(7):
    sides = int(input("How many sides? "))
    dieBag.append(MSDie(sides))

 # die is an MSDie object in the second loop
for die in dieBag:
    #ope/close parenthesis b/c it's a method
    die.roll()
    print(die.getValue())

for die in dieBag:
    die.setSides(10)
    die.setValue(2)
    print(die.getValue(), die.getSides())

#die1 is the object of the class, MSDie
# die1 = MSDie(6)

# for i in range(10):
#     die1.roll()
#     print(die1.value)
# die1.value = 3
# print(die1.sides)
# print(die1.value)
# die2 = MSDie(100)
