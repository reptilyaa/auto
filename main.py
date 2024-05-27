from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

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
    await message.answer('Привет, я твой первый эхо бот')


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