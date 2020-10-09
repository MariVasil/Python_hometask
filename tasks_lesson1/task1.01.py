# Part I
param1 = 34
param2 = 48430
param3 = 56.89
param4 = "Hello!"

print(param1)
print(param2)
print(param4)

sum13 = param1 + param2 + param3
print(sum13)

# Part II
address_city = input("Введите город: ")
address_street = input("Введите улицу: ")
address_house_number = input("Введите номер дома: ")
address_house_floors = int(input("Введите количество этажей в доме: "))

print(f"Ваш адрес: город {address_city}, улица {address_street}, дом {address_house_number}")
print(f"Количество этажей в вашем доме: {address_house_floors}")
