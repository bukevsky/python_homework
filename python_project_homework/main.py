import parser
import random
import sqlite3

def get_random_products_by_type(gender):
    # Подключение к базе данных
    conn = sqlite3.connect('zoo_magazin.sqlite')
    cursor = conn.cursor()

    # Выполнение SQL-запроса для выборки случайной записи каждого типа продукта
    cursor.execute('''SELECT * FROM (
                          SELECT * FROM product
                          WHERE gender = ?
                          ORDER BY RANDOM()
                       ) GROUP BY type_product''', (gender,))

    # Получение результатов выборки
    rows = cursor.fetchall()

    # Закрытие соединения с базой данных
    conn.close()

    return rows

def get_gender():
    gender = input().lower()
    random_products = get_random_products_by_type(gender)
    for product in random_products:
        print("ID:", product[0])
        print("Title:", product[1])
        print("Price:", product[2])
        print("Gender:", product[3])
        print("Type:", product[4])
        print("-------------------")



if __name__ == "__main__":
    # parser.dog_toy()
    # parser.cat_toy()
    # parser.cat_food()
    # parser.dog_food()
    # parser.add_data_to_database()
    get_gender()
