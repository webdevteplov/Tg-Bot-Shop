from telebot import types
from botConnection import bot
from upload import upload_categories, upload_goods, upload_materials, upload_orders, upload_species
from viewGoods import view_goods
from cart import view_cart


def view_buttons_admin_panel(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Таблица товаров')
    item2 = types.KeyboardButton('Таблица категорий')
    item3 = types.KeyboardButton('Таблица материалов')
    item4 = types.KeyboardButton('Таблица видов')
    item5 = types.KeyboardButton('Таблица заказов')
    item6 = types.KeyboardButton('◀ Выйти')
    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, reply_markup=markup, text='Что хотите выгрузить?')

def view_buttons_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('👕 Каталог товаров')
    item2 = types.KeyboardButton('📫 Доставка и оплата')
    item3 = types.KeyboardButton('☎ Контакты')
    item4 = types.KeyboardButton('📋 Таблицы размеров')
    item5 = types.KeyboardButton('🛒 Корзина')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!\n'
                                      'Ниже перечислены все действия, которые умеет этот бот\n\n'
                                      '👕 Каталог товаров - здесь вы увидите все наши товары, актуальные на данный момент\n\n'
                                      '📫 Доставка и оплата - в этом пункте вы можете узнать о способах доставки, а также о наших выгодных условиях\n\n'
                                      '☎ Контакты - тут находится вся наша контактная информация и физический адрес\n\n'
                                      '📋 Таблицы размеров - в этом разделе, для удобства, вы можете узнать, какой размер одежды вам подойдет\n\n'
                                      '🛒 Корзина - здесь храняться товары, которые вы добавили в корзину'.format(message.from_user), reply_markup=markup)

def view_buttons_catalog(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('👩 Женские изделия')
    item2 = types.KeyboardButton('🧔 Мужские изделия')
    item3 = types.KeyboardButton('🧒 Детские изделия')
    item4 = types.KeyboardButton('👶 Ясельные изделия')
    item5 = types.KeyboardButton('◀ Назад')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, '👕 Каталог товаров'.format(message.from_user), reply_markup=markup)

def view_buttons_womens_products(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Женские комплекты')
    item2 = types.KeyboardButton('Платья')
    item3 = types.KeyboardButton('Блузки')
    item4 = types.KeyboardButton('Туники')
    item5 = types.KeyboardButton('Халаты')
    item6 = types.KeyboardButton('◀ Назад к каталогу')

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, '👩 Женские изделия'.format(message.from_user), reply_markup=markup)

def view_buttons_mens_products(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Джемперы')
    item2 = types.KeyboardButton('Мужские комплекты')
    item3 = types.KeyboardButton('Брюки')
    item4 = types.KeyboardButton('Футболки')
    item5 = types.KeyboardButton('◀ Назад к каталогу')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, '🧔 Мужские изделия'.format(message.from_user), reply_markup=markup)

def view_buttons_childrens_products(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Для девочек')
    item2 = types.KeyboardButton('Для мальчиков')
    item3 = types.KeyboardButton('◀ Назад к каталогу')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, '🧒 Детские изделия'.format(message.from_user), reply_markup=markup)

def view_buttons_shipping_and_payment(message):
    bot.send_message(message.chat.id, '❗ПРОЦЕДУРА ФОРМИРОВАНИЯ ЗАКАЗА❗\n\n'
                                      '✅1. Вы знакомитесь с ассортиментом товара.\n'
                                      '✅2. Составляете заказ (заказ линейками) и отправляете его при помощи звонка, или на электронную почту.\n'
                                      '✅3. Мы обрабатываем заказ, редактируя заявку вместе с Вами, определяем сроки поставки, собираем товар, выставляем счет.\n'
                                      '✅4. После оплаты за товар наличными денежными средствами в кассу либо по факту поступления денежных средств на расчетный счет, мы отгружаем продукцию.\n'
                                      '✅5. К Вашим услугам любые виды отгрузки товара.\n\n'
                                      '❗ПО ОПЛАТЕ❗\n\n'
                                      '✅Мы работаем по 100% предоплате.  Оплата принимается наличными денежными средствами в кассу и безналичным расчетом.\n\n'
                                      '❗ПРЕИМУЩЕСТВА РАБОТЫ С НАМИ❗\n\n'
                                      '✅1. Минимальная сумма закупки всего 10000 рублей.\n'
                                      '✅2. Возможность рассрочки для постоянных клиентов и дополнительная скидка при заказе от 300.000 рублей.\n'
                                      '✅3. Любые удобные способы оплаты.\n'
                                      '✅4. Бесплатная доставка до транспортной компании.\n'
                                      '✅5. Вся продукция прошла обязательную сертификацию и имеет все необходимые документы\n'
                                      '✅6. Гарантия 100% обмена или возврата при обнаружении брака.\n'
                                      '✅7. Быстрая обработка заявки персональным менеджером и при отсутствии части ассортимента быстрый запуск в производство.')

def view_buttons_contacts(message):
    bot.send_message(message.chat.id, '🏠Наш адрес: Кемеровская обл, пгт. Краснобродский, ул. Юбилейная 3\n'
                                      '📞Тел: 8-905-902-9662; 8-(3845)-27-55-21; 8-905-902-9663\n'
                                      '🕗Режим работы: 8.30 – 17.00 (Пн. – Пт.), 8.30 – 15.00 (Сб.),  Выходной - Вс.\n'
                                      '🍵Обед: 12:30-13:00\n'
                                      '📧e-mail: tf_nadejda@mail.ru')

def view_buttons_size_charts(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('👩 Женские размеры')
    item2 = types.KeyboardButton('🧔 Мужские размеры')
    item3 = types.KeyboardButton('🧒 Детские размеры')
    item4 = types.KeyboardButton('👶 Ясельные размеры')
    item5 = types.KeyboardButton('◀ Назад')
    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, '📋 Таблицы размеров', reply_markup=markup)

def view_womens_sizes(message):
    bot.send_photo(message.chat.id,
                   photo='https://sun139-1.userapi.com/impg/aNTmJ8vB2WF9BshR07QCjJolNXqYvRlL-smeAg/yzOdDZ8Abw8.jpg?size=802x773&quality=96&sign=49a1dd3c6ce7934720bbfbec3f55bf13&type=album')

def view_mens_sizes(message):
    bot.send_photo(message.chat.id,
                   photo='https://sun9-59.userapi.com/impg/nSuIYwos_dUR-5lDHsaFoVhl2GIEH2wKmrU2kQ/frgfnuWpf-I.jpg?size=803x475&quality=96&sign=57ce427861937336282d37b4cd420e60&type=album')

def view_childrens_sizes(message):
    bot.send_photo(message.chat.id,
                   photo='https://sun9-80.userapi.com/impg/RIN8UvIHmAkoB_1HQjSX_zNQSa79849a3_qCEQ/nRxVt1GeT0Y.jpg?size=802x773&quality=96&sign=fd4e3c11712a55eea12d05e2fac22346&type=album')

def view_nursery_sizes(message):
    bot.send_photo(message.chat.id,
                   photo='https://sun9-71.userapi.com/impg/UCsruYQKVzQDFyZkQ6h2IgDabN9y1MgrbfrSyA/hHR58wkdsHg.jpg?size=484x674&quality=96&sign=17cee6548f9a0e3e6f93da619737c1ad&type=album')

def button_back_to_start_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('👕 Каталог товаров')
    item2 = types.KeyboardButton('📫 Доставка и оплата')
    item3 = types.KeyboardButton('☎ Контакты')
    item4 = types.KeyboardButton('📋 Таблицы размеров')
    item5 = types.KeyboardButton('🛒 Корзина')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, '◀ Назад'.format(message.from_user), reply_markup=markup)

def view_buttons(message):
    if message.text == 'Таблица товаров': # выгрузка товаров
        upload_goods(message)

    elif message.text == 'Таблица категорий': # выгрузка категорий
        upload_categories(message)

    elif message.text == 'Таблица материалов': # выгрузка материалов
        upload_materials(message)

    elif message.text == 'Таблица видов': # выгрузка видов
        upload_species(message)

    elif message.text == 'Таблица заказов': # выгрузка заказов Выйти
        upload_orders(message)

    elif message.text == '◀ Выйти':  # выход из панели админа
        bot.send_message(message.chat.id, 'До встречи!')
        view_buttons_start(message)

    elif message.text == '👕 Каталог товаров':
        view_buttons_catalog(message)


    elif message.text == '👩 Женские изделия':
        view_buttons_womens_products(message)



    elif message.text == 'Женские комплекты':
        view_goods(message, 'Женские изделия', 'Комплекты')

    elif message.text == 'Платья':
        view_goods(message, 'Женские изделия', 'Платья')

    elif message.text == 'Блузки':
        view_goods(message, 'Женские изделия', 'Блузки')

    elif message.text == 'Туники':
        view_goods(message, 'Женские изделия', 'Туники')

    elif message.text == 'Халаты':
        view_goods(message, 'Женские изделия', 'Халаты')




    elif message.text == '🧔 Мужские изделия':
        view_buttons_mens_products(message)



    elif message.text == 'Джемперы':
        view_goods(message, 'Мужские изделия', 'Джемперы')

    elif message.text == 'Мужские комплекты':
        view_goods(message, 'Мужские изделия', 'Комплекты')

    elif message.text == 'Брюки':
        view_goods(message, 'Мужские изделия', 'Брюки')

    elif message.text == 'Футболки':
        view_goods(message, 'Мужские изделия', 'Футболки')



    elif message.text == '🧒 Детские изделия':
        view_buttons_childrens_products(message)


    elif message.text == 'Для девочек':
        view_goods(message, 'Детские изделия', 'Для девочек')

    elif message.text == 'Для мальчиков':
        view_goods(message, 'Детские изделия', 'Для мальчиков')



    elif message.text == '👶 Ясельные изделия':
        view_goods(message, 'Ясельные изделия', 'Комплекты')



    elif message.text == '◀ Назад к каталогу':
        view_buttons_catalog(message)

    elif message.text == '📫 Доставка и оплата':
        view_buttons_shipping_and_payment(message)

    elif message.text == '☎ Контакты':
        view_buttons_contacts(message)

    elif message.text == '📋 Таблицы размеров':
        view_buttons_size_charts(message)

    elif message.text == '👩 Женские размеры':
        view_womens_sizes(message)
    elif message.text == '🧔 Мужские размеры':
        view_mens_sizes(message)
    elif message.text == '🧒 Детские размеры':
        view_childrens_sizes(message)
    elif message.text == '👶 Ясельные размеры':
        view_nursery_sizes(message)


    elif message.text == '🛒 Корзина':
        view_cart(message)

    elif message.text == '◀ Назад':
        button_back_to_start_menu(message)
