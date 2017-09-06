class Bike(object):
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print(self.price)
        print(self.max_speed)
        print(self.miles)
        return self
    
    def ride(self):
        print("Riding")
        self.miles += 10
        return self
    
    def reverse(self):
        print("Reversing")
        self.miles -= 5
        if (self.miles < 0):
            self.miles = 0
        return self

i_want_to_ride_my = Bike(1000,"50mph")
rosie = Bike(500,"100mph")
mudflap = Bike(25,"1000mph")

i_want_to_ride_my.ride().ride().ride().reverse().displayInfo()
rosie.ride().ride().reverse().reverse().displayInfo()
mudflap.reverse().reverse().reverse().displayInfo()
