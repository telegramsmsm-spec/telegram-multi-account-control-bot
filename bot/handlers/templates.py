from aiogram import Router, F
from aiogram.types import CallbackQuery
from bot.keyboards.common import back_home_kb

router = Router()

@router.callback_query(F.data == "menu_templates")
async def templates_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        "📝 <b>Templates Manager</b>\n\n"
        "• Internal report templates\n"
        "• External email templates\n"
        "• Multiple variations + variables\n"
        "• Arabic + English\n"
        "• Add / Edit / Preview / Activate",
        reply_markup=back_home_kb(),
        parse_mode="HTML"
    )
    await callback.answer()
