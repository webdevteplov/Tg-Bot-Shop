from telebot.types import PreCheckoutQuery
from botConnection import bot
from DBConnection import cursor, connection_bd

@bot.pre_checkout_query_handler(func=lambda query: True)
def pre_checkout_process(pre_checkout: PreCheckoutQuery):
    bot.answer_pre_checkout_query(pre_checkout.id, ok=True)

@bot.message_handler(content_types=['successful_payment'])
def successful_payment(message):
    bot.send_message(message.chat.id, 'Платеж прошел успешно!')
    address = message.successful_payment.order_info.shipping_address
    cursor.execute("{CALL AddOrders (?, ?, ?, ?)}", message.chat.id, address.state, address.city, address.street_line1)
    connection_bd.commit()
    cursor.execute("{CALL DellCart}")
    connection_bd.commit()