from aiogram import Router, F
from aiogram.types import CallbackQuery
from bot.keyboards.accounts_kb import accounts_menu_kb
from bot.keyboards.common import back_home_kb

router = Router()

@router.callback_query(F.data == "accounts_all")
async def accounts_all(callback: CallbackQuery):
    await callback.message.edit_text(
        "📋 <b>All Accounts</b>\n\nList of every account with status and country.",
        reply_markup=back_home_kb("menu_accounts"),
        parse_mode="HTML"
    )
    await callback.answer()

@router.callback_query(F.data.startswith("country_"))
async def country_section(callback: CallbackQuery):
    country = callback.data.replace("country_", "").title()
    await callback.message.edit_text(
        f"🇰 <b>{country} Accounts</b>\n\nIsolated section for {country} accounts only.",
        reply_markup=back_home_kb("menu_accounts"),
        parse_mode="HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "account_add")
async def account_add(callback: CallbackQuery):
    await callback.message.edit_text(
        "➕ <b>Add New Account</b>\n\nSend phone number in international format.\nSession will be created and bound to proxy + country.",
        reply_markup=back_home_kb("menu_accounts"),
        parse_mode="HTML"
    )
    await callback.answer()
