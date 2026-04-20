---
title: "DR-001: Three-Stage Notion Flow — Inbox, Outbox, Archive"
date: 2026-04-20
status: accepted
vault: Security
---

# DR-001: Three-Stage Notion Flow — Inbox, Outbox, Archive
**Date:** 2026-04-20
**Vault:** Security

## Context
The Security vault receives Instagram reels and URLs via a Notion inbox for
extraction and distillation. Other vaults use a two-stage flow (Inbox → Archive).
Without a processed-link destination, the /content-extract skill would re-read
and re-process the same links every session, accumulating duplicates.

## Decision
Use a three-stage Notion flow specific to this vault:
- **Inbox** — new links land here, awaiting extraction
- **Outbox** — links move here after successful extraction (prevents re-processing)
- **Archive** — dated batch records created by /content-extract for auditing

The Outbox is not part of the global /content-extract skill. It is documented in
this vault's CLAUDE.md and MODS.md only, and the skill reads those files to
adapt its behavior per vault.

## Consequences
- Every /content-extract run on this vault must remove the link from Inbox AND add it to Outbox — both steps required
- Outbox grows over time as a human-readable log of what has been processed
- Archive holds Claude's dated batch records separately from the Outbox human log
- If this vault is ever migrated or the skill is updated, the Outbox URL must be preserved in MODS.md
- Future vaults with high-volume inboxes should consider this same pattern
