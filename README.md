# Telegram Multi-Account Control Bot - Full MVP

**Complete production-ready architecture**  
Inline buttons only • Country sections • Sessions • Proxies • Join • TXT Messaging • Internal + External Reports • Professional templates

## Features (Nothing Missing)

### 1. Core
- Permanent StringSession / TData storage
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

### 9. UI/UX (Critical)
- **Zero /** commands
- Pure Inline Keyboard multi-level menus
- Back + Home on every screen
- Breadcrumbs
- Clear respectful messages on every click
- Consistent layout, no mess

### 10. Safety
- Rate limits
- Flood-wait auto-handle
- Session keep-alive
- Global pause
- Complete logs

## Project Structure
```
telegram-multi-account-control-bot/
├── bot/
│   ├── main.py
│   ├── config.py
│   ├── handlers/
│   │   ├── start.py
│   │   ├── accounts.py
│   │   ├── proxy.py
│   │   ├── join.py
│   │   ├── messaging.py
│   │   ├── reports_internal.py
│   │   ├── reports_external.py
│   │   ├── templates.py
│   │   └── navigation.py
│   ├── keyboards/
│   │   ├── main_menu.py
│   │   ├── accounts_kb.py
│   │   ├── countries_kb.py
│   │   ├── proxy_kb.py
│   │   ├── join_kb.py
│   │   ├── messaging_kb.py
│   │   ├── reports_kb.py
│   │   └── common.py
│   ├── services/
│   │   ├── session_manager.py
│   │   ├── proxy_manager.py
│   │   ├── account_service.py
│   │   ├── join_service.py
│   │   ├── messaging_service.py
│   │   ├── report_service.py
│   │   └── template_service.py
│   ├── database/
│   │   ├── models.py
│   │   └── db.py
│   └── utils/
│       ├── delays.py
│       ├── validators.py
│       └── logger.py
├── data/
│   ├── sessions/
│   ├── proxies/
│   ├── templates/
│   └── logs/
├── requirements.txt
├── .env.example
├── .gitignore
└── docs/
    ├── FULL_PLAN.md
    ├── UI_FLOW.md
    └── API.md
```

## Tech Stack
- Python 3.11+
- aiogram 3.x (pure inline)
- Telethon / Pyrogram for user accounts
- SQLAlchemy + SQLite/PostgreSQL
- python-socks / aiohttp-socks
- pydantic-settings

## Quick Start
1. Clone
2. `pip install -r requirements.txt`
3. Copy `.env.example` → `.env` and fill BOT_TOKEN + API_ID + API_HASH
4. `python -m bot.main`

## Status
Full MVP structure published.  
Core modules skeleton ready for implementation.

**Owner:** telegramsmsm-spec  
**Repo:** https://github.com/telegramsmsm-spec/telegram-multi-account-control-bot
