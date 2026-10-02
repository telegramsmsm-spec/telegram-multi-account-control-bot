from aiogram import Router, F
from aiogram.types import CallbackQuery
from bot.keyboards.common import back_home_kb

router = Router()

@router.callback_query(F.data == "menu_reports")
async def reports_menu(callback: CallbackQuery):
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📢 Internal Reports", callback_data="report_internal")],
        [InlineKeyboardButton(text="📧 External Reports", callback_data="report_external")],
        [InlineKeyboardButton(text="◀ Back", callback_data="main_menu"),
         InlineKeyboardButton(text="🏠 Home", callback_data="main_menu")]
    ])
    await callback.message.edit_text(
        "🚨 <b>Report Center</b>\n\nInternal Telegram reports or External email reports.",
        reply_markup=kb,
        parse_mode="HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "report_internal")
async def report_internal(callback: CallbackQuery):
    await callback.message.edit_text(
        "📢 <b>Internal Reports</b>\n\n"
        "• Select accounts (All / Country / Manual)\n"
        "• Target group/channel\n"
        "• Choose report type\n"
        "• Unique realistic text per account\n"
        "• Sequential delayed execution",
        reply_markup=back_home_kb("menu_reports"),
        parse_mode="HTML"
    )
    await callback.answer()
