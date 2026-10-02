from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from bot.keyboards.main_menu import main_menu_kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "🚀 <b>Telegram Multi-Account Control</b>\n\n"
        "Full control panel ready.\n"
        "All actions use buttons only.",
        reply_markup=main_menu_kb(),
        parse_mode="HTML"
    )

@router.callback_query(F.data == "main_menu")
async def cb_main_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        "🚀 <b>Telegram Multi-Account Control</b>\n\n"
        "Choose section:",
        reply_markup=main_menu_kb(),
        parse_mode="HTML"
    )
    await callback.answer()
