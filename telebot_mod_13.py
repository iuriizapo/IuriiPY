from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button = KeyboardButton(text= 'Информация')
keyboard.add(button)
keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_2 = KeyboardButton(text= 'Рассчитать')
keyboard_2.add(button_2)
kb = InlineKeyboardMarkup()
but_1 = InlineKeyboardButton(text='Норма калорий', callback_data='calories')
but_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb.add(but_1, but_2)



class UserState(StatesGroup):
    adress = State()
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text= 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:',reply_markup=kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('''
    для мужчин:
    10 х вес (кг) + 
    6,25 x рост (см) – 
    5 х возраст (г) + 5''')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст(полных лет): ")
    await UserState.age.set()
    #await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(secon=message.text)
    await message.answer('Введите свой рост(см): ')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(fird=message.text)
    await message.answer('Введите свой вес(кг): ')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(fors=message.text)
    data = await state.get_data()
    await message.answer(f"Ваша норма калорий:"
                         f" {10*int(data['fors'])+6.25*int(data['fird'])-5*int(data['secon'])+5}")
    await state.finish()


@dp.message_handler(text= 'заказать')
async def buy(message):
    await message.answer("Отправь нам свой адрес, пожалуйста")
    await UserState.adress.set()

@dp.message_handler(state=UserState.adress)
async def fsm_handler(message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()
    await message.answer(f'Доставка будет отправлена на {data["first"]}')
    await state.finish()

@dp.message_handler(text=['Информация'])
async def info_message(message):
    await message.answer('Если хочешь узнать свою норму калорий, жми: Рассчитать',reply_markup=keyboard_2)

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет. Я бот помогающий твоему здоровью!',reply_markup=keyboard)   #



@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


