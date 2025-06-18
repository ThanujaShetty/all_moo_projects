from abc import ABC,abstractmethod
class College(ABC):
    def __init__(self, name):
        self._name = name  # Protected member
        self.__location = "Unknown"  # Private member

    @abstractmethod
    def display_info(self):
        pass

    def get_name(self):
        return self._name

    def get_location(self):
        return self.__location

# Derived class representing a University
class University(College):
    def __init__(self, name, num_departments):
        super().__init__(name)
        self.__num_departments = num_departments  # Private member

    def display_info(self):
        print(f"{self._name} is a university with {self.__num_departments} departments.")

    def get_num_departments(self):
        return self.__num_departments

# Derived class representing a Community College
class CommunityCollege(College):
    def __init__(self, name, num_programs):
        super().__init__(name)
        self._num_programs = num_programs  # Protected member

    def display_info(self):
        print(f"{self._name} is a community college with {self._num_programs} programs.")

    def get_num_programs(self):
        return self._num_programs

# Function demonstrating polymorphism
def describe_college(college):
    college.display_info()

# Creating instances of the derived classes
university = University("ABC University", 10)
community_college = CommunityCollege("XYZ Community College", 30)

# Accessing private and protected members
print(f"Name of the university: {university.get_name()}")
print(f"Location of the community college: {community_college.get_location()}")
print(f"Number of programs in the community college: {community_college.get_num_programs()}")

# Using polymorphism to describe colleges
describe_college(university)
describe_college(community_college)