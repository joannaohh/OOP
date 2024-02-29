import CarClass as c

car = c.car(2017, 'Lexus')

for i in range(5):
    car.accelerate()
    print(f"Current speed: {car.get_speed()}")

for j in range(5):
    car.brake()
    print(f"Current speed: {car.get_speed()}")
