from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def back_home_kb(back_callback: str = "main_menu") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="◀ Back", callback_data=back_callback),
            InlineKeyboardButton(text="🏠 Home", callback_data="main_menu")
        ]
    ])

def confirm_kb(yes_cb: str, no_cb: str = "main_menu") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Confirm", callback_data=yes_cb),
            InlineKeyboardButton(text="❌ Cancel", callback_data=no_cb)
        ]
    ])
