class Machinery:

    def __init__(self, year_of_production=None, lose_fuel_per_one_hour=None,
                weight_of_machinery_in_kg=None, machiene_mileage=None, wheel_type=None, fuel_type=None):
        self.year_of_production = year_of_production
        self.lose_fuel_per_one_hour = lose_fuel_per_one_hour
        self.weight_of_machinery_in_kg = weight_of_machinery_in_kg
        self.machiene_mileage = machiene_mileage
        self.wheel_type = wheel_type
        self.fuel_type = fuel_type

    @staticmethod
    def create_list_of_machinery(year_of_production: int, lose_fuel_per_one_hour: int,
                                   weight_of_machinery_in_kg: int, machine_mileage: int, wheel_type: bool, fuel_type: bool):
        machinery = [year_of_production, lose_fuel_per_one_hour, weight_of_machinery_in_kg, machine_mileage,
                       wheel_type, fuel_type]
        machinery_name = ['year_of_production', 'lose_fuel_per_one_hour', 'weight_of_machinery_in_kg',
                            'machiene_mileage', 'wheel_type', 'fuel_type']
        result_machinery = []
        for enum in range(6):
            if machinery[enum]:
                result_machinery.append(machinery_name[enum])
        return result_machinery


    def __del__(self):
        return

    def __str__(self):
        year_of_production = 'Year of production: {}\n'.format(self.year_of_production)
        lose_fuel_per_one_hour = 'Lose fuel per one hour: {}\n'.format(self.lose_fuel_per_one_hour)
        weight_of_machinery_in_kg = 'Weight of machinery in kg: {}\n'.format(self.weight_of_machinery_in_kg)
        machiene_mileage = 'Machiene mileage: {}\n'.format(self.machiene_mileage)
        price_of_ticket_in_usd = 'Price of ticket in usd: {}\n'.format(self.machinery_by_mileage_in_km)
        wheel_type = 'Wheel type: {}\n'.format(self.wheel_type)
        fuel_type = 'Fuel type: {}\n'.format(self.fuel_type)
        return year_of_production + lose_fuel_per_one_hour + weight_of_machinery_in_kg + machiene_mileage + price_of_ticket_in_usd + wheel_type + fuel_type


class RiderTraceMakerMachine(Machinery):

    def __init__(self, count_of_wheels=None):
        self.count_of_wheels = count_of_wheels

    def __del__(self):
        return

    def __str__(self):
        count_of_wheels = f'Count of wheels: {self.count_of_wheels}'
        return count_of_wheels


class SkiLiftMakerMachine(Machinery):

    def __init__(self, size_of_machine=None):
        self.size_of_machine = size_of_machine

    def __del__(self):
        return

    def __str__(self):
        size_of_machine = f'Size of machine: {self.size_of_machine}'
        return size_of_machine


class SkisTraceMakerMachine(Machinery):

    def __init__(self, hight_of_machine_in_meters=None):
        self.hight_of_machine_in_meters = hight_of_machine_in_meters

    def __del__(self):
        return

    def __str__(self):
        hight_of_machine_in_meters = f'Hight of machine in meters: {self.hight_of_machine_in_meters}'
        return hight_of_machine_in_meters