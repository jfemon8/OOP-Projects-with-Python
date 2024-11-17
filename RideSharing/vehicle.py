from abc import ABC

class Vehicle(ABC):
    speed = {
        'car' : 100,
        'bike' : 80,
        'cng' : 60
    }
    
    def __init__(self, type, licence_plate, rate):
        super().__init__()
        self.type = type
        self.licence_plate = licence_plate
        self.rate = rate
    
class Car(Vehicle):
    def __init__(self, type, licence_plate, rate):
        super().__init__(type, licence_plate, rate)
        
class Bike(Vehicle):
    def __init__(self, type, licence_plate, rate):
        super().__init__(type, licence_plate, rate)
        
