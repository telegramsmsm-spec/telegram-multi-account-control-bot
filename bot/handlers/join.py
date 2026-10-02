from aiogram import Router, F
from aiogram.types import CallbackQuery
from bot.keyboards.common import back_home_kb

router = Router()

@router.callback_query(F.data == "menu_join")
async def join_menu(callback: CallbackQuery):
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔍 Search Join", callback_data="join_search")],
        [InlineKeyboardButton(text="🔗 Private Link Join", callback_data="join_link")],
        [InlineKeyboardButton(text="◀ Back", callback_data="main_menu"),
         InlineKeyboardButton(text="🏠 Home", callback_data="main_menu")]
    ])
    await callback.message.edit_text(
        "🔗 <b>Join Center</b>\n\nChoose join method:",
        reply_markup=kb,
        parse_mode="HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "join_search")
async def join_search(callback: CallbackQuery):
    await callback.message.edit_text(
        "🔍 <b>Search Join</b>\n\nEnter keywords to search public groups.\nThen select accounts (All / Country / Manual).",
        reply_markup=back_home_kb("menu_join"),
        parse_mode="HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "join_link")
async def join_link(callback: CallbackQuery):
    await callback.message.edit_text(
        "🔗 <b>Private Link Join</b>\n\nPaste invite link (t.me/+ or hash).\nSelect accounts and join with full protection.",
        reply_markup=back_home_kb("menu_join"),
        parse_mode="HTML"
    )
    await callback.answer()
