from aiogram import Router, F
from aiogram.types import CallbackQuery
from bot.keyboards.main_menu import main_menu_kb

router = Router()

# Central navigation hub - all menu_* callbacks land here or in specific handlers
@router.callback_query(F.data.startswith("menu_"))
async def menu_router(callback: CallbackQuery):
    data = callback.data
    if data == "menu_accounts":
        from bot.keyboards.accounts_kb import accounts_menu_kb
        await callback.message.edit_text(
            "📁 <b>Accounts</b>\nAll Accounts • Country Sections",
            reply_markup=accounts_menu_kb(),
            parse_mode="HTML"
        )
    elif data == "menu_proxies":
        await callback.message.edit_text(
            "🌐 <b>Proxy Manager</b>\n\nManage sticky proxies for every account.",
            reply_markup=main_menu_kb(),  # placeholder - real kb later
            parse_mode="HTML"
        )
    elif data == "menu_join":
        await callback.message.edit_text(
            "🔗 <b>Join Center</b>\n\nSearch Join or Private Link Join.",
            reply_markup=main_menu_kb(),
            parse_mode="HTML"
        )
    elif data == "menu_messaging":
        await callback.message.edit_text(
            "📨 <b>Messaging</b>\n\nUpload TXT and send line by line.",
            reply_markup=main_menu_kb(),
            parse_mode="HTML"
        )
    elif data == "menu_reports":
        await callback.message.edit_text(
            "🚨 <b>Reports</b>\n\nInternal + External report modules.",
            reply_markup=main_menu_kb(),
            parse_mode="HTML"
        )
    elif data == "menu_templates":
        await callback.message.edit_text(
            "📝 <b>Templates</b>\n\nManage all professional templates.",
            reply_markup=main_menu_kb(),
            parse_mode="HTML"
        )
    elif data == "menu_logs":
        await callback.message.edit_text(
            "📊 <b>Logs</b>\n\nFull action history.",
            reply_markup=main_menu_kb(),
            parse_mode="HTML"
        )
    elif data == "menu_settings":
        await callback.message.edit_text(
            "⚙️ <b>Settings</b>\n\nDelays, limits, safety switches.",
            reply_markup=main_menu_kb(),
            parse_mode="HTML"
        )
    await callback.answer()
