# FULL MVP PLAN - Telegram Multi-Account Control Bot

## 1. Core Foundation
- Session storage (StringSession preferred)
- Account fields: phone, session_string, proxy_id, country, status, last_activity, notes
- Full control API over every account

## 2. Account Organization
- Global "All Accounts"
- Country sections (isolated):
  - Egypt
  - Saudi Arabia
  - UAE
  - Iraq
  - Syria
  - Jordan
  - Morocco
  - Algeria
  - Tunisia
  - Custom
- Auto placement on add
- Move between sections

## 3. Proxy System
- Mandatory binding
- Types: SOCKS5 (primary), HTTP, MTProto
- 1 account = 1 sticky proxy
- Health check (connect + Telegram ping)
- Auto replace on fail
- Country preference matching

## 4. Join Modules
### Search Join
- Keyword search public groups
- Filters: members, language, activity
- Select accounts: All / Country / Manual
- Controlled speed + random delays

### Private Link Join
- t.me/+ or private hash
- Handles join requests
- Same account selection

## 5. Group Messaging (TXT Sender)
- Upload .txt
- Line-by-line sequential
- Account select: All / Country / Manual
- Target: username or invite link
- Delays configurable + human jitter
- Pause / Resume / Stop
- Per-line success log

## 6. Internal Report Module
- Target group/channel
- Account select: All / Country / Manual
- Unique realistic report text per account
- Categories: spam, violence, porn, copyright, fake, child, other
- Sequential + delayed
- Full log

## 7. External Report Module
- Linked email accounts (Gmail etc.)
- Bot collects: email, password, 2FA/app password
- Targets: abuse@telegram.org, dmca@telegram.org, stop@telegram.org, copyright@telegram.org
- Professional templates
- Unique per email
- Tracking

## 8. Template System
- Banks for internal + external
- Variables: {group_name}, {link}, {date}, {reason}
- Multiple Arabic + English variations
- Admin CRUD + preview

## 9. UI/UX Rules (Non-Negotiable)
- Zero slash commands
- Pure InlineKeyboardMarkup multi-level
- Every screen has:
  - Clear title + breadcrumb
  - Consistent button rows
  - Back button
  - Home button (deep levels)
- Every callback → polished respectful message
- Loading / success / error states clean
- No messy floating text

## 10. Safety
- Per-account rate limits
- FloodWait auto sleep
- Session keep-alive pings
- Proxy health loop
- Global pause switch
- Complete action logs with timestamps

## Menu Tree
Main
├─ Accounts
│  ├─ All
│  ├─ By Country
│  ├─ Add Account
│  └─ Status
├─ Proxies
├─ Join
│  ├─ Search
│  └─ Link
├─ Messaging (TXT)
├─ Reports
│  ├─ Internal
│  └─ External
├─ Templates
├─ Logs
└─ Settings
