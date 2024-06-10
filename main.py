from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.Key_inline import get_keyboard_inline,get_keyboard_inline_1, get_keyboard_inline_2, get_keyboard_inline_3, get_keyboard_inline_4
from keyboard.keyboard import get_keyboard_1, get_keyboard_2


bot = Bot(token=TELEGRAM_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
  await message.answer('Привет!  Я бот, который поможет тебе разобраться в мире автомобилей! ', reply_markup=get_keyboard_1())

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Я могу помочь тебе найти информацию о различных автомобилях')

@dp.message_handler(commands='info')
async def help(message: types.Message):
    await message.reply('Это бот которого мы делали на практике')


@dp.message_handler(commands='creators')
async def help(message: types.Message):
    await message.reply('Мартынов Иван, Тухтаев Умеджон')


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description='Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы узнать, чем может помочь наш бот'),
        types.BotCommand(command='/info', description='Команда для того, чтобы узнать, Марки и модели, технические характеристики'),
        types.BotCommand(command='/creators', description='Команда для того, чтобы узнать, создателей бота'),
        types.BotCommand(command='/test', description='Команда для того, чтобы проверить работу команды')
    ]
    await bot.set_my_commands(commands)


@dp.message_handler(lambda message: message.text == 'Информация об автомобилях')
async def button_1_click(message: types.Message):
    await message.answer('Тут ты найдешь все информацию об автомобиле Мерседес.',  reply_markup=get_keyboard_2())
    await bot.send_photo(message.chat.id, photo='https://universeofcars.ru/wp-content/uploads/2021/05/all-new-mercedes-s-class-by-mansory-debuts-with-exclusive-styling-more-power_4.jpg',caption='Вот тебе Мерседес!', reply_markup=get_keyboard_inline())
@dp.message_handler(lambda message: message.text == 'Поиск по название модели')
async def button_1_click(message: types.Message):
    await message.answer('Тут ты найдешь все информацию о моделях Мерседеса.',  reply_markup=get_keyboard_2())
    await bot.send_photo(message.chat.id, photo='https://carsweek.ru/upload/iblock/10e/10ebc907c5f1a198a0a89dca515e9eeb.jpg',caption='Вот тебе дилере Мерседеса!', reply_markup=get_keyboard_inline_1())
@dp.message_handler(lambda message: message.text == 'Поиск по дилеру')
async def button_1_click(message: types.Message):
    await message.answer('Все доступные дилеры от Мерседеса.',  reply_markup=get_keyboard_2())
    await bot.send_photo(message.chat.id, photo='https://novosti-ru.ru/wp-content/uploads/2024/01/avtosalon-mersedes-bents-daimler.-foto-sotsseti.jpeg',caption='Вот тебе все модели Мерседеса!', reply_markup=get_keyboard_inline_2())

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_1_click(message: types.Message):
    await message.answer('Тут ты можешь ознакомиться с историей автомобилей', reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'История автомобилей')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://cs8.pikabu.ru/post_img/big/2017/05/28/10/1495993394143880604.jpg',caption='Вот тебе информация о Мерседесе!', reply_markup=get_keyboard_inline_3())
@dp.message_handler(lambda message: message.text == 'Советы по выбору')
async def button_3_click(message: types.Message):
    await message.answer('Наш бот может помочь определиться с выбором', reply_markup=get_keyboard_2())
    await bot.send_photo(message.chat.id, photo='https://avatars.mds.yandex.net/get-verba/1540742/2a0000018f715b68b3fcffcbff4119bac587/320x240',caption='Вот тебе советы о мерседесе!', reply_markup=get_keyboard_inline_4())

@dp.message_handler(lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_1_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото мерседеса', reply_markup=get_keyboard_1())
@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Я могу помочь тебе найти информацию о различных автомобилях')

@dp.message_handler(commands='info')
async def help(message: types.Message):
    await message.reply('Это бот которого мы делали на практике')


@dp.message_handler(commands='creators')
async def help(message: types.Message):
    await message.reply('Мартынов Иван, Тухтаев Умеджон')



@dp.message_handler(commands='test')
async def help(message: types.Message):
    await message.reply('123')


@dp.message_handler()
async  def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)