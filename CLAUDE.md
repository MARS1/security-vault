# Security Vault — Claude Instructions

> Personal cybersecurity knowledge base. Captures tips from Instagram and other sources,
> distills Mars's own written content, and tracks emerging threats and defenses.

**Type:** Obsidian research vault — standalone knowledge base
**Vault path:** `/Volumes/VM/OBSIDIAN/Security/`

## Notion

**Security Notion inbox:** https://www.notion.so/Security-3483d8e13700806a9ae6f08ae646d94a

**Link queue pattern:** Drop links in Inbox → Claude fetches and processes → files to correct folder. Do NOT just dump to `00-Inbox/` and leave. Route immediately using the category system.

## Vault Structure

| Folder | Contents |
|--------|----------|
| `00-Inbox/` | Temporary holding — never leave items here more than one session |
| `01-Threats/` | Attack vectors, malware types, social engineering, CVEs, threat intel |
| `02-Defense/` | Hardening checklists, monitoring, incident response, security controls |
| `03-Identity/` | Auth, IAM, zero trust, MFA, credential hygiene, access management |
| `04-Infrastructure/` | Network security, cloud posture, endpoint, OS-level hardening |
| `05-Tools/` | Commands, cheat sheets, security tools Mars actually uses or studies |
| `06-My-Content/` | Mars's own written posts, distilled messages, published cybersecurity content |
| `07-Sources/` | Instagram accounts, newsletters, podcasts, resources worth following |
| `08-Archive/` | Superseded or completed notes |
| `_attachments/` | Screenshots from Instagram, diagrams, images |
| `_templates/` | Security-Capture, My-Post, Daily-Note templates |
| `_credentials/` | API keys and secrets — NEVER committed |

## Extraction Workflow — CRITICAL

**All Instagram links and URLs are processed via `/content-extract`.** Never dump to `00-Inbox/` and leave.

**Workflow:**
1. User drops Instagram/YouTube/article link into Notion Inbox
2. Run `/content-extract` — skill reads Notion Inbox, extracts content (transcript, OCR, captions), routes to correct folder
3. After saving: **remove link from Inbox → add link to Outbox** — this prevents re-processing the same content
4. Create a dated batch record in Archive for reference
5. `00-Inbox/` vault folder is only a fallback for ambiguous captures — must be cleared before session ends

**Notion pages:**
- **Inbox:** https://www.notion.so/3483d8e1370080b39896fcb383aa1bdd — drop links here
- **Outbox:** https://www.notion.so/3483d8e13700807c82a0c981ef1706c4 — processed links land here
- **Archive:** https://www.notion.so/3483d8e1370081d1aad9d2f5639267eb — dated batch records

**Content-extract routing for this vault:**

| Content type | Folder |
|---|---|
| Attack vectors, malware, CVEs, social engineering | `01-Threats/` |
| Hardening, monitoring, incident response, controls | `02-Defense/` |
| Auth, IAM, MFA, zero trust, credential hygiene | `03-Identity/` |
| Network, cloud, endpoint, OS-level security | `04-Infrastructure/` |
| Security tools, commands, cheat sheets | `05-Tools/` |
| Mars's own written posts and messages | `06-My-Content/` |
| Sources to follow: accounts, newsletters, podcasts | `07-Sources/` |
| Ambiguous or unclear fit | `00-Inbox/` (process before session ends) |

## File Naming Convention

All notes use category prefix: `{category}--{slug}.md`

| Prefix | Routes to |
|--------|-----------|
| `threats--` | `01-Threats/` |
| `defense--` | `02-Defense/` |
| `identity--` | `03-Identity/` |
| `infra--` | `04-Infrastructure/` |
| `tools--` | `05-Tools/` |
| `my-content--` | `06-My-Content/` |
| `source--` | `07-Sources/` |

## Frontmatter Standard

All notes must include:

```yaml
---
title: Human-readable title
category: threats | defense | identity | infra | tools | my-content | source
tags: [tag1, tag2]
source: instagram | podcast | article | personal | unknown
date: YYYY-MM-DD
---
```

## Rules

- NEVER leave items in `00-Inbox/` across sessions — process or explicitly defer with a date
- NEVER commit the `_credentials/` folder
- Always append to SESSION-LOG.md at the end of every session
- Use `[[wiki links]]` for internal cross-references
- NEVER create files speculatively — only when explicitly asked or processing a capture
- Prefer editing existing notes over creating new ones
- Screenshots go in `_attachments/` and are linked from the note

## Session Logging

After every session, append to SESSION-LOG.md:
- Date, what was captured or written, key insights, files created or changed (3–5 lines max)
- Do NOT overwrite — always append

## DO NOT

- Commit `_credentials/` or any file matching `*.key`, `*.pem`, `.env`
- Create folders outside the established structure without asking
- Move or rename existing notes without explicit instruction (`mv` is blocked by permissions)
- Delete any notes

## Permissions

Vault-safe profile: `bypassPermissions` with destructive ops blocked.
`mv` is blocked — notes are never moved without explicit confirmation.
