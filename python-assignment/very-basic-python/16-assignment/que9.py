distance=float(input("enter the distance value:"))
mileage=float(input("enter the mileage value:"))
petrol_cost=float(input("enter the petrol_price value:"))

fuel_used = distance / mileage
total_cost = fuel_used * petrol_cost
print("Fuel used:", fuel_used, "liters")
print("Total cost:", total_cost)