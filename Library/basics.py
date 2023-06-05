class Vechical:
    
    companyName = "Maruthi Suzuki"
    
    def __init__(self, name, color, maxSpeed, serviceInterval,isSuperBike=False):
        self.name = name
        self.color = color
        self.maxSpeed = maxSpeed
        self.serviceInterval = serviceInterval
        self.isSuperBike = isSuperBike

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


v1 = Vechical(name="Yamaha R1", color="Blue", maxSpeed=300, serviceInterval=1000)
v2 = Vechical("Kawasaki Ninja zx10r", "Black", 190 , 500, True)

print(v1.companyName)
print(v2.companyName)

Vechical.companyName = "Audi"

print(v1.companyName)
print(v2.companyName)