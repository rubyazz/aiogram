from bot import bot, dp
from aiogram.types import Message
from config import my_id



async def send_to_admin(dp):
    await bot.send_message(chat_id=my_id, text="Hello, everyone!")


@dp.message_handler()
async def echo(message:Message):
    if message.text == 'Kalaisyn':
        text = f"Jagsy wukir ozin kalaisyn"
        await bot.send_message(chat_id=message.from_user.id, text=text)
    elif message.text == 'Salem':
        await bot.send_message(chat_id=message.from_user.id, text='Privet\nKak dela?')


@dp.message_handler()
async def get_data(message:Message):
    if message.text == 'pizza':
        pass
        #Lets make a choice which one Margarita or THe big boy







