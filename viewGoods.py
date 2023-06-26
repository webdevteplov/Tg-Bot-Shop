from telebot import types
from DBConnection import cursor
from botConnection import bot

def view_goods(message, nameCategory, nameSpecies):
    cursor.execute("{CALL ShowGoods (?,?)}", nameCategory, nameSpecies)
    goods = cursor.fetchall()
    for good in goods:
        markup = types.InlineKeyboardMarkup()
        item = types.InlineKeyboardButton("Добавить в корзину", callback_data=good[0] + '/')
        markup.add(item)
        bot.send_photo(message.chat.id, reply_markup=markup, photo=good[6], caption='🔢 Код товара: ' + good[0] + '\n'
                                                                                    '🔤 Название:' + good[1] + '\n'
                                                                                    '🧵 Полотно: ' +good[4] + '\n'
                                                                                    '📏 Размеры: ' + good[7] + '\n'
                                                                                    '💵 Цена: ' + str(good[2]) + '\n')