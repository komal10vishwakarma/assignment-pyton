class Vehicle:
    def __init__(self, vehicle_number, brand, rent_per_day):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.rent_per_day = rent_per_day

    @property
    def rent_per_day(self):
        return self._rent_per_day

    @rent_per_day.setter
    def rent_per_day(self, value):
        if value <= 0:
            raise ValueError("Rent per day must be greater than 0.")
        self._rent_per_day = value

    @rent_per_day.deleter
    def rent_per_day(self):
        del self._rent_per_day

    def display_vehicle(self):
        print(" Vehicle Details")
        print(f"Vehicle Number: {self.vehicle_number}")
        print(f"Brand: {self.brand}")
        print(f"Rent Per Day: {self.rent_per_day}")

    def calculate_rent(self, days):
        return self.rent_per_day * days


class Car(Vehicle):
    def __init__(
        self,
        vehicle_number,
        brand,
        rent_per_day,
        number_of_seats
    ):
        super().__init__(
            vehicle_number,
            brand,
            rent_per_day
        )
        self.number_of_seats = number_of_seats

    def display_vehicle(self):
        super().display_vehicle()
        print("Vehicle Type: Car")
        print(f"Number of Seats: {self.number_of_seats}")

    def calculate_rent(self, days):
        return super().calculate_rent(days)


class Bike(Vehicle):
    def __init__(
        self,
        vehicle_number,
        brand,
        rent_per_day,
        engine_cc
    ):
        super().__init__(
            vehicle_number,
            brand,
            rent_per_day
        )
        self.engine_cc = engine_cc

    def display_vehicle(self):
        super().display_vehicle()
        print("Vehicle Type: Bike")
        print(f"Engine CC: {self.engine_cc}")

    def calculate_rent(self, days):
        return super().calculate_rent(days)


vehicle_number = input("Enter Vehicle Number: ")
brand = input("Enter Brand: ")
rent_per_day = float(input("Enter Rent Per Day: "))

print("\n1. Car")
print("2. Bike")

vehicle_type = int(input("Enter Vehicle Type: "))

if vehicle_type == 1:
    number_of_seats = int(input("Enter Number of Seats: "))

    vehicle = Car(
        vehicle_number,
        brand,
        rent_per_day,
        number_of_seats
    )

elif vehicle_type == 2:
    engine_cc = int(input("Enter Engine CC: "))

    vehicle = Bike(
        vehicle_number,
        brand,
        rent_per_day,
        engine_cc
    )

else:
    print("Invalid Vehicle Type.")
    exit()

days = int(input("Enter Number of Rental Days: "))

vehicle.display_vehicle()

print(f"\nRental Days: {days}")
print(f"Total Rent: {vehicle.calculate_rent(days)}")