from aiogram import Router, F
from aiogram.types import CallbackQuery
from bot.keyboards.common import back_home_kb

router = Router()

@router.callback_query(F.data == "menu_messaging")
async def messaging_menu(callback: CallbackQuery):
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📄 Upload TXT & Send", callback_data="msg_start")],
        [InlineKeyboardButton(text="◀ Back", callback_data="main_menu"),
         InlineKeyboardButton(text="🏠 Home", callback_data="main_menu")]
    ])
    await callback.message.edit_text(
        "📨 <b>Group Messaging</b>\n\n"
        "Upload a .txt file.\n"
        "Bot sends line by line in exact order.\n"
        "Select accounts: All / Country / Manual.",
        reply_markup=kb,
        parse_mode="HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "msg_start")
async def msg_start(callback: CallbackQuery):
    await callback.message.edit_text(
        "📄 <b>Start Messaging</b>\n\n"
        "1. Choose accounts (All / Country / Manual)\n"
        "2. Send group username or invite link\n"
        "3. Upload the .txt file\n"
        "4. Set delays\n"
        "5. Confirm",
        reply_markup=back_home_kb("menu_messaging"),
        parse_mode="HTML"
    )
    await callback.answer()
