class vehicle:
    def __init__(self,_vehicle_id,_base_rate):
        self._vehicle_id=_vehicle_id
        self._base_rate=_base_rate
    def display_details(self):
        return f"vehicle id :{self._vehicle_id},base rate :{self._base_rate}"
    def rental_charge(self):
        return 0.0
class car(vehicle):
    def __init__(self, _vehicle_id, _base_rate,num_seats):
        super().__init__(_vehicle_id, _base_rate)
        self.num_seats=num_seats
    def rental_charge(self):
        return self._base_rate*self.num_seats
class bike(vehicle):
    def __init__(self, _vehicle_id, _base_rate,bike_type):
        super().__init__(_vehicle_id, _base_rate)
        self.bike_type=bike_type
    def rental_charge(self):
        return self._base_rate*0.5
def calcualte_rental(vehicle):
    return vehicle.rental_charge() 
c=car("CAR001",100.0,4)  
b=bike("BIKE001",80.0,"scooter")
print(c.display_details())
print("car rentel charge",calcualte_rental(c))
print(b.display_details())
print("bike rental charge",calcualte_rental(b))


    
    