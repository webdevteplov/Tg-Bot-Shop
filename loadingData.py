import xml.etree.ElementTree as ET
from DBConnection import connection_bd, cursor


pathXml = 'BD/import.xml'
tree = ET.parse(pathXml)
root = tree.getroot()


def loadingData():
    categoriesArray = []
    setCategoriesArray = []  # Уникальные категории

    materialsArray = []
    setMaterialsArray = []  # Уникальные материалы

    speciesArray = []
    setSpeciesArray = []  # Уникальные виды

    for goods in root.findall('Каталог/Товары/Товар'):  # -----------> Вытягиваем всю информацию с xml
        productCode = goods.find('Артикул').text
        name = goods.find('Наименование').text

        categoriesArray.append(goods.find('Категория').text)
        setCategoriesArray = set(categoriesArray)

        speciesArray.append(goods.find('Вид').text)
        setSpeciesArray = set(speciesArray)

        materialsArray.append(goods.find('ХарактеристикиТовара/Наименование').text)
        setMaterialsArray = set(materialsArray)

        photo = goods.find('ХарактеристикиТовара/Фото').text
        photoUrl = photo.replace('*', '&')

        price = goods.find('ХарактеристикиТовара/Цена').text
        sizeRange = goods.find('ХарактеристикиТовара/РазмерныйРяд').text

    for item in setCategoriesArray:
        cursor.execute("{CALL AddCategories (?)}", item)

    connection_bd.commit()

    for item in setMaterialsArray:
        cursor.execute("{CALL AddMaterials (?)}", item)

    connection_bd.commit()

    for item in setSpeciesArray:
        cursor.execute("{CALL AddSpecies (?)}", item)

    connection_bd.commit()

    for goods in root.findall('Каталог/Товары/Товар'):  # ---------> Добавление товара
        productCode = goods.find('Артикул').text
        name = goods.find('Наименование').text
        price = goods.find('ХарактеристикиТовара/Цена').text
        category = goods.find('Категория').text
        material = goods.find('ХарактеристикиТовара/Наименование').text
        species = goods.find('Вид').text
        photo = goods.find('ХарактеристикиТовара/Фото').text
        photoUrl = photo.replace('*', '&')
        sizeRange = goods.find('ХарактеристикиТовара/РазмерныйРяд').text

        cursor.execute("{CALL AddGoods (?,?,?,?,?,?,?,?)}", productCode, name, int(price), category, material, species,
                       photoUrl, sizeRange)

    connection_bd.commit()