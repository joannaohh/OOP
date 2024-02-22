import InsectClass as c

def main():
    mosquito = c.insect()
    housefly = c.insect()

    mosquito.flight_length()
    housefly.flight_length()

    print("Mosquito's flight length: ", mosquito.get_length())
    print("Housefly's flight length: ", housefly.get_length())

main()