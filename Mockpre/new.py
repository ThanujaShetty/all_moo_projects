class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"{self.brand} {self.model}"


# Derived class
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        # Calling the constructor of the base class
        super().__init__(brand, model)
        self.num_doors = num_doors

    def display_info(self):


        
        # Overriding the display_info method
        return f"{self.brand} {self.model} with {self.num_doors} doors"


# Creating instances of the classes
vehicle_instance = Vehicle(brand="Toyota", model="Camry")
car_instance = Car(brand="Ford", model="Mustang", num_doors=2)

# Accessing attributes and methods
print(vehicle_instance.display_info())  # Calls the display_info method in Vehicle class
print(car_instance.display_info())  # Calls the overridden display_info method in Car class

