#!/usr/bin/env python3
"""
Security Vault — Inbox Sorter
Run: python3 sort-inbox.py

Routes 00-Inbox files to the correct topic folder based on:
  1. frontmatter `category` field (always wins)
  2. filename prefix (category--slug.md)
  3. files without a clear prefix are listed for manual review

Topic folders:
  01-Threats        — attack vectors, malware, CVEs, social engineering
  02-Defense        — hardening, monitoring, incident response
  03-Identity       — auth, IAM, MFA, zero trust, credentials
  04-Infrastructure — network, cloud, endpoint, OS security
  05-Tools          — commands, cheat sheets, tools
  06-My-Content     — Mars's own posts and written content
  07-Sources        — feeds, accounts, newsletters, podcasts
  08-Archive        — superseded or completed notes
"""

import os
import re
import shutil

VAULT = os.path.dirname(os.path.abspath(__file__))
INBOX = os.path.join(VAULT, '00-Inbox')

# Frontmatter `category` field → destination folder
CATEGORY_MAP = {
    'threats':        '01-Threats',
    'threat':         '01-Threats',
    'malware':        '01-Threats',
    'attack':         '01-Threats',
    'cve':            '01-Threats',
    'defense':        '02-Defense',
    'defensive':      '02-Defense',
    'hardening':      '02-Defense',
    'monitoring':     '02-Defense',
    'incident':       '02-Defense',
    'response':       '02-Defense',
    'identity':       '03-Identity',
    'iam':            '03-Identity',
    'auth':           '03-Identity',
    'mfa':            '03-Identity',
    'access':         '03-Identity',
    'credentials':    '03-Identity',
    'zero-trust':     '03-Identity',
    'infra':          '04-Infrastructure',
    'infrastructure': '04-Infrastructure',
    'network':        '04-Infrastructure',
    'cloud':          '04-Infrastructure',
    'endpoint':       '04-Infrastructure',
    'tools':          '05-Tools',
    'tool':           '05-Tools',
    'cheatsheet':     '05-Tools',
    'command':        '05-Tools',
    'my-content':     '06-My-Content',
    'content':        '06-My-Content',
    'post':           '06-My-Content',
    'source':         '07-Sources',
    'sources':        '07-Sources',
    'resource':       '07-Sources',
    'archive':        '08-Archive',
}

# Filename prefix → destination folder (order matters)
PREFIX_RULES = [
    (['threats--', 'threat--', 'malware--', 'attack--', 'cve--'],  '01-Threats'),
    (['defense--', 'defensive--', 'hardening--', 'incident--'],     '02-Defense'),
    (['identity--', 'iam--', 'auth--', 'mfa--', 'credentials--'],   '03-Identity'),
    (['infra--', 'infrastructure--', 'network--', 'cloud--'],        '04-Infrastructure'),
    (['tools--', 'tool--', 'cheatsheet--', 'command--'],            '05-Tools'),
    (['my-content--', 'content--', 'post--'],                        '06-My-Content'),
    (['source--', 'sources--', 'resource--'],                        '07-Sources'),
    (['archive--'],                                                   '08-Archive'),
]


def read_frontmatter(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    fm = {}
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, _, v = line.partition(':')
                fm[k.strip().lower()] = v.strip().lower()
    return fm


def route_file(fname, fm):
    # 1. Frontmatter category wins
    category = fm.get('category', '').strip()
    if category in CATEGORY_MAP:
        return CATEGORY_MAP[category]

    # 2. Filename prefix
    fname_lower = fname.lower()
    for prefixes, folder in PREFIX_RULES:
        for p in prefixes:
            if fname_lower.startswith(p):
                return folder

    return None  # stays in inbox — needs manual review


def main():
    if not os.path.isdir(INBOX):
        print(f'No inbox found at {INBOX}')
        return

    files = [f for f in sorted(os.listdir(INBOX)) if f.endswith('.md')]
    if not files:
        print('Inbox is empty. Nothing to sort.')
        return

    moved = []
    stayed = []

    for fname in files:
        src = os.path.join(INBOX, fname)
        fm = read_frontmatter(src)
        dest_folder = route_file(fname, fm)

        if dest_folder:
            dest_dir = os.path.join(VAULT, dest_folder)
            os.makedirs(dest_dir, exist_ok=True)
            dst = os.path.join(dest_dir, fname)
            shutil.move(src, dst)
            moved.append((fname, dest_folder))
        else:
            stayed.append((fname, fm.get('category', '(none)')))

    if moved:
        print(f'Sorted {len(moved)} file(s):')
        for fname, folder in moved:
            print(f'  {fname} → {folder}/')
    else:
        print('No files could be auto-routed.')

    if stayed:
        print(f'\n{len(stayed)} file(s) need a category before they can be sorted:')
        print('Add `category: threats|defense|identity|infra|tools|my-content|source` to frontmatter,')
        print('or rename with a category prefix (e.g. threats--your-note.md)\n')
        for fname, cat in stayed:
            print(f'  {fname}  (current category: {cat})')


if __name__ == '__main__':
    main()
