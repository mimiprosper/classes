class Car:
    
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.fuel_capacity = 15
        self.fuel_level = 10

    # def __str__(self) -> str:
    #     return f'{self.make} {self.model} {self.year} model'

    def drive(self):
        print('the car is moving')

    def fill_tank(self):
        if self.fuel_level == self.fuel_capacity:
            print('fuel tank is full!!!')
        else:
            print('fuel tank empty')

    def update_fuel_level(self, new_level):
        if new_level <= self.fuel_capacity:
            #self.fuel_level = new_level
            print(f'tank within capacity {new_level} liters')
        else:
            print('The tank cannot hold that capacity')

    def add_fuel(self, amount):
        new_level = self.fuel_level + amount
        if new_level < self.fuel_capacity:
            print(f'level is now {new_level} liters')
        elif new_level == self.fuel_capacity:
            self.fill_tank()
        else:
            print('The tank cannot hold that much')

# creating an object of a class Car
my_car = Car('toyota', 'venza', '2023')
print(my_car.year, my_car.model, my_car.make)

# calling the method of the class Car
# my_car.fill_tank()
# print(my_car.fuel_level)

my_car.update_fuel_level(10)
my_car.add_fuel(1)
