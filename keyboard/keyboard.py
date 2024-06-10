from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('Информация об автомобилях')
    button_2 = KeyboardButton('Поиск по название модели')
    button_3 = KeyboardButton('Поиск по дилеру')
    button_4 = KeyboardButton('Перейти на следующую клавиатуру')
    keyboard.add(button_1, button_2, button_3, button_4)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    button_5 = KeyboardButton('История автомобилей')
    button_6 = KeyboardButton('Советы по выбору')
    button_7 = KeyboardButton('Вернуться на 1 клавиатуру')
    keyboard_2.add(button_5, button_6, button_7)
    return keyboard_2