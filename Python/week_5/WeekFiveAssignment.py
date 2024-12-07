'''
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.
'''

class Car:
    def __init__(self, brand,make , model ,year , color ):
        self.brand = brand
        self.make= make
        self.model= model
        self.year= year
        self.color = color

    def move(self):
        return f" driving"
    
    def turn_on(self):
        return f" the car is on"
    
    def turn_off(self,):
        return f"The car is turned off"
    def display_info(self):
        return f"{self.brand} {self.make} {self.model} {self.year}"



car1 = Car("dodge","dodge Challenger", "hellcat","2023","black" )
cars= [
    Car("dodge","dodge Challenger", "hellcat","2023","black" ),
    Car ("chevrolet", "chevrolet Camaro", "ss", "2020", "red"),
    Car ("ford", "ford Mustang", "shelby gt500", "2019", "green"),
    Car("toyota", "toyota Supra", "gr", "2022", "white"),
    Car("nissan", "nissan GT-R", "nismo", "2021", "silver"),
    Car("audi", "audi R8", "v10 performance", "2023", "blue"),
    Car("mercedes", "mercedes-AMG GT", "black series", "2020", "yellow"),
    Car("bmw", "bmw M4", "competition", "2021", "orange"),
]
print(car1.brand)
print(car1.move())
print(cars[5].display_info())

class SportsCar(Car):
    def  __init__(self, brand, model ,year , color, horsepower,topspeed ):
        super().__init__(self, brand, model ,year , color )
        self.horsepower = horsepower
        self.topspeed = topspeed




#Activity 2: Polymorphism Challenge!

'''Create a program that includes animals or vehicles with the same action (like move()).
 However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗,
while Plane.move() prints "Flying" ✈️).'''


class Plane:
    def __init__(self, manufacturer, model, wingspan, max_speed, seating_capacity):
        self.manufacturer = manufacturer
        self.model = model
        self.wingspan = wingspan
        self.max_speed = max_speed
        self.seating_capacity = seating_capacity

    def plane_info(self,):
        return f"{self.manufacturer} {self.model}: {self.seating_capacity} seats, {self.max_speed} km/h max speed"
    def move(self,):
        return f" {self.manufacturer} {self.model} is flying"
    

boeing = Plane("Boeing", "737", 35.8, 876, 180)

print(boeing.plane_info())
print(boeing.move())
