from abc import ABC, abstractmethod

# Base class representing an electronic device
class Device(ABC):
    def __init__(self, brand):
        self._brand = brand  # Protected member
        self.__serial_number = "Unknown"  # Private member

    @abstractmethod
    def display_info(self):
        pass

    def get_brand(self):
        return self._brand

    def get_serial_number(self):
        return self.__serial_number

# Derived class representing a Smartphone
class Smartphone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.__model = model  # Private member

    def display_info(self):
        print(f"{self._brand} {self.__model} is a smartphone with serial number {self.get_serial_number()}.")

    def get_model(self):
        return self.__model

# Derived class representing a Laptop
class Laptop(Device):
    def __init__(self, brand, processor):
        super().__init__(brand)
        self._processor = processor  # Protected member

    def display_info(self):
        print(f"{self._brand} laptop with {self._processor} processor, serial number {self.get_serial_number()}.")

    def get_processor(self):
        return self._processor

# Function demonstrating polymorphism
def describe_device(device):
    device.display_info()

# Creating instances of the derived classes
smartphone = Smartphone("ABC", "XYZ123")
laptop = Laptop("XYZ", "Intel i7")

# Accessing private and protected members
print(f"Brand of the smartphone: {smartphone.get_brand()}")
print(f"Serial number of the laptop: {laptop.get_serial_number()}")
print(f"Processor of the laptop: {laptop.get_processor()}")

# Using polymorphism to describe devices
describe_device(smartphone)
describe_device(laptop)