from bs4 import BeautifulSoup
import requests
import create_db

headers_ = {"User-Agent": "Chrome/39.0.2171.95"}
food_cat = []
food_dog = []
toy_cat = []
toy_dog = []
data_ = {"cat": {"food": food_cat, "toy": toy_cat}, "dog": {"food": food_dog, "toy": toy_dog}}
select_data = "SELECT * from product WHERE Gender = 'cat'"
connection = create_db.create_connection("C:\project_python_homework\zoo_magazin.sqlite")


def cat_food():
    url_cat_food = "https://4lapy.ru/catalog/koshki/korm-koshki/sukhoy/"
    data_cat_food = requests.get(url_cat_food, headers=headers_)
    data_ = BeautifulSoup(data_cat_food.content, "html.parser")
    sata = data_.find_all(class_="b-item-name js-item-name")
    sata_1 = data_.find_all(class_="b-common-item__price js-price-block")
    for i in range(len(sata)):
        food_cat.append((sata[i].text.strip(), sata_1[i].text))


def dog_food():
    url_dog_food = "https://4lapy.ru/catalog/sobaki/korm-sobaki/sukhoy-korm-sobaki/"
    data = requests.get(url_dog_food, headers=headers_)
    data_dog_food = BeautifulSoup(data.content, "html.parser")
    data_dog_food_name = data_dog_food.find_all(class_="b-item-name js-item-name")
    data_dog_food_price = data_dog_food.find_all(class_="b-common-item__price js-price-block")
    for i in range(len(data_dog_food_name)):
        food_dog.append((data_dog_food_name[i].text.strip(), data_dog_food_price[i].text))


def cat_toy():
    url_cat_toy = "https://4lapy.ru/catalog/koshki/igrushki-koshki/"
    data_cat_toy = requests.get(url_cat_toy, headers=headers_)
    data = BeautifulSoup(data_cat_toy.content, "html.parser")
    data_cat_toy_name = data.find_all(class_="b-item-name js-item-name")
    data_cat_toy_price = data.find_all(class_="b-common-item__price js-price-block")
    for i in range(len(data_cat_toy_name)):
        toy_cat.append((data_cat_toy_name[i].text.strip(), data_cat_toy_price[i].text))


def dog_toy():
    url_dog_toy = "https://4lapy.ru/catalog/sobaki/igrushki/"
    data_dog_toy = requests.get(url_dog_toy, headers=headers_)
    data = BeautifulSoup(data_dog_toy.content, "html.parser")
    data_dog_toy_name = data.find_all(class_="b-item-name js-item-name")
    data_dog_toy_price = data.find_all(class_="b-common-item__price js-price-block")
    for i in range(len(data_dog_toy_name)):
        toy_dog.append((data_dog_toy_name[i].text.strip(), data_dog_toy_price[i].text))


def add_data_to_database():
    for gender, value in data_.items():
        for type_product, v in value.items():
            for i in v:
                add_data = f"""INSERT INTO product (title, price, gender, type_product) VALUES ("{str(i[0])}",{int(i[1])},"{str(gender)}","{str(type_product)}");
                     """
                create_db.execute_query(connection, add_data)
