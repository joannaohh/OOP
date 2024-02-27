import CellPhoneClass as c

manufacturer = input('Enter manufacturer: ')
model_number = input('Enter model number: ')
r_price = input('Enter retail price: ')

phone = c.CellPhone(manufacturer, model_number, r_price)

phone.set_retail_price('999')

print(f"The phone's manufacturer: {phone.get_manufact()}")
print(f"The phone's model number: {phone.get_model()}")
print(f"The phone's retail price: ${phone.get_retail_price()}")