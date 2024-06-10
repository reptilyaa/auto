from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://auto.ru/mag/article/lyubopytnye-fakty-o-mercedesbenz-o-kotoryh-vy-i-ne-dogadyvalis/')
    but_inline2 = InlineKeyboardButton('Посмотреть', url='https://auto.ru/mag/article/lyubopytnye-fakty-o-mercedesbenz-o-kotoryh-vy-i-ne-dogadyvalis/')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline
def get_keyboard_inline_1():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://auto.ru/catalog/cars/mercedes/?utm_referrer=https%3A%2F%2Fwww.google.com%2F')
    but_inline2 = InlineKeyboardButton('Посмотреть', url='https://auto.ru/catalog/cars/mercedes/?utm_referrer=https%3A%2F%2Fwww.google.com%2F')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline
def get_keyboard_inline_2():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://mb-avilon.ru/')
    but_inline2 = InlineKeyboardButton('Посмотреть', url='https://mb-avilon.ru/')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline
def get_keyboard_inline_3():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://pikabu.ru/story/15_interesnyikh_faktov_o_mersedese_5084278')
    but_inline2 = InlineKeyboardButton('Посмотреть', url='https://pikabu.ru/story/15_interesnyikh_faktov_o_mersedese_5084278')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline
def get_keyboard_inline_4():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://pogazam.ru/news/auto_news/2019/8/32909/')
    but_inline2 = InlineKeyboardButton('Посмотреть', url='https://pogazam.ru/news/auto_news/2019/8/32909/')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline