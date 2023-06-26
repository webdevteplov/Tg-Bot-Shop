from DBConnection import cursor
from botConnection import bot
import pandas as pd


def upload_goods(message):
    cursor.execute("{CALL UploadGoods}")
    good_id = []
    name = []
    price = []
    category_id = []
    material_id = []
    species_id = []
    photo_url = []
    size_range = []
    goods = cursor.fetchall()

    for good in goods:
        good_id.append(good[0])
        name.append(good[1])
        price.append(good[2])
        category_id.append(good[3])
        material_id.append(good[4])
        species_id.append(good[5])
        photo_url.append(good[6])
        size_range.append(good[7])

    upload_goods = pd.DataFrame({
        'Артикул': good_id,
        'Наименование': name,
        'Цена': price,
        'Номер категории': category_id,
        'Номер материала': material_id,
        'Номер вида': species_id,
        'Ссылка на фото': photo_url,
        'Размерный ряд': size_range
    })
    upload_goods.to_excel('Upload/UploadGoods.xlsx', sheet_name='Goods', index=False)
    bot.send_message(message.chat.id, 'Таблица товаров выгружена!')

def upload_categories(message):
    cursor.execute("{CALL UploadCategories}")
    category_id = []
    name_category = []
    categories = cursor.fetchall()

    for category in categories:
        category_id.append(category[0])
        name_category.append(category[1])

    upload_goods = pd.DataFrame({
        'ID': category_id,
        'Наименование': name_category,
    })
    upload_goods.to_excel('Upload/UploadCategories.xlsx', sheet_name='Categories', index=False)
    bot.send_message(message.chat.id, 'Таблица категорий выгружена!')

def upload_materials(message):
    cursor.execute("{CALL UploadMaterials}")
    material_id = []
    name_material = []
    materials = cursor.fetchall()

    for material in materials:
        material_id.append(material[0])
        name_material.append(material[1])

    upload_goods = pd.DataFrame({
        'ID': material_id,
        'Наименование': name_material,
    })
    upload_goods.to_excel('Upload/UploadMaterials.xlsx', sheet_name='Materials', index=False)
    bot.send_message(message.chat.id, 'Таблица материалов выгружена!')

def upload_species(message):
    cursor.execute("{CALL UploadSpecies}")
    species_id = []
    name_species = []
    species = cursor.fetchall()

    for specie in species:
        species_id.append(specie[0])
        name_species.append(specie[1])

    upload_goods = pd.DataFrame({
        'ID': species_id,
        'Наименование': name_species,
    })
    upload_goods.to_excel('Upload/UploadSpecies.xlsx', sheet_name='Species', index=False)
    bot.send_message(message.chat.id, 'Таблица видов выгружена!')

def upload_orders(message):
    cursor.execute("{CALL UploadOrders}")
    orders_id = []
    buyers_id = []
    states = []
    cities = []
    streets = []
    orders = cursor.fetchall()

    for order in orders:
        orders_id.append(order[0])
        buyers_id.append(order[1])
        states.append(order[2])
        cities.append(order[3])
        streets.append(order[4])

    upload_goods = pd.DataFrame({
        'ID': orders_id,
        'ID покупателя': buyers_id,
        'Область': states,
        'Город': cities,
        'Улица': streets
    })
    upload_goods.to_excel('Upload/UploadOrders.xlsx', sheet_name='Orders', index=False)
    bot.send_message(message.chat.id, 'Таблица заказов выгружена!')