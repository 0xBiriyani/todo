class Vechical:
    
    companyName = "Maruthi Suzuki"
    
    def __init__(self, name, color, maxSpeed, serviceInterval,isSuperBike=False):
        self.name = name
        self.color = color
        self.maxSpeed = maxSpeed
        self.serviceInterval = serviceInterval
        self.isSuperBike = isSuperBike
        self.tag = f"{self.name} {self.color} Rocks"
        
        

    def isOverSpeed(self, speed):
        if speed > self.maxSpeed:
            return True
        else:
            return False
        
    def isServiceDue(self, currentReading):
        if currentReading > self.serviceInterval:
            return True
        else:
            return False

    
    def updateColor(self, newColor):
        self.color = newColor
        self.tag = f"{self.name} {self.color} Rocks"


v1 = Vechical(name="Yamaha R1", color="Blue", maxSpeed=300, serviceInterval=1000)
v2 = Vechical("Kawasaki Ninja zx10r", "Black", 190 , 500, True)




v1.updateColor("Red")
print(v1.color)
print(v1.tag)
v1.tag = "Something Wrong"
print(v1.tag)