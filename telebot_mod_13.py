from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    adress = State()
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text= 'Калории')
async def set_age(message):
    await message.answer("Введите свой возраст(полных лет): ")
    await UserState.age.set()

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

@dp.message_handler(text=['Urban'])
async def urban_message(message):
    print('Urban message')

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью,'
                         ' если хочешь узнать свою норму, напиши: Калории.')


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

