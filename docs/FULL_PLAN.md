# FULL MVP PLAN - Telegram Multi-Account Control Bot (Admin Only)

## Access Control (Critical)
- Only Telegram user IDs listed in ADMIN_IDS can use any feature
- Middleware blocks every message and every callback from non-admins
- Non-admins receive clear "Access denied" message
- Owner has full unrestricted control

## 1. Core Foundation
- Session storage (StringSession)
- Account fields: phone, session_string, proxy_id, country, status, last_activity, notes
- Full control API over every account

## 2. Account Organization
- Global "All Accounts"
- Country sections (isolated):
  - Egypt, Saudi Arabia, UAE, Iraq, Syria, Jordan, Morocco, Algeria, Tunisia, Custom
- Auto placement on add
- Move between sections

## 3. Proxy System
- Mandatory binding
- Types: SOCKS5 (primary), HTTP, MTProto
- 1 account = 1 sticky proxy
- Health check + auto replace
- Country preference matching

## 4. Join Modules
### Search Join
- Keyword search public groups
- Filters + controlled speed
- Select accounts: All / Country / Manual

### Private Link Join
- t.me/+ or private hash
- Handles join requests
- Same account selection

## 5. Group Messaging (TXT Sender)
- Upload .txt
- Line-by-line sequential
- Account select: All / Country / Manual
- Target: username or invite link
- Delays + human jitter
- Pause / Resume / Stop
- Per-line success log

## 6. Internal Report Module
- Target group/channel
- Account select: All / Country / Manual
- Unique realistic report text per account
- Sequential + delayed
- Full log

## 7. External Report Module
- Linked email accounts
- Bot collects: email, password, 2FA/app password
- Targets: abuse@telegram.org, dmca@telegram.org, stop@telegram.org, copyright@telegram.org
- Professional templates
- Unique per email

## 8. Template System
- Banks for internal + external
- Variables + multiple variations
- Arabic + English
- Admin CRUD + preview

## 9. UI/UX Rules
- Zero slash commands (except /start for owner)
- Pure InlineKeyboardMarkup multi-level
- Every screen has Back + Home
- Clear respectful messages
- Consistent layout

## 10. Safety
- Per-account rate limits
- FloodWait auto sleep
- Session keep-alive
- Proxy health loop
- Global pause switch
- Complete action logs
- Admin-only enforcement on every request
