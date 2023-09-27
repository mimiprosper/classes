# import car_module
# from car_module import*

from car_module import Car, ElectricCar

# list to hold gas powered cars
gas_fleet = []
# list to hold electric powered cars
electric_fleet = []


# make 500 gas cars
for _ in range(20):
    gas_cars = Car('innoson', 'hummer bus', 2023)
    gas_fleet.append(gas_cars)

# make 250 electric powered cars
for _ in range(10):
    electric_cars = ElectricCar('tesla', 'G-series', 2020)
    electric_fleet.append(electric_cars)

# fill gas cars
for gas_car in gas_fleet:
    gas_cars.fill_tank()

# charge electric cars
for electric_cars in electric_fleet:
    electric_cars.charge()

print(f'Gas cars :{len(gas_fleet)}, Electric cars :{len(electric_fleet)}' )
