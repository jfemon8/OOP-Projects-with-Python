from datetime import datetime
from vehicle import Bike, Car

class RideShare:
    def __init__(self, company_name):
        self.company_name = company_name
        self.drivers = []
        self.riders = []
        self.rides = []
        
    def add_driver(self, driver):
        self.drivers.append(driver)
        
    def add_rider(self, rider):
        self.riders.append(rider)
        
    def __str__(self):
        return f'Company Name: {self.company_name}. We have {len(self.drivers)} expart drivers with {len(self.riders)} satisfied riders.'

class Ride:
    def __init__(self, start_location, end_location, vehicle):
        self.start_location = start_location
        self.end_location = end_location
        self.start_time = None
        self.end_time = None
        self.rider = None
        self.driver = None
        self.estimated_fare = None
        self.vehicle = vehicle
        
    def set_driver(self, driver):
        self.driver = driver
        
    def set_rider(self, rider):
        self.rider = rider
        
    def start_ride(self):
        self.start_time = datetime.now()
        
    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
        
    def calculate_fare(self, distance, vehicle):
        fare_rate ={
            'car' : 35,
            'bike' : 30,
            'cng' : 25
        }
        self.estimated_fare = distance * fare_rate.get(vehicle)
        
    def __repr__(self):
        return f'Ride from {self.start_location} to {self.end_location}.\nRider: {self.rider.name}\nDriver: {self.driver.name}\nTotal fare: {self.estimated_fare}'
    
class RideRequest:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location
        
class RideMatching:
    def __init__(self, drivers):
        self.available_drivers = drivers
        
    def find_driver(self, ride_request, vehicle_type):
        if len(self.available_drivers)>0:
            print('Looking for drivers . . .')
            driver = self.available_drivers[0]
            vehicle = None
            if vehicle_type == 'Car':
                vehicle = Car('Car', 'ABC123', 100)
            elif vehicle_type == 'Bike':
                vehicle = Bike('Bike', '789XYZ', 150)
            ride = Ride(ride_request.rider.current_location, ride_request.end_location, vehicle)
            driver.accept_ride(ride)
            return ride
