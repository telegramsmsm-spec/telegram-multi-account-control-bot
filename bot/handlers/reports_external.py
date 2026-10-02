from aiogram import Router, F
from aiogram.types import CallbackQuery
from bot.keyboards.common import back_home_kb

router = Router()

@router.callback_query(F.data == "report_external")
async def report_external(callback: CallbackQuery):
    await callback.message.edit_text(
        "📧 <b>External Reports</b>\n\n"
        "• Link Gmail / Outlook / other emails\n"
        "• Bot collects email + password + 2FA\n"
        "• Sends to abuse@ / dmca@ / stop@ / copyright@\n"
        "• Professional unique templates per email",
        reply_markup=back_home_kb("menu_reports"),
        parse_mode="HTML"
    )
    await callback.answer()
