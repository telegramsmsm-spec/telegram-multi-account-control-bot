from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.keyboards.common import back_home_kb

def accounts_menu_kb() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="📋 All Accounts", callback_data="accounts_all")],
        [
            InlineKeyboardButton(text="🇪🇬 Egypt", callback_data="country_egypt"),
            InlineKeyboardButton(text="🇸🇦 Saudi", callback_data="country_saudi")
        ],
        [
            InlineKeyboardButton(text="🇦🇪 UAE", callback_data="country_uae"),
            InlineKeyboardButton(text="🇮🇶 Iraq", callback_data="country_iraq")
        ],
        [
            InlineKeyboardButton(text="🇸🇾 Syria", callback_data="country_syria"),
            InlineKeyboardButton(text="🇯🇴 Jordan", callback_data="country_jordan")
        ],
        [
            InlineKeyboardButton(text="🇲🇦 Morocco", callback_data="country_morocco"),
            InlineKeyboardButton(text="🇩🇿 Algeria", callback_data="country_algeria")
        ],
        [
            InlineKeyboardButton(text="🇹🇳 Tunisia", callback_data="country_tunisia"),
            InlineKeyboardButton(text="🌐 Custom", callback_data="country_custom")
        ],
        [InlineKeyboardButton(text="➕ Add Account", callback_data="account_add")],
        [
            InlineKeyboardButton(text="◀ Back", callback_data="main_menu"),
            InlineKeyboardButton(text="🏠 Home", callback_data="main_menu")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)
