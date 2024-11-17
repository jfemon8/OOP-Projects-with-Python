from user import Driver, Rider
from vehicle import Car, Bike
from ride import Ride, RideMatching, RideRequest, RideShare

uthao = RideShare('Uthao')

emon = Rider('Emon', 'emon@gmail.com', 123, 'Barishal', 2500)
uthao.add_rider(emon)
sami = Driver('Sami', 'sami@gmail.com', 456, 789, 'Faridpur')
uthao.add_driver(sami)
emon.request_ride(uthao, 'Dhaka', 'car')
emon.show_current_ride()
sami.reach_destination(emon.curren_ride)

