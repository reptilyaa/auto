from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://ru.pinterest.com/angel888angel/%D0%BC%D0%B8%D0%BB%D1%8B%D0%B5-%D0%BA%D0%BE%D1%82%D0%B8%D0%BA%D0%B8/')
    but_inline2 = InlineKeyboardButton('Посмотреть', url='https://ru.pinterest.com/angel888angel/%D0%BC%D0%B8%D0%BB%D1%8B%D0%B5-%D0%BA%D0%BE%D1%82%D0%B8%D0%BA%D0%B8/')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline
