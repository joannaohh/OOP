import InsectClass as c

def main():
    mosquito = c.insect(2, 4, 'Mosquito')
    housefly = c.insect(2, 4, 'Housefly')

    mosquito.flight_length()
    housefly.flight_length()

    print(f"The {mosquito.get_name()} can fly up to {mosquito.get_length()}")
    print(f"The {housefly.get_name()} can fly up to {housefly.get_length()}")

main()