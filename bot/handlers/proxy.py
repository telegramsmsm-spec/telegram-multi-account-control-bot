from aiogram import Router, F
from aiogram.types import CallbackQuery
from bot.keyboards.common import back_home_kb

router = Router()

@router.callback_query(F.data == "menu_proxies")
async def proxy_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        "🌐 <b>Proxy Manager</b>\n\n"
        "• Add / Edit / Delete proxies\n"
        "• Auto health check\n"
        "• Bind one sticky proxy per account\n"
        "• Country matching preferred",
        reply_markup=back_home_kb(),
        parse_mode="HTML"
    )
    await callback.answer()
