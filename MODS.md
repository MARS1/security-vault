# Security Vault — MODS

## Notion

| Page | URL |
|------|-----|
| Security root | https://www.notion.so/Security-3483d8e13700806a9ae6f08ae646d94a |
| Inbox (links to extract) | https://www.notion.so/3483d8e1370080b39896fcb383aa1bdd |
| Outbox (processed links) | https://www.notion.so/3483d8e13700807c82a0c981ef1706c4 |
| Archive (dated batch records) | https://www.notion.so/3483d8e1370081d1aad9d2f5639267eb |

**Workflow:** Drop Instagram links into Notion Inbox → run `/content-extract` → skill extracts content, routes to vault folder, moves link from Inbox to Outbox, creates dated batch record in Archive.

## Autonomy & Direct Action

- When you have direct tool access (SSH, git, Airtable MCP, Notion MCP, Bash), USE IT — do not ask the user to run manual terminal commands, paste URLs, or perform UI actions you could do yourself
- Never commit code changes without explicit user approval — stage, show diff, summarize, then wait
- For OAuth/auth links, open in Brave (not Chrome) — never ask user to open the browser manually
- When stuck after 2–3 search attempts, STOP and ask rather than continuing to grep blindly
- When a session type has an existing skill (`/content-extract`, `/session-close`, etc.), USE THE SKILL — do not write custom scripts

## Repos

| Vault | Path | VCS | Branch |
|-------|------|-----|--------|
| Security | `/Volumes/VM/OBSIDIAN/Security/` | git | main | https://github.com/MARS1/security-vault.git |
