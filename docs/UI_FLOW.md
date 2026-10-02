# UI Flow - Pure Inline Buttons

## Design Rules
- No /commands ever
- Every interaction = callback_query
- Message text always clean + respectful
- Buttons arranged in logical rows (2-3 per row max)
- Back + Home always available

## Main Menu Example
```
🚀 Telegram Multi Control

Choose section:

[Accounts] [Proxies]
[Join Center] [Messaging]
[Reports] [Templates]
[Logs] [Settings]
```

## Accounts Submenu
```
📁 Accounts
All Accounts • Country Sections

[All Accounts]
[Egypt] [Saudi] [UAE]
[Iraq] [Syria] [Jordan]
[Morocco] [Algeria] [Tunisia]
[Custom] [Add New]
[Back] [Home]
```

## Messaging Flow
1. Messaging button
2. Select accounts (All / Country / Manual list)
3. Enter group link
4. Upload txt
5. Set delays
6. Confirm → Start
7. Live progress message with Pause/Stop buttons

## Report Flow
Same pattern: select accounts → target → type → confirm → sequential run with live status

All messages use formal respectful Arabic/English mix as needed.
