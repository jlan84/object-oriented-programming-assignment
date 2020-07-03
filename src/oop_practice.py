import string
from collections import Counter

class Dog():
    def _init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name, 'is now sitting')
    
    def roll_over(self):
        print(self.name, 'rolled over!')

class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def increment_number_served(self, n):
        self.number_served += n

               
    def describe_restaurant(self):
        print(f'{string.capwords(self.name)} {string.capwords(self.cuisine)} Cuisine')

    def open_restaurant(self):
        print(f'{string.capwords(self.name)} is now open')



# if __name__=='__main__':
#     lorenzos = Restaurant("lorenzo's", 'italian')
#     lorenzos.describe_restaurant()
#     lorenzos.open_restaurant()


# class User():
#     def __init__(self, first_name, last_name, birthday, hometown):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.birthday = birthday
#         self.hometown = hometown
#         self.login_attempts = 0
    
#     def add_attempt(self):
#         self.login_attempts += 1
    
#     def reset_attempts(self):
#         self.login_attempts = 0
    
#     def __str__(self):
#         return f"The user's name is {string.capwords(self.first_name)} {string.capwords(self.last_name)}\
# . Their birthday and hometown are {self.birthday} and {string.capwords(self.hometown)}.\
# They have attempted to log in {self.login_attempts} times."

#     def describe_user(self):
#         print(f"The user's name is {string.capwords(self.first_name)} {string.capwords(self.last_name)}\
# . Their birthday and hometown are {self.birthday} and {string.capwords(self.hometown)}")
    
#     def greet_user(self):
#         print(f'Hellow {string.capwords(self.first_name)}!')

# if __name__=='__main__':
#     user1 = User('Justin', 'Lansdale', '12/04/84', 'johannesburg')
#     user1.describe_user()
#     user1.greet_user()
#     user1.add_attempt()
#     print(user1)

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year, tank_size=0, mpg=0):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.tank_size = tank_size
        self.mpg = mpg
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print(f'The odemeter reads {self.odometer}')
    
    def drive(self, mileage):
        if mileage > 0:
            self.odometer += mileage
            self.tank_size -= mileage/self.mpg
            self.gas_left()
    
    def gas_left(self):
        print(f'There are {self.tank_size} gallons left in the tank')

class ElectricCar(Car):
    def __init__(self, make, model, year, wpm, bt_size):
        super().__init__(make,model, year) 
        self.bt_size = bt_size   
        self.battery = Battery(self.bt_size)
        self.wpm = wpm

    def drive(self, mileage):
        if mileage > 0:
            self.odometer += mileage
            self.battery.power_left -= mileage/self.wpm
            self.power()
    
    def gas_left(self):
        print(f'This car does not use gas')
    
    def power(self):
        print(f'The battery has {self.battery.power_left} kwh left')

class Battery():
    def __init__(self, size=70):
        self.size = size
        self.power_left = self.size
    
    def battery_size(self):
        print(f'The size of the battery is {self.size} kwh')





if __name__=='__main__':
    my_new_car = Car('audi', 'a4', 2016, 20, 40)
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()
    my_new_car.odometer = 100
    my_new_car.read_odometer()
    my_new_car.drive(100)
    my_new_car.read_odometer()
    tesla = ElectricCar('Tesla','Model X','2019',100, 100)
    print(tesla.get_descriptive_name())
    tesla.drive(100)

letlist = ['a','b','a']
print(Counter(letlist))