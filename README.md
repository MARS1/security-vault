# Security Vault

> Personal cybersecurity knowledge base — capturing tips, distilling content, tracking threats and defenses.

## Structure

| Folder | Contents |
|--------|----------|
| `00-Inbox/` | Transit zone — process every session, never leave items here |
| `01-Threats/` | Attack vectors, malware, CVEs, social engineering |
| `02-Defense/` | Hardening, monitoring, incident response |
| `03-Identity/` | Auth, IAM, MFA, zero trust, credential hygiene |
| `04-Infrastructure/` | Network, cloud, endpoint, OS security |
| `05-Tools/` | Commands, cheat sheets, security tools |
| `06-My-Content/` | Mars's own written posts and messages |
| `07-Sources/` | Accounts, newsletters, podcasts to follow |
| `08-Archive/` | Superseded or completed notes |

## Getting Started

Open in Obsidian: File → Open vault → select this folder

Start at [SECURITY-BRAIN.md](SECURITY-BRAIN.md)

## Sorting

Auto-route inbox files after capturing:
```bash
python3 sort-inbox.py
```

## AI Sessions

```bash
cd /Volumes/VM/OBSIDIAN/Security
claude
```

CLAUDE.md contains session rules. SESSION-LOG.md tracks what was done each session.
