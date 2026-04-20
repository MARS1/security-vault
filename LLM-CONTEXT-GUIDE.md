# LLM Context Guide — Security Vault

> Read this first when working in this vault. It tells you what this vault is,
> what it's for, and how to navigate it effectively.

## What This Vault Is

A personal cybersecurity knowledge base for Mars. It captures security tips encountered on Instagram and elsewhere, distills Mars's own written cybersecurity content, and tracks threats, tools, and defenses worth knowing. This is not a code project — it is a living reference vault.

**Research vault.** No companion codebase.

## Two Flows of Content

**Inbound (external captures):**
Instagram tips, articles, podcasts → Notion inbox → processed into topic folders

**Outbound (Mars's own content):**
Mars writes cybersecurity posts or messages → stored in `06-My-Content/` → distilled insight retained

## Folder Map

| Folder | What lives here | Questions it answers |
|--------|-----------------|----------------------|
| `00-Inbox/` | Temporary unprocessed captures | "What just came in?" |
| `01-Threats/` | Attack types, malware, social engineering, CVEs | "How does this attack work?" |
| `02-Defense/` | Hardening, monitoring, incident response | "How do I protect against X?" |
| `03-Identity/` | Auth, IAM, MFA, zero trust, credentials | "How should I handle access?" |
| `04-Infrastructure/` | Network, cloud, endpoint, OS security | "Is my infra secure?" |
| `05-Tools/` | Commands, cheat sheets, tools Mars uses | "What tool or command do I use for X?" |
| `06-My-Content/` | Mars's own posts, messages, written content | "What have I already written about X?" |
| `07-Sources/` | Accounts, newsletters, podcasts worth following | "Where should I look for more on X?" |
| `08-Archive/` | Completed or superseded notes | "What did I used to think about X?" |

## Sorting Rule — Hard Requirement

**`00-Inbox/` is a transit zone, not a destination.** Items dropped here must be processed within the same session. Use `python3 sort-inbox.py` to auto-route files that have the correct frontmatter `category` field or filename prefix. Never let inbox backlog accumulate.

## File Naming

All notes use: `{category}--{slug}.md`

Examples:
```
threats--sim-swapping-explained.md
defense--hardening-macos-2026.md
identity--passkeys-vs-passwords.md
infra--cloudflare-zero-trust-setup.md
tools--nmap-quick-reference.md
my-content--instagram-post-phishing-red-flags.md
source--darknet-diaries-podcast.md
```

## Domain Context

- Mars is building cybersecurity fluency partly from Instagram content — sources are often short-form, practical tips rather than academic papers
- Content Mars writes is for a general audience — clarity over jargon
- The vault is personal and private — treat all contents accordingly
- Cross-reference KodeArk (`/Volumes/VM/OBSIDIAN/KodeArk/`) if a security pattern has a technical implementation angle (e.g., auth flows, encryption recipes)

## Session Rules

1. Read CLAUDE.md before starting any session
2. Process all Notion inbox items before closing — never leave them unrouted
3. Append to SESSION-LOG.md when the session ends
4. Do not create files speculatively — ask first
5. Use `[[wiki links]]` for all internal cross-references

## What Good Looks Like

- `00-Inbox/` is empty at the end of every session
- Notes are titled descriptively: not "phishing notes" but "phishing-anatomy-how-attackers-spoof-email.md"
- Every note has frontmatter with `category`, `source`, and `date`
- `06-My-Content/` grows as Mars writes — searchable by topic
- SESSION-LOG.md has an entry after every working session
