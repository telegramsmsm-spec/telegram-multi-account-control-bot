# Telegram Multi-Account Control Bot - Full MVP (Admin Only)

**Complete production-ready architecture**  
**Only the owner/admin can use any feature**

Inline buttons only • Country sections • Sessions • Proxies • Join • TXT Messaging • Internal/External Reports • Professional templates

## Access Control
- Hard admin-only lock via middleware
- Only Telegram user IDs listed in `ADMIN_IDS` can interact with the bot
- Everyone else receives "Access denied" and is blocked
- Applied to every message and every button press

## Features (Nothing Missing)

### 1. Core
- Permanent StringSession storage
- Full account control
- Status tracking (active / limited / banned / warming)

### 2. Account Organization
- All Accounts view
- Isolated country sections: Egypt, Saudi, UAE, Iraq, Syria, Jordan, Morocco, Algeria, Tunisia, Custom
- Auto-sort + move between sections

### 3. Proxy System
- Mandatory 1 sticky proxy per account
- SOCKS5 / HTTP / MTProto
- Health checks + auto-replace
- Country matching

### 4. Join
- Search Join (keyword + filters)
- Private Link Join (invite links + approval handling)
- Select: All / Country / Manual

### 5. Group Messaging (TXT)
- Upload .txt → line-by-line sequential send
- Account select: All / Country / Manual
- Delays + human randomization
- Pause / Resume / Stop + full logs

### 6. Internal Reports
- Any group/channel
- Unique realistic text per account
- Sequential delayed execution
- Arabic + English templates

### 7. External Reports
- Gmail + all email providers
- Collects email/password/2FA
- Official Telegram addresses (abuse, dmca, stop, copyright)
- Professional unique messages

### 8. Templates
- Full banks with variables
- Multiple variations
- Easy manage

### 9. UI/UX
- Zero slash commands (except /start for owner)
- Pure Inline Keyboard multi-level menus
- Back + Home on every screen
- Breadcrumbs
- Clear respectful messages on every click
- Consistent layout

### 10. Safety
- Rate limits
- Flood-wait auto-handle
- Session keep-alive
- Global pause
- Complete logs
- Admin-only enforcement

## Project Structure
```
telegram-multi-account-control-bot/
├── bot/
│   ├── main.py
│   ├── config.py
│   ├── middlewares/
│   │   └── admin.py          # Admin-only lock
│   ├── handlers/
│   ├── keyboards/
│   ├── services/
│   ├── database/
│   └── utils/
├── data/
├── docs/
├── requirements.txt
├── .env.example
└── .gitignore
```

## Quick Start
1. Clone the repo
2. `pip install -r requirements.txt`
3. Copy `.env.example` → `.env`
4. Put your Telegram user ID in `ADMIN_IDS=`
5. Fill BOT_TOKEN, API_ID, API_HASH
6. `python -m bot.main`

Only the ID(s) in ADMIN_IDS will be able to use the bot.

**Repo:** https://github.com/telegramsmsm-spec/telegram-multi-account-control-bot
