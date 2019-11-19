class Customer():
    def __init__(self, name, address, telephone):
        #instance variables
        self.name = name
        self.address = address
        self.telephone = telephone

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getTelephone(self):
        return self.telephone

    def setTelephone(self, telephone):
        self.telephone = telephone




customer1 = Customer("mey755", "101 Main Street", "234-9078")
#always have the parenthesis because its a method
print(customer1.getName(),customer1.getAddress())
customer1.setTelephone("360789657")






    




