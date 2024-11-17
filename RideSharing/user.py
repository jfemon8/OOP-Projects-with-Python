from abc import ABC, abstractmethod
from ride import *

class User(ABC):
    def __init__(self, name, email, nid):
        super().__init__()
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0
        
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_balance):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = initial_balance
        self.curren_ride = None
        
    def display_profile(self):
        print(f'Name: {self.name} and Email: {self.email}')
        
    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print('Invalid amount!')
            
    def update_location(self, new_location):
        self.current_location = new_location
    
    def request_ride(self, ride_sharing, destination, vehicle_type):
        ride_request = RideRequest(self, destination)
        ride_matching = RideMatching(ride_sharing.drivers)
        ride = ride_matching.find_driver(ride_request, vehicle_type)
        self.curren_ride = ride
        distance = len(self.current_location) + len(destination)
        ride.calculate_fare(distance, vehicle_type) #change here
        ride.rider = self
        print('We got a ride!!!')
    
    def show_current_ride(self):
        print(self.curren_ride)
        
class Driver(User):
    def __init__(self, name, email, nid, licence, current_location):
        super().__init__(name, email, nid)
        self.licence = licence
        self.current_location = current_location
        self.wallet = 0
        
    def display_profile(self):
        print(f'Driver name: {self.name}')
        
    def accept_ride(self, ride):
        ride.set_driver(self)
        ride.start_ride()
    
    def reach_destination(self, ride):
        ride.end_ride()
