from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📁 Accounts", callback_data="menu_accounts"),
            InlineKeyboardButton(text="🌐 Proxies", callback_data="menu_proxies")
        ],
        [
            InlineKeyboardButton(text="🔗 Join Center", callback_data="menu_join"),
            InlineKeyboardButton(text="📨 Messaging", callback_data="menu_messaging")
        ],
        [
            InlineKeyboardButton(text="🚨 Reports", callback_data="menu_reports"),
            InlineKeyboardButton(text="📝 Templates", callback_data="menu_templates")
        ],
        [
            InlineKeyboardButton(text="📊 Logs", callback_data="menu_logs"),
            InlineKeyboardButton(text="⚙️ Settings", callback_data="menu_settings")
        ]
    ])
