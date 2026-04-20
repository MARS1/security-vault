---
title: Vercel Hack — AI Tool Supply Chain Attack
category: threats
tags: [supply-chain, oauth, ai-tools, third-party, npm, github-tokens]
source: instagram
source-url: https://www.instagram.com/reel/DXVwxofjU5D/?igsh=MWh4M2Rnb3c3M2N3bw==
date: 2026-04-20
---

# Vercel Hack — AI Tool Supply Chain Attack

> "Vercel didn't get hacked because its security was weak. It got hacked because it was careless."

## Key Takeaway

A compromised third-party AI tool with OAuth access to Google Workspace gave attackers a direct path into Vercel's internal systems — no firewall breach, no zero-day exploit needed.

## What Happened

1. Vercel employees authorized a small third-party AI app with OAuth access to their Google Workspace (standard "click allow" flow)
2. That AI tool itself got compromised
3. Because the tool had OAuth permissions, attackers inherited those permissions — and walked straight into Vercel's internal systems

## What Was Stolen

Data for sale on the dark web for **$2 million**:
- 580 Vercel employee records
- Source code
- Internal database contents
- API tokens, NPM tokens, GitHub tokens

## Why the Tokens Matter Most

- **NPM token** → ability to publish packages → could push malicious code to **Next.js** updates → impacts millions of websites built on the framework
- **GitHub tokens** → access to source repositories
- This isn't just a Vercel problem — a buyer could compromise a huge chunk of JavaScript-powered internet

## The Attack Vector

```
Attacker compromises third-party AI tool
→ Tool already has OAuth access to Google Workspace
→ Attacker inherits permissions
→ Lateral movement into Vercel internals
→ Data exfiltration
```

## Defense Takeaway

- Audit every third-party app with OAuth access to your workspace — if it gets compromised, the attacker gets your permissions
- Treat AI tool integrations as a new attack surface, not just productivity tools
- Least-privilege OAuth: grant only what's needed, revoke when not actively used

## Related

- [[02-Defense/]] — hardening third-party access permissions
