from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

TOKEN = "8717876300:AAGH_uryEeRXQvGmMg3zqeskWVbRl-e1yLo"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Головне меню
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("✨ Записатися"))
menu.add(KeyboardButton("💅 Прайс"))
menu.add(KeyboardButton("📸 Наші роботи"))
menu.add(KeyboardButton("📍 Адреса"))
menu.add(KeyboardButton("💌 Зв’язатися"))

# Послуги
services = ReplyKeyboardMarkup(resize_keyboard=True)
services.add(KeyboardButton("Манікюр"))
services.add(KeyboardButton("Нарощування"))
services.add(KeyboardButton("Педикюр"))
services.add(KeyboardButton("⬅️ Назад"))

# Дати
calendar = ReplyKeyboardMarkup(resize_keyboard=True)
calendar.add(KeyboardButton("16 травня"))
calendar.add(KeyboardButton("17 травня"))
calendar.add(KeyboardButton("18 травня"))
calendar.add(KeyboardButton("⬅️ Назад"))

# Час
hours = ReplyKeyboardMarkup(resize_keyboard=True)
hours.add(KeyboardButton("10:00"))
hours.add(KeyboardButton("13:00"))
hours.add(KeyboardButton("16:00"))
hours.add(KeyboardButton("⬅️ Назад"))

user_data = {}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "🌸 Ласкаво просимо до Kharkiv Beauty Studio!\n\nОберіть дію 👇",
        reply_markup=menu
    )

@dp.message_handler(lambda message: message.text == "✨ Записатися")
async def booking(message: types.Message):
    await message.answer(
        "✨ Оберіть послугу:",
        reply_markup=services
    )

@dp.message_handler(lambda message: message.text in ["Манікюр", "Нарощування", "Педикюр"])
async def service_selected(message: types.Message):
    user_data[message.from_user.id] = {
        "service": message.text
    }

    await message.answer(
        "📅 Оберіть дату:",
        reply_markup=calendar
    )

@dp.message_handler(lambda message: message.text in ["16 травня", "17 травня", "18 травня"])
async def date_selected(message: types.Message):
    user_data[message.from_user.id]["date"] = message.text

    await message.answer(
        "⏰ Оберіть час:",
        reply_markup=hours
    )

@dp.message_handler(lambda message: message.text in ["10:00", "13:00", "16:00"])
async def time_selected(message: types.Message):
    user_data[message.from_user.id]["time"] = message.text

    service = user_data[message.from_user.id]["service"]
    date = user_data[message.from_user.id]["date"]
    time = user_data[message.from_user.id]["time"]

    await message.answer(
        f"🌸 Ви записані!\n\n"
        f"💅 Послуга: {service}\n"
        f"📅 Дата запису: {date}\n"
        f"⏰ Час: {time}\n\n"
        f"📍 Kharkiv Beauty Studio\n"
        f"Центр Харкова, біля метро Наукова ✨\n\n"
        f"Instagram: https://instagram.com/vykhrovaa",
        reply_markup=menu
    )

@dp.message_handler(lambda message: message.text == "💅 Прайс")
async def price(message: types.Message):
    await message.answer(
        "💅 Прайс:\n\n"
        "Манікюр — 700 грн\n"
        "Нарощування — 1200 грн\n"
        "Педикюр — 900 грн\n\n"
        "Instagram: https://instagram.com/vykhrovaa"
    )

@dp.message_handler(lambda message: message.text == "📸 Наші роботи")
async def works(message: types.Message):
    await message.answer(
        "📸 Наш Instagram:\n"
        "https://instagram.com/vykhrovaa"
    )

@dp.message_handler(lambda message: message.text == "📍 Адреса")
async def address(message: types.Message):
    await message.answer(
        "📍 Kharkiv Beauty Studio\n"
        "Центр Харкова, біля метро Наукова ✨\n\n"
        "Instagram: https://instagram.com/vykhrovaa"
    )

@dp.message_handler(lambda message: message.text == "💌 Зв’язатися")
async def contact(message: types.Message):
    await message.answer(
        "💌 Напишіть майстру:\n@nverbb\n\n"
        "Instagram: https://instagram.com/vykhrovaa"
    )

@dp.message_handler(lambda message: message.text == "⬅️ Назад")
async def back(message: types.Message):
    await message.answer(
        "Головне меню 👇",
        reply_markup=menu
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
