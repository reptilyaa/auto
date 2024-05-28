from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1,get_keyboard_2
from keyboard.Key_inline import get_keyboard_inline

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description='Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы узнать, чем может помочь наш бот'),
        types.BotCommand(command='/info', description='Команда для того, чтобы узнать, для чего этот бот'),
        types.BotCommand(command='/creators', description='Команда для того, чтобы узнать, создателей бота'),
        types.BotCommand(command='/test', description='Команда для того, чтобы проверить работу команды')
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я твой первый эхо бот', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://avatars.dzeninfra.ru/get-zen_doc/8269145/pub_641ec1d0798be415157b4180_641f3d1cd4b1f54fcf2f0a01/scale_1200',caption='Вот тебе кот!', reply_markup=get_keyboard_inline())

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_1_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото собаки', reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отправь фото собаки')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://zooqi.by/social/cache/image_attachment_preview_large/attachment-image/160/3621_15127421369091.jpg?1644400101',caption='Вот тебе собака!')

@dp.message_handler(lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_1_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото кота', reply_markup=get_keyboard_1())
@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Я могу помочь тебе с ....')

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