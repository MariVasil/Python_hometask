product_quantity = int(input("Сколько товаров вы хотите ввести: "))

product_keys = ["название", "цена", "количество", "единица измерения"]
product_list = []

for i in range(product_quantity):
    product_specifications = {}
    print(f"Введите характеристики {i + 1}-го товара")
    for key in product_keys:
        product_specifications[key] = input(f"{key}: ")
    product_list.append((i + 1, product_specifications))
# print(product_list)


# Analitics
product_analysis = {}
for key in product_keys:
    values = []
    for product in product_list:
        if values.count(product[1].get(key)) == 0:
            values.append(product[1].get(key))
    product_analysis[key] = values
print(product_analysis)
