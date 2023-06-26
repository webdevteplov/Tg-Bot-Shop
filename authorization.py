from DBConnection import cursor, connection_bd
from botConnection import bot
from viewButtons import view_buttons_start, view_buttons_admin_panel, view_buttons



#функция для проверки, зарегистрирован ли пользователь
def is_registered(chat_id):
    cursor.execute("{CALL ShowBuyers (?)}", chat_id)
    result = cursor.fetchone()
    if result[0] > 0:
        return True
    else:
        return False

# функция для регистрации пользователя
def register_user(name, phone, chat_id):
    cursor.execute("{CALL AddBuyers (?, ?, ?)}", chat_id, name, phone)
    connection_bd.commit()



# функция для обработки команды /start и запроса авторизации
@bot.message_handler(commands=['start'])

def send_welcome(message):
    if is_registered(message.chat.id):
        bot.reply_to(message, "Вы уже зарегистрированы.")
        view_buttons_start(message)
    else:
        Name = bot.reply_to(message, "Добро пожаловать! \n"
                                     " Введите ваше имя:")
        bot.register_next_step_handler(Name, process_name_step)

# функция для обработки ввода имени пользователя и запроса номера телефона
def process_name_step(message):
    try:
        Name = message.text
        Phone = bot.reply_to(message, "Введите ваш номер телефона:")

        bot.register_next_step_handler(Phone, process_phone_number_step, Name)
    except Exception as e:
        bot.reply_to(message, "Ошибка: {}. Попробуйте еще раз.".format(e))

# функция для обработки ввода номера телефона и регистрации пользователя
def process_phone_number_step(message, name):
    try:
        phone_number = message.text
        register_user(name, phone_number, message.chat.id)

        bot.reply_to(message, "Вы успешно зарегистрированы, {}! Ваш номер телефона: {}".format(name, phone_number))
        view_buttons_start(message)
    except Exception as e:
        bot.reply_to(message, "Ошибка: {}. Попробуйте еще раз.".format(e))




@bot.message_handler(commands=['admin'])
def login_for_admin(message):
    login = bot.reply_to(message, "Введите ваш логин:")
    bot.register_next_step_handler(message, password_for_admin, login)

def password_for_admin(message, login):
    login = message.text
    password = bot.reply_to(message, "Введите ваш пароль:")
    bot.register_next_step_handler(message, is_registered_admin, login, password)

def is_registered_admin(message, login, password):
    password = message.text
    cursor.execute("{CALL ShowAdministrators (?, ?)}", login, password)
    result = cursor.fetchone()
    if result[0] > 0:
        bot.reply_to(message, 'Добро пожаловать')
        view_buttons_admin_panel(message)
        # admin_panel(message)
    else:
        bot.reply_to(message, 'Неверный логин или пароль!')
        # start(message)
        view_buttons_start(message)

# Вывести меню
@bot.message_handler(content_types=['text'])
def bot_show_goods(message):
    if message.chat.type == 'private':
        view_buttons(message)



