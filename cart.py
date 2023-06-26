from telebot.types import LabeledPrice
from telebot import types
from DBConnection import cursor, connection_bd
from botConnection import bot
from config import pay_token


def view_cart(message):
    cursor.execute("{CALL ShowCart (?)}", message.chat.id)
    cart = cursor.fetchall()
    if len(cart) > 0:
        prices = []
        for good in cart:
            markup_del = types.InlineKeyboardMarkup()
            item_del = types.InlineKeyboardButton("Удалить", callback_data=good[0] + '*')
            markup_del.add(item_del)
            total_price_good = good[2] * good[4]
            prices.append(
                LabeledPrice(label=good[1] + '\n(x' + str(good[4]) + ')', amount=int(str(total_price_good) + '00')))
            bot.send_photo(message.chat.id, reply_markup=markup_del, photo=good[3], caption='🔢 Код товара: ' + good[0] + '\n'
                                                                                            '🔤 Название:' + good[1] + '\n'
                                                                                            '💵 Цена: ' + str(good[2]) + '\n'
                                                                                            '📎 Количество: ' + str(good[4]))
        markup_pay = types.InlineKeyboardMarkup()
        item_pay = types.InlineKeyboardButton(text='Оплатить', pay=True)
        markup_pay.add(item_pay)
        bot.send_invoice(message.chat.id,
                         title='Оплатить корзину',
                         photo_height=800,
                         photo_width=500,
                         description='Общая стоимость',
                         provider_token=pay_token,
                         currency='rub',
                         need_shipping_address=True,
                         prices=prices,
                         start_parameter='example',
                         invoice_payload='some_invoice',
                         reply_markup=markup_pay)
    else:
        bot.send_message(message.chat.id, 'Корзина пуста')

def add_to_cart(call):
    cursor.execute("{CALL ShowGoodsId}")
    goods = cursor.fetchall()
    for good in goods:
        good[0] = good[0]+'/'
        if call.data == good[0]:
            cursor.execute("{CALL AddCart (?,?)}", good[0][:-1], call.message.chat.id)
            connection_bd.commit()
            bot.send_message(call.message.chat.id, 'Товар добавлен в корзину!')
            bot.answer_callback_query(call.id)

def dell_to_cart(call):
    cursor.execute("{CALL ShowCart (?)}", call.message.chat.id)
    goods = cursor.fetchall()
    if len(goods) > 0:
        for good in goods:
            good[0] = good[0] + '*'
            if call.data == good[0]:
                cursor.execute("{CALL DellGoodInCartById (?, ?)}", good[0][:-1], call.message.chat.id)
                connection_bd.commit()
                bot.send_message(call.message.chat.id, text='Товар удален из корзины!')
                bot.answer_callback_query(call.id)
                view_cart(call.message)


@bot.callback_query_handler(func=lambda call: True)  # Обработчик кнопок добавление и удаление в корзине
def callback_handler(call):
    if call.message:
        add_to_cart(call)
    if call.message:
        dell_to_cart(call)

