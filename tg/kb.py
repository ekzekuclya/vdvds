from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

builder = ReplyKeyboardBuilder()
builder.add(KeyboardButton(text="🔍 У меня НН"))
builder.add(KeyboardButton(text="⏱ Когда пополнение?"))
builder.add(KeyboardButton(text="🧑‍🏭 Работа"))