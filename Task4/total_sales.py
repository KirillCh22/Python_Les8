import csv


def main():

    dict_total_sales = dict()
    with open('E:\Учеба в GeekBrains\Семинары по Python(углубленная)\Les8\Task4\sales.csv', 'r', newline='') as csv_read:
        reader = csv.DictReader(csv_read)

        for row in reader:
            product = row['product']
            quantity = int(row['quantity'])
            price = float(row['price'])

            total_sales = quantity * price

            # ПРОВЕРЯЕМ ЕСТЬ ЛИ УЖЕ ТАКОЙ ПРОДУКТ В НАШЕЙ БИБЛИОТЕКЕ, ЕСЛИ ЕСТЬ, ТО ПРОСТО ДОБАВЛЯЕМ СУММУ
            # ЕСЛИ НЕТ, ТО УКАЗЫВАЕМ ДАННЫЙ ПРОДУКТ И ПРИСВАИВАЕМ ЕМУ НОВОЕ ЗНАЧЕНИЕ
            if product in dict_total_sales:
                dict_total_sales[product] += total_sales
            else:
                dict_total_sales[product] = total_sales

# СОЗДАЕМ НОВЫЙ ФАЙЛ csv В КОТОРЫЙ ДОБАВИМ НАШУ НОВУЮ БИБЛИОТЕКУ
    with open('total_sales.csv', 'w', newline='') as csv_write:
        keys_names = ['product', 'total_sales']
        writer = csv.DictWriter(csv_write, fieldnames=keys_names)
        writer.writeheader()

        for product, total_sales in dict_total_sales.items():
            writer.writerow({'product': product, 'total_sales': total_sales})





if __name__ == '__main__':
    main()