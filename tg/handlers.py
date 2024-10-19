from aiogram import Router, Bot, F
from aiogram.filters import Command, CommandObject, BaseFilter
from aiogram.types import Message, InlineKeyboardButton, ReplyKeyboardMarkup, ChatMemberOwner, ChatMemberAdministrator
from django.db.models import Q

from .models import Trigger

from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from asgiref.sync import sync_to_async
from .models import TelegramUser

router = Router()


def name(user):
    link = "tg://user?id="
    player_username = (
        f"@{user.username}"
        if user.username
        else (
            f"[{user.first_name + (' ' + user.last_name if user.last_name else '')}]"
            f"({link}{str(user.user_id)})"
        )
    )
    player_username = player_username.replace("_", r"\_")
    return "👤 " + player_username


# @router.message(Command("start"))
# async def start_cmd(msg: Message, bot: Bot, cmd: CommandObject):
#     user, created = await sync_to_async(TelegramUser.objects.get_or_create)(user_id=msg.from_user.id)
#     data = cmd.args
#     if created:
#         if data:
#             if data == "5464573":
#                 user.in_place = "Центра"
#                 user.save()
#             elif data == "v88543536":
#                 user.in_place = "Вверха"
#                 user.save()


# @router.business_message()
# async def start_menu(msg: Message, bot: Bot):
#     print("CHAT ID", msg.chat.id, "\nFROM USER ID", msg.from_user.id)
#     user, created = await sync_to_async(TelegramUser.objects.get_or_create)(user_id=msg.from_user.id)
#     text = "Приветствие"
#     photo = "AgACAgIAAxkBAANhZxAyGc3IU8B_olhhcYMnQ-rbsVsAAgTtMRtbd4FIvTZ7t3jvULkBAAMCAAN5AAM2BA"
#     builder = InlineKeyboardBuilder()
#     builder.add(InlineKeyboardButton(text='Купить LTC', callback_data="buy_ltc"))
#     builder.add(InlineKeyboardButton(text="Вызвать оператора", callback_data="call_op"))
#     builder.adjust(1)
#     await msg.answer("test", reply_markup=builder.as_markup())
#     await bot.send_message(chat_id="6126380985", text=f"Пользователь @{user.username} пишет вам!")


# @router.business_message(Command("post"))
# async def start_command(msg: Message, bot: Bot, command: CommandObject):
#     # user, created = await sync_to_async(TelegramUser.objects.get_or_create)(user_id=msg.from_user.id)
#     # # if user.is_admin:
#     # builder = InlineKeyboardBuilder()
#     # builder.add(InlineKeyboardButton(text="BOT", url="http://t.me/MarioBrothers_new_bot?start=UH59ZYW"))
#     # builder.add(InlineKeyboardButton(text="Сайт", url="https://mariobro.cc"))
#     # builder.add(InlineKeyboardButton(text="Канал", url="https://t.me/+prcRs3PvG2c1YTll"))
#     # builder.adjust(1, 2)
#     # await bot.send_message("-1002249276088", text="post", reply_markup=builder.as_markup())
#     await bot.send_message("-1001844416402", text='.')
#
#
# @router.message(F.text.startswith("!add"))
# async def add_trigger(msg: Message, bot: Bot):
#     if msg.reply_to_message:
#         chat_member = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
#         print(chat_member.status)
#         if chat_member.status in ["creator", "administrator"]:
#             new_trigger = await sync_to_async(Trigger.objects.create)(chat_id=msg.chat.id, trigger_name=msg.text[5:].lower(), message_id=msg.reply_to_message.message_id)
#             await msg.reply(f"Триггер {new_trigger.trigger_name} успешно добавлен")
#
#
# @router.message(F.text.startswith("!triggers"))
# async def show_triggers(msg: Message, bot: Bot):
#     all_triggers = await sync_to_async(Trigger.objects.filter)(chat_id=msg.chat.id)
#     text = ""
#     if all_triggers:
#         for i in all_triggers:
#             text += i.trigger_name + "\n"
#         await msg.reply(text, parse_mode=None)
#     elif not all_triggers:
#         await msg.reply("Здесь нет триггеров")
#
#
# @router.message(F.text.startswith("!del"))
# async def del_trigger(msg: Message, bot: Bot):
#     chat_member = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
#     if chat_member.status in ["creator", "administrator"]:
#         try:
#             trigger = await sync_to_async(Trigger.objects.get)(chat_id=msg.chat.id, trigger_name=msg.text[5:].lower())
#             trigger.delete()
#             await msg.reply(f"Триггер {trigger.trigger_name} успешно удален")
#         except Exception as e:
#             print(e)
#             await msg.answer("Не удалось найти триггер")
#
# class TriggerFilter(BaseFilter):
#     async def __call__(self, message: Message) -> bool:
#         chat_id = message.chat.id
#         if message.text:
#             trigger_name = message.text.strip()
#             return Trigger.objects.filter(Q(chat_id=chat_id) & Q(trigger_name=trigger_name.lower())).exists()
#
#
# @router.message(TriggerFilter())
# async def check_trigger(msg: Message, bot: Bot):
#     chat_id = msg.chat.id
#     trigger_name = msg.text.strip()
#     trigger = Trigger.objects.filter(Q(chat_id=chat_id) & Q(trigger_name=trigger_name.lower())).first()
#     if trigger:
#         await bot.copy_message(chat_id=chat_id, from_chat_id=trigger.chat_id, message_id=trigger.message_id)
#
#


@router.message()
async def poster_photo(msg: Message, bot: Bot):
    user, created = await sync_to_async(TelegramUser.objects.get_or_create)(user_id=msg.from_user.id)
    await bot.forward_message(msg.from_user.id, "-1002455211388", 7)
    # if msg.photo:
    #     photo_id = msg.photo[-1].file_id
    #     builder = InlineKeyboardBuilder()
    #     builder.add(InlineKeyboardButton(text="ПОКУПКА", url="https://t.me/Operator_Butterfly"))
    #     builder.add(InlineKeyboardButton(text="Chat", url="https://t.me/+6gF26fuonpxhYjAx"))
    #     builder.add(InlineKeyboardButton(text="Channel", url="https://t.me/+WLak2v0dz7I0NTVh"))
    #     builder.adjust(1, 2)
    #     a = await bot.send_photo("-1002455211388", caption=".", photo=photo_id, reply_markup=builder.as_markup())
    #     print(a.chat.id, a.message_id)
    #     await bot.forward_message(msg.from_user.id, a.chat.id, a.message_id)
#         print(photo_id)
#         # builder = InlineKeyboardBuilder()
#         # builder.add(InlineKeyboardButton(text="🍁 Покупка у MARIO 🍁", url="http://t.me/MarioBrothers_new_bot?start=UH59ZYW"))
#         # builder.add(InlineKeyboardButton(text="🦖 Обмен у DINO 🦖", url="https://t.me/Dino_Obmen_RZV"))
#         # builder.add(InlineKeyboardButton(text="💟 УЧАСТВОВАТЬ В РУЛЕТКЕ 💟", url="https://t.me/RandomTGbot?start=7229911453"))
#         # # builder.add(InlineKeyboardButton(text="CHANNEL", url="https://t.me/+prcRs3PvG2c1YTll"))
#         # builder.adjust(1)
#         # await bot.send_photo("-1002249276088", caption=".", photo=photo_id,
#         #                      reply_markup=builder.as_markup())
#
#     # builder = InlineKeyboardBuilder()
#     # builder.add(InlineKeyboardButton(text="🔍 У меня НН", callback_data="have_nn"))
#     # builder.add(InlineKeyboardButton(text="⏱ Когда пополнение?", callback_data="when_replenishment"))
#     #
#     # from aiogram.types import KeyboardButton
#     # from aiogram.utils.keyboard import ReplyKeyboardBuilder
#     #
#     # builder_two = ReplyKeyboardBuilder()
#     # builder_two.add(KeyboardButton(text="🔍 У меня НН"))
#     # builder_two.add(KeyboardButton(text="⏱ Когда пополнение?"))
#     #
#     # await msg.answer("Выберите опцию:", reply_markup=builder_two.as_markup(resize_keyboard=True))
#     # await msg.answer("test", reply_markup=builder.as_markup())

