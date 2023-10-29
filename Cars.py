class Vehicle:
    def type_of_vehicle(self):
        print("I am default vehicle method")

    def fuel_type(self):
        print("Petrol or Diesel or ELectric")

    def max_speed(self):
        print("Max speed maybe between 180-220")

class Ferrari(Vehicle):
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        print("Max speed 350")

class BMW(Vehicle):
    def fuel_type(self):
        print("Diesel")

    def max_speed(self):
        print("Max speed is 240")


class Mercedes(Vehicle):

    def type_of_vehicle(self):
        print("I am Mercedes")

ferrari = Ferrari()
bmw = BMW()
mercedes = Mercedes()

# iterate objects of same type
for car in (ferrari, bmw):
    # call methods without checking class of object
    car.fuel_type()
    car.max_speed()

bmw.type_of_vehicle()
ferrari.type_of_vehicle()
mercedes.type_of_vehicle()

ferrari.max_speed()
mercedes.max_speed()
ferrari.fuel_type()
mercedes.fuel_type()

