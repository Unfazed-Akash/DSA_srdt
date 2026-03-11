# Q5: Tyres in Dealerships
# Motorbike = 2 tyres, Car = 4 tyres, Truck = 10 tyres
# Accept counts, calculate tyres per type, total tyres, mean tyres per vehicle

motorbikes = int(input("Enter number of motorbikes: "))
cars = int(input("Enter number of cars: "))
trucks = int(input("Enter number of trucks: "))

motorbike_tyres = motorbikes * 2
car_tyres = cars * 4
truck_tyres = trucks * 10

total_vehicles = motorbikes + cars + trucks
total_tyres = motorbike_tyres + car_tyres + truck_tyres
mean_tyres = total_tyres / total_vehicles if total_vehicles > 0 else 0

print(f"\nMotorbike tyres : {motorbike_tyres}")
print(f"Car tyres       : {car_tyres}")
print(f"Truck tyres     : {truck_tyres}")
print(f"Total tyres     : {total_tyres}")
print(f"Mean tyres/vehicle: {mean_tyres:.2f}")
