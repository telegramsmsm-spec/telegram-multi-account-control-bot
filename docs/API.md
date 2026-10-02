# Internal Service API Overview

## SessionManager
- get_client(account_id, session_string, proxy) → Telethon client
- disconnect_all()

## ProxyManager
- check_proxy(proxy_dict) → bool
- assign_proxy(account_id, proxy_id)

## MessagingService
- send_from_txt(accounts, group, lines, delay_min, delay_max)

## ReportService
- internal_report(accounts, target, report_type, templates)
- external_report(email_accounts, target_address, templates)

All services are async and designed for sequential safe execution.
